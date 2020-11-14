import time
from tests.libmedia.media_harness import MediaTest


class video_seek_test(MediaTest):
    def __init__(self, test):
        super(video_seek_test, self).__init__(test)
        self.log("[MediaTest] Video Seek Test")
        self.time_to_check = {'seek': 5.1, 'seek_during_playback': 20.1}
        self.video = self.media_player_page['js_media_object']

    def do_test(self):
        # App Launch and load a media file
        self.prepare()

        # Seek the video to 5 seconds
        self.seek_to(self.time_to_check['seek'])

        # Wait until currentTime is changed after seeking
        self.uawait_until(condition="%s.currentTime == %f"
                        % (self.video,
                            self.time_to_check['seek']),
                        message="""
                        [ %s.currentTime is not changed to %f. ]
                        """ % (self.video,
                                self.time_to_check['seek']),
                        timeout=5)

        # Check seek result of the video.
        time.sleep(5)
        img = self.get_screenshot("after_seek.png")
        after_seek_screen_num = self.get_number_array_from_image(img)[0]

        assert after_seek_screen_num == int(self.time_to_check['seek']), (
            """
            Video seek failure.
            [ The number video displays is correct after seek. ]
            after_seek_screen_num : %d
            """ % after_seek_screen_num)

        # Play video
        self.play()

        # Wait until currentTime is increased after playing
        self.uawait_until(condition="%s.currentTime >= %f"
                        % (self.video,
                            self.time_to_check['seek']+1.0),
                        message="""
                        [ %s.currentTime is not increased after %f. ]
                        """ % (self.video,
                                self.time_to_check['seek']+1.0),
                        timeout=5)

        # Check seek during playback
        self.seek_to(self.time_to_check['seek_during_playback'])

        # Wait until currentTime is increased after playing
        self.uawait_until(condition="%s.currentTime >= %f"
                        % (self.video,
                            self.time_to_check['seek_during_playback']+1.0),
                        message="""
                        [ %s.currentTime is not increased after %f. ]
                        """ % (self.video,
                                self.time_to_check['seek_during_playback']
                                + 1.0),
                        timeout=5)

        # Check seek during playback result of the video.
        img = self.get_screenshot("after_seek_during_playback.png")
        after_seek_during_playback_screen_num = (
            self.get_number_array_from_image(img)[0])

        assert (after_seek_during_playback_screen_num >=
                int(self.time_to_check['seek_during_playback'])-1), (
            """76             Video seek failure.
            [ The number video displays is correct after seek. ]
            after_seek_screen_num : %d
            """ % after_seek_during_playback_screen_num)