import cv2
import numpy as np

img = cv2.imread("Resources/Schaftholzklasse-11.jpg")
cv2.imshow("Classic", img)

b,g,r = cv2.split(img)
cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)

merged = cv2.merge([b,g,r])
cv2.imshow("Merged", merged)

blank = np.zeros(img.shape[:2],dtype='uint8')
blue = cv2.merge([b,blank,blank])
green = cv2.merge([blank,g,blank])
red = cv2.merge([blank,blank,r])
cv2.imshow("Blue image", blue)
cv2.imshow("Red image", red)
cv2.imshow("Green image", green)

cv2.waitKey(0)