import cv2
import numpy as np

img = cv2.imread("Resources/Schaftholzklasse-11.jpg")

blank = np.zeros(img.shape, dtype='uint8')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(imgGray,(5,5), cv2.BORDER_DEFAULT)
canny = cv2.Canny(img, 200, 200)
ret, thresh = cv2.threshold(imgGray, 120, 255, cv2.THRESH_BINARY)

contours, hierarchies = cv2.findContours(thresh,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

cv2.drawContours(blank, contours, -1, (0,0,255), 1)

cv2.imshow("Gray image", imgGray)
cv2.imshow("Canny image", canny)
cv2.imshow("Blurred", blur)
cv2.imshow("Thresh", thresh)
cv2.imshow("Blank", blank)

cv2.waitKey(0)