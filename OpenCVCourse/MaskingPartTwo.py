import cv2
import numpy as np



img = cv2.imread("Resources/Schaftholzklasse-11.jpg")

blank = np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow("Blank image", blank)

mask = cv2.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv2.imshow("Mask", mask)

maskedImage = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Masked Image", maskedImage)



















cv2.waitKey(0)