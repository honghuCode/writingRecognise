import numpy as np
import argparse
import cv2
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
 
# load the image
image = cv2.imread(args["image"])

lower_blue=np.array([110,50,50])
upper_blue=np.array([130,255,255])
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lower_blue, upper_blue)
output = cv2.bitwise_and(image, image, mask = mask)
 
	# show the images
	#cv2.imshow("images", np.hstack([image, output]))
cv2.imshow("images", image)
cv2.imshow("output", output)
cv2.waitKey(0)

#

# define the list of boundaries
'''
boundaries = [
	([17, 15, 100], [50, 56, 200]),
	([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 174, 250]),
	([103, 86, 65], [145, 133, 128])
]

for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
 
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
 
	# show the images
	#cv2.imshow("images", np.hstack([image, output]))
	cv2.imshow("images", output)
	cv2.waitKey(0)
'''


