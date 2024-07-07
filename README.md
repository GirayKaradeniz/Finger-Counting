# Finger-Counting
This project uses OpenCV and Mediapipe to count the number of fingers held up in front of a camera. The code captures video from the default camera, processes each frame to detect hands, and counts the number of extended fingers. It can distinguish between right and left hands and displays the finger count on the video feed in real-time.

# Features

+ Accurate counting of extended fingers.
+ Differentiation between right and left hands.
+ Display of the finger count on the video feed.
+ Real-time hand detection using Mediapipe.

# Dependencies

+ OpenCV
+ Mediapipe

# Code Explanation

The script begins by initializing the video capture and setting the resolution. Mediapipe is used to detect hand landmarks in the video frames. The script identifies whether the detected hand is the right or left hand and then determines the number of extended fingers based on the hand type. The count of extended fingers is displayed on the video feed.

# Contributing

Feel free to submit issues and enhancement requests.

