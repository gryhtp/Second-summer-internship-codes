import cv2
import numpy as np

blank = np.zeros((400,400), dtype='uint8')
rectangle = cv2.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv2.circle(blank.copy(), (200,200), 200, 255, -1)

cv2.imshow("Rectangle", rectangle)
cv2.imshow("Circle", circle)

#Bitwise and only show intersections
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("Bitwise and", bitwiseAnd)

#Bitwise or show both intersection and non intersected sides 
bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("Bitwise or", bitwiseOr)

#Bitwise xor only show non intersected sides
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("Bitwise xor", bitwiseXor)

#Bitwise not revert the colors
bitwiseNot = cv2.bitwise_not(rectangle, circle)
cv2.imshow("Bitwise not", bitwiseNot)

cv2.waitKey(0)