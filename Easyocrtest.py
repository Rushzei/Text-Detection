#!/usr/bin/env python

import easyocr
import cv2
import matplotlib.pyplot as plt
import os
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32MultiArray
from sensor_msgs.msg import Image

#----------------------------------------
#publishing the topic "logo_det"
rospy.init_node('topic_publisher')
pub = rospy.Publisher('/logo_det', Int32MultiArray, queue_size=4)
foo = Int32MultiArray()
foo.data = [1, 2, 3 ,4]
#----------------------------------------
#reads the text
#def readtext(data):
reader = easyocr.Reader(['en'])
result = reader.readtext('snapshot1.jpg')
print(result)
image = cv2.imread('snapshot1.jpg')
cv2.imshow("Original", image)
res = reader.readtext('snapshot1.jpg')
for (bbox, text, prob) in res:
# unpacks the bounding box(basically the points of the box)
        (tl, tr, br, bl) = bbox
        tl = (int(tl[0]), int(tl[1]))
        tr = (int(tr[0]), int(tr[1]))
        br = (int(br[0]), int(br[1]))
        bl = (int(bl[0]), int(bl[1]))
        newimg = cv2.rectangle(image, tl, br, (0, 255, 0), 2)
        #cv2.putText(image, text, (tl[0], tl[1] - 10),
        #cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        plt.rcParams['figure.figsize'] = (16,16)
        #plt.imshow(image)
        #cv2.circle(image, tl, radius = 0, color =(255, 0, 0), thickness=-1)
        cv2.imshow("stuff", newimg)
        cv2.waitKey(0)
#----------------------------------------  
#prints that its done

rospy.loginfo('Published')

#image_sub = rospy.Subscriber("/camera/rgb/image_raw", Image, readtext,queue_size=1)

#----------------------------------------  

#keeps topic publishing

while not rospy.is_shutdown():
        foo.data =[1, 2, 3, 4]
        pub.publish(foo)

#----------------------------------------  
#videoReq = requests.get("https://www.example.com/myimage.mp4")
#videoBytes = np.asarray(bytearray(data), dtype=np.uint8)
#loadedVideo = cv2.videodecapture(image, cv2.IMREAD_COLOR)
