#!/usr/bin/env python

import time
import easyocr
import cv2
import matplotlib.pyplot as plt
import os
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32MultiArray
from sensor_msgs.msg import Image
from std_msgs.msg import Int32
#----------------------------------------
#publishing the topic "logo_det"
rospy.init_node('text_detection')
pub = rospy.Publisher('/counter', Int32MultiArray, queue_size=10)
foo = Int32MultiArray()
res = ''
#----------------------------------------
#reads the text
#readtext(data):
reader = easyocr.Reader(['en'])
result = reader.readtext('snapshot4.jpg')
print(result)
image = cv2.imread('snapshot4.jpg')
cv2.imshow("Original", image)
res = reader.readtext('snapshot4.jpg')
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
	cv2.waitKey(3000)
	final_time = time.time()
#----------------------------------------  
#prints that its done

rospy.loginfo('Published')

#----------------------------------------  

#keeps topic publishing
while not rospy.is_shutdown():
#	image_sub = rospy.Subscriber("/camera/rgb/image_raw", Image, readtext,queue_size=1)
	if res == []:
		foo.data = [2]
	else:
		foo.data = [3]
#		print(res)
	pub.publish(foo)

#----------------------------------------
