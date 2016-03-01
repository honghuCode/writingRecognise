import cv2

image = cv2.imread("6.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 35, 125)

cv2.imshow("thresh",edged)
cv2.waitKey(0)

# find the contours in the edged image and keep the largest one;
# we'll assume that this is our piece of paper in the image
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
c = max(cnts, key = cv2.contourArea)

print  cv2.minAreaRect(c)[1][0]
# compute the bounding box of the of the paper region and return it
#return cv2.minAreaRect(c)
