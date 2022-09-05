import cv2
import numpy as np

def empty(a):
    pass

img = cv2.imread("Resources/Schaftholzklasse-11.jpg")
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", (640, 240))
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 21, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 132, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 197, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 127, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)


while True:
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    HMin = cv2.getTrackbarPos("Hue Min", "TrackBars")
    HMax = cv2.getTrackbarPos("Hue Max", "TrackBars")
    SMin = cv2.getTrackbarPos("Sat Min", "TrackBars")
    SMax = cv2.getTrackbarPos("Sat Max", "TrackBars")
    VMin = cv2.getTrackbarPos("Val Min", "TrackBars")
    VMax = cv2.getTrackbarPos("Val Max", "TrackBars")
    lower = np.array([HMin, SMin, VMin])
    upper = np.array([HMax, SMax, VMax])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)


    cv2.imshow("Normal", img)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Results", imgResult)

    cv2.waitKey(1)


