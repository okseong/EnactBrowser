
import os
import pytesseract
import re
import sys
import time
import urlparse

from driver_runner import runs_only_on
from inspect import getframeinfo, stack
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from tests.libaprt import AppRuntimeTest

TEST_CONFIGS = {'uri': {'media_path': './media/time_1080p_uri.mp4',
                    'reference_strings': ["TLeft", "Top", "TRight",
                                        "Left", "00", "Right",
                                        "BLeft", "Bottom", "BRight"],
                    'last_number_of_video': 30},
            'mse': {'media_path': './media/time_1080p.mpd',
                    'reference_strings': ["TLeft", "Top", "TRight",
                                        "Left", "00", "Right",
                                        "BLeft", "Bottom", "BRight"],
                    'last_number_of_video': 30}
            }


def debug_info():
st = stack()
caller = getframeinfo(st[1][0])

for f in st:
    if getframeinfo(f[0]).filename != __file__:
        caller = getframeinfo(f[0])
        return "%s:%d" % (os.path.basename(caller.filename), caller.lineno)
return "%s:%d" % (os.path.basename(caller.filename), caller.lineno)


@runs_only_on('wam_demo')
class MediaTest(AppRuntimeTest):
def __init__(self, test):
    super(MediaTest, self).__init__()
    self.webserver = "http://%s:8888/" % self.host_ip
    self.media_player_page = {'path': "media_test_player_page.html",
                            'title': "Media Test Page",
                            'js_media_object': "video",
                            'media_element_id': "video"}

    self.media_path = TEST_CONFIGS[test]['media_path']
    self.reference_video_strings = TEST_CONFIGS[test]['reference_strings']
    self.last_number_of_video = TEST_CONFIGS[test]['last_number_of_video']
    self.app_info = {'app_id': "bing", 'title': "Bing"}
    self.app_windows = []

def log(self, msg, newline=True, debug=True):
    if debug:
        sys.stderr.write("[%35s]\t%s" % (debug_info(), msg))
    else:
        sys.stderr.write("%s" % msg)

    if newline:
        sys.stderr.write("\n")

def prepare(self, screenshot_filename='loaded.png'):
    # App Launch
    app_id, app_title = self.app_info.values()
    self.launch_app(app_id, app_title, True)

    # Load a media file
    self.load_video_on_media_test_player(
        app_id=app_id,
        screenshot_filename=screenshot_filename)

def get_string_from_image_by_ocr(self, img):
    return pytesseract.image_to_string(img)

def get_numbers_from_string(self, string):
    return re.sub("[^0-9]", "", string)

def get_number_array_from_image(self, image):
    # Returns a string of numbers
    num_str = self.get_numbers_from_string(
        self.get_string_from_image_by_ocr(image))
    return map(int, num_str.split())

def compare_image_with_string_array(self, image, reference_string_array,
                                    exception_message="""
                                    String Array Compare Failure
                                    """):
    # If all the strings in |reference_string_array| are not in
    # |string_from_image| raise an exception.
    image_str = self.get_string_from_image_by_ocr(
        image).encode("ascii", 'ignore')
    valid_image_str = re.sub(r"[^A-Za-z0-9\s]+", '', image_str)
    # String to array with strings
    string_array_from_image = valid_image_str.split()

    comparision_result = (
        set(reference_string_array) - set(string_array_from_image))
    if comparision_result:
        raise Exception("""
            %s
            Reference string compare error : [Comparison Result]
            %s
            [Reference]
            %s
            [Screenshot]
            %s
            """ % (exception_message, comparision_result,
                reference_string_array, string_array_from_image))
    self.log(msg="Strings in the image - OK", debug=False)

def assign_video_source(self, url):
    disassembled = urlparse.urlparse(url)
    _, extention = os.path.splitext(
        os.path.basename(disassembled.path))

    if extention == ".mpd":
        self.log("Load media (MSE) : %s" % url)
        self.driver.execute_script(
            """
            let url = '%s';
            let player = dashjs.MediaPlayer().create();
            player.initialize( video, url, false);
            """ % (url))
    else:
        self.log("Load media (URI) : %s" % url)
        self.driver.execute_script("video.src = '%s'" % url)

def load_video_on_media_test_player(self, app_id,
                                    screenshot_filename='loaded.png'):
    def assign_video(media_url):
        self.driver.execute_script("document._video_loaded = false;")
        self.assign_video_source(media_url)
        # Wait until the video is loaded.
        self.uawait_until("document._video_loaded === true",
                        "Video Load failure"
                        " [ video.onloaded not called. ]")
        time.sleep(3)

    # Load uri_media_test_page.html.

    self.log("load player page : %s" % urlparse.urljoin(
        self.webserver, self.media_player_page['path']))
    self.load_content(app_id,
                    urlparse.urljoin(
                        self.webserver,
                        self.media_player_page['path']),
                    self.media_player_page['title'])

    # Wait the video element's presence.
    try:
        self.wait.until(EC.presence_of_element_located(
            (By.ID, self.media_player_page['media_element_id'])))
    except TimeoutException:
        raise Exception("Video element presence failure.")

    # Assign media url to video.src

    media_url = urlparse.urljoin(self.webserver, self.media_path)
    assign_video(media_url)

    # Check if a video has been loaded and rendered correctly.
    self.log("Check strings in captured image from the video loaded : ",
            False)

    for t in range(0, 10):
        try:
            self.log("Screen capture %d" % t, debug=False)
            img = self.get_screenshot(screenshot_filename)
            self.compare_image_with_string_array(
                img, self.reference_video_strings,
                """Video rendering failure
                [ the loaded video doesn't display its content correctly. ]
                """)
            break
        except Exception as e:
            self.log("%s" % str(e))
            # Todo : Remove below assign_video(), which is a
            # workaround fix for NEVA-5051, when NEVA-5051 is not
            # reproducible
            assign_video(media_url)
            if t == 9:
                raise(e)
            continue

    self.log("Video has been loaded. Duration : %f" % self.get_duration())

def send_keys(self, key):
    body = self.driver.find_element(By.XPATH, "//body")
    body.send_keys(key)

def play(self):
    self.log("Play")
    self.send_keys("k")

def pause(self):
    self.log("Pause")
    self.send_keys("p")

def seek_to(self, time):
    self.driver.execute_script('%s.currentTime=%f' % (
        self.media_player_page['media_element_id'], time))

def enter_fullscreen(self):
    self.log("Enter Fullscreen")
    self.send_keys("f")

def exit_fullscreen(self):
    self.log("Exit Fullscreen")
    self.send_keys("x")

def get_currentTime(self):
    return self.driver.execute_script(
        "return %s.currentTime;"
        % self.media_player_page['js_media_object'])

def get_duration(self):
    return self.driver.execute_script(
        "return %s.duration;"
        % self.media_player_page['js_media_object'])

def wait_until_currentTime(self, playback_time, error_msg="", timeout=60,
                        interval=0.2):
    start_time = time.time()
    current_time = time.time()
    video_currentTime = None

    while current_time - start_time < timeout:
        video_currentTime = self.get_currentTime()
        if video_currentTime >= playback_time:
            self.log("%s.currentTime is reached at %f in %f sec(s)"
                    % (self.media_player_page['js_media_object'],
                        video_currentTime, current_time - start_time))
            return
        time.sleep(interval)
        current_time = time.time()

    msg = str()
    if error_msg:
        msg = ("[%s]\t" % debug_info()) + msg + error_msg + "\n"

    current_time = time.time()
    video_currentTime = self.get_currentTime()
    msg = (msg +
        """
        [%s]\tTimeout ERROR : %s.currentTime is reached at %f
        in %f sec(s) [Timeout: %f]
        """ % (debug_info(), self.media_player_page['js_media_object'],
                video_currentTime, current_time - start_time, timeout))

    assert False, msg

