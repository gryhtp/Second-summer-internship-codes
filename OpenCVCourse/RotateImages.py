import cv2
import numpy as np

def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions= (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dimensions)
# -x left // -y up // x right // y down

def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv2.warpAffine(img, rotMat, dimensions)

img = cv2.imread("Resources/cards.jpg")

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
translated = translate(img, 100, 100)
rotated = rotate(img,45)

flipped = cv2.flip(img, 1)

cv2.imshow("Flipped", flipped)
cv2.imshow("Translated", translated)
cv2.imshow("Gray", grayImg)
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)