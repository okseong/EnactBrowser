from tests.libmedia.media_harness import MediaTest
 
 
 class video_play_test(MediaTest):
     def __init__(self, test):
         super(video_play_test, self).__init__(test)
         self.log("[MediaTest] Video Play Test")
         self.video = self.media_player_page['js_media_object']
 
     def is_video_ended(self):
         return self.driver.execute_script("return %s.ended;" % self.video)
 
     def do_test(self):
         # App launch and load a media file
         self.prepare()
         self.log(" The first # video displays is 00."
                  " The initial video frame displays correctly.")
 
         self.play()                            # Play
 
         # Capture screen until video playback reaches the end
         captured_screens_image = []
         video_currentTime_captured = 0.0
         duration = self.get_duration()
 
         while self.is_video_ended() is False:
 
             capture_time = video_currentTime_captured + 2.0
             if capture_time >= duration:
                 break
             self.uawait_until(condition="%s.currentTime >= %f"
                               % (self.video, capture_time),
                               message="""
                               [ %s.currentTime is not increased after %f. ]
                               """ % (self.video, video_currentTime_captured),
                               timeout=5)
 
             video_currentTime_captured = self.get_currentTime()
             image = self.get_screenshot()
             captured_screens_image.append(image)
             self.log("Capture Screen at %f" % video_currentTime_captured)
 
         # Save captured images
         index = 0
         for image in captured_screens_image:
             filename = "playback_%d.png" % index
             image.save(self.out(filename))
             index += 1
 
         self.log("Playback End")
 
         # Change the number string from "00" to "30"
         self.reference_video_strings[4] = str(self.last_number_of_video)
 
         # Check end of video
         image = self.get_screenshot()
         image.save(self.out("end.png"))
         self.compare_image_with_string_array(
             image, self.reference_video_strings)
         self.log("The last # video displays is %s.\n"
                  % self.reference_video_strings[4] +
                  "The last video frame displays correctly.")
 
         # Erase the number string, "00"
         del self.reference_video_strings[4]
 
         last_number = 0
         current_number = 0
         self.log("Checking Captured screens")
 
         for image in captured_screens_image:
             # Check if Video rendering results is correct by examining
             # the captured screenshot images
             current_number = self.get_number_array_from_image(image)[0]
 
             is_number_increased = current_number > last_number
             is_ended = (last_number == current_number and
                         last_number == self.last_number_of_video)
 
             self.log("Current # : %d , Last # : %d - %s.  ".rstrip("\n")
                      % (current_number, last_number,
                         "Ok" if is_number_increased else "Error"), False)
             self.compare_image_with_string_array(
                 image, self.reference_video_strings)
             assert is_number_increased or is_ended, (
                 """Video Playback is not progressed.
                 [ The number of video content was not increased. ]
                 current_number : %d , last_number : %d""" % (current_number,
                                                              last_number))
             last_number = current_number
             