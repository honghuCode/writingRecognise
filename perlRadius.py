#coding:utf-8

import numpy as np
import cv2
import imutils
import math
im = cv2.imread('6.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

#print cnts
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
#image, contours, hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
          #cv2.drawContours(thresh, [c], -1, (255, 255, 0), 2)
for c in cnts:
	 M = cv2.moments(c)
	
	 cv2.drawContours(im, [c], -1, (255, 255, 0), 2)
         cX = int(M["m10"] / M["m00"])
	 cY = int(M["m01"] / M["m00"])
	 u11 = M["m11"] - M["m01"]*cX
	 u02 = M["m02"] - M["m01"]*cX
	 u20 = M["m20"] - M["m10"]*cX
         area=cv2.contourArea(c)
         cz = (2 * (u20 + u02 + math.sqrt( (u20 - u02) ** 2) + 4 * (u11 **2)  )  /  M["m00"])
	 #print u11,u02,u20,cz,cX, cY,area
	 #print M
	 area = cv2.contourArea(c)  
         equi_diameter = np.sqrt(4*area/np.pi)
	 r = equi_diameter / 2
	 print equi_diameter / 2,M["m00"],np.pi *( (equi_diameter / 2) ** 2)
 	 #cv2.circle(im, (cX, cY), int(r), (0, 255, 0), -1)
	 cv2.imshow("Image",im)
	 cv2.waitKey(0)
cv2.destroyAllWindows()



