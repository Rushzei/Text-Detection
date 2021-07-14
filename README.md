# Text-Detection
#how to set it up
Requires Python3 and pip
# install easyocr
1. pip install easyocr
# install opencv
2. sudo apt update -y
3. sudo apt install python3-opencv -y
 # check to make sure it installed
4. python3 -c "import cv2; print(cv2.__version__)"
 # install rospy
5. sudo apt-get install -y python-rospy
 # install matplotlib
6. python -m pip install -U matplotlib -y

 # Notes
----------
This uses a ros publisher and subscriber.
If you don't use ros comment it our.
