from tests.libmedia.media_harness import MediaTest
 
 
 class video_loop_test(MediaTest):
     def __init__(self, test):
         super(video_loop_test, self).__init__(test)
         self.log("[MediaTest] Video Loop Test")
         self.time_to_check = {'play': 5.1}
         self.video = self.media_player_page['js_media_object']
 
     def do_test(self):
         # App Launch and Load a media file
         self.prepare()
 
         # Play the video and Check if it is played.
         self.driver.execute_script("%s.loop = true" % self.video)
         self.play()                         # Play
         self.uawait_until("%s.currentTime > %f"
                           % (self.video, self.time_to_check['play']),
                           """Video playback failure.
         [ Video.currentTime is not increased after playback is tried. ]
         """, 10)
 
         img = self.get_screenshot("play+5sec.png")
         playback_screen_num = self.get_number_array_from_image(img)[0]
 
         assert playback_screen_num >= int(self.time_to_check['play']), (
             """Video playback failure
             [ The number video displays is not correct. ]""")
 
         # Check if loop playback is performed.
         # Check if playback time reaches at its duration time - 5.0
         time_5secs_before_the_end = (
             self.driver.execute_script("return %s.duration;" % self.video)
             - 5.0)
 
         self.uawait_until("%s.currentTime >= %f"
                           % (self.video, time_5secs_before_the_end),
                           """Video playback failure.
                           [ Video playback doesn't reach at %f. ]""" %
                           time_5secs_before_the_end)
 
         img = self.get_screenshot("almost_end_of_playback.png")
         almost_end_of_playback_screen_num = (
             int(self.get_number_array_from_image(img)[0]))
 
         # Wait until playback time reaches at TIME_TO_CHECK_PLAYBACK
         self.log("almost_end_of_playback_screen_num : %f " %
                  almost_end_of_playback_screen_num)
 
         self.uawait_until("%s.currentTime < %f && %s.currentTime > %f "
                           % (self.video,
                              time_5secs_before_the_end,
                              self.video, self.time_to_check['play']),
                           """Video looping playback failure.
         [ Video looping playback is not performed. ]
         """, 20)
 
         # Check loop playback displays video content correctly
         self.pause()
 
         img = self.get_screenshot("loop_playback_at_%f.png" %
                                   self.get_currentTime())
 
         del self.reference_video_strings[4]                  # remove "00"
         self.compare_image_with_string_array(img, self.reference_video_strings,
                                              """Video rendering failure
         [ Loop playback doesn't display the video content correctly. ]""")
 
         loop_playback_screen_num = self.get_number_array_from_image(img)[0]
 
         self.log("loop_playback_screen_num: %f " % loop_playback_screen_num)
         assert (loop_playback_screen_num < almost_end_of_playback_screen_num
                 and (loop_playback_screen_num >=
                      int(self.time_to_check['play']))
                 and loop_playback_screen_num <= int(self.time_to_check['play'])
                 ), (
             """
             Video loop playback failure.
             [ Video loop playback is not performed correctly. ]
             almost_end_of_playback_screen_num : %d
             loop_playback_screen_num : %d
             """ % (almost_end_of_playback_screen_num, loop_playback_screen_num)
         )
 