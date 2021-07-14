#!/usr/bin/env python
import easyocr
import cv2
import matplotlib.pyplot as plt
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32MultiArray

#publishing the topic "counter"
rospy.init_node('topic_publisher')
pub = rospy.Publisher('/counter', Int32MultiArray, queue_size=4)
foo = Int32MultiArray()
foo.data = [1, 2, 3 ,4]

#reads the text
reader = easyocr.Reader(['en'])
result = reader.readtext('code_bw.jpg')
print(result)
image = cv2.imread('code_bw.jpg')
res = reader.readtext('code_bw.jpg')
for (bbox, text, prob) in res:
  # unpack the bounding box
	(tl, tr, br, bl) = bbox
	tl = (int(tl[0]), int(tl[1]))
	tr = (int(tr[0]), int(tr[1]))
	br = (int(br[0]), int(br[1]))
	bl = (int(bl[0]), int(bl[1]))
	cv2.rectangle(image, tl, br, (0, 255, 0), 2)
	cv2.putText(image, text, (tl[0], tl[1] - 10),
	cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
	plt.rcParams['figure.figsize'] = (16,16)
	plt.imshow(image)

#keeps topic publishing
while not rospy.is_shutdown():
	foo.data =[1, 2, 3, 4]
	pub.publish(foo)
