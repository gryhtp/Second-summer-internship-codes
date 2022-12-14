import cv2
import numpy as np

img = cv2.imread("Resources/Schaftholzklasse-11.jpg")

imgHorizontal = np.hstack((img, img))
imgVertical = np.vstack((img, img))

cv2.imshow("Horizontal", imgHorizontal)
cv2.imshow("Vertical", imgVertical)

cv2.waitKey(0)