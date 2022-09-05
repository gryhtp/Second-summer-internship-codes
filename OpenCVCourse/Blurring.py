import cv2
import numpy as np

img = cv2.imread("Resources/Schaftholzklasse-11.jpg")
cv2.imshow("Original", img)

#Averaging 
avarage = cv2.blur(img, (5,5))
cv2.imshow("Avarage", avarage)

#Method
gaussian = cv2.GaussianBlur(img, (5,5), 0)
cv2.imshow("Gaussian", gaussian)

#Median
median = cv2.medianBlur(img, 5)
cv2.imshow("Median", median)

#Bilateral
bilateral = cv2.bilateralFilter(img, 50, 100, 100)
cv2.imshow("Bilateral", bilateral)













cv2.waitKey(0)