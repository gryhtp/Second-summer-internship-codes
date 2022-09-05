import cv2
import numpy as np

def empty(a):
    pass

img11 = cv2.imread("Resources/Schaftholzklasse-11.jpg")
kernel = np.ones((5,5), np.uint8)

img1 = cv2.imread("Resources/Schaftholzklasse-1.jpg")
img2 = cv2.imread("Resources/Schaftholzklasse-2.jpg")
img3 = cv2.imread("Resources/Schaftholzklasse-3.jpg")
img4 = cv2.imread("Resources/Schaftholzklasse-4.jpg")
img5 = cv2.imread("Resources/Schaftholzklasse-5.jpg")
img6 = cv2.imread("Resources/Schaftholzklasse-6.jpg")
img7 = cv2.imread("Resources/Schaftholzklasse-7.jpg")
img8 = cv2.imread("Resources/Schaftholzklasse-8.jpg")
img9 = cv2.imread("Resources/Schaftholzklasse-9.jpg")
img10 = cv2.imread("Resources/Schaftholzklasse-10-1024x367.jpg")

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", (640, 240))
cv2.createTrackbar("Canny Min", "TrackBars", 0, 500, empty)
cv2.createTrackbar("Canny Max", "TrackBars", 500, 500, empty)


imgGray = cv2.cvtColor(img11, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
edgeDetection11 = cv2.Canny(img11, 150, 200)
imgDialation = cv2.dilate(edgeDetection11, kernel, iterations=1 )
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

# edgeDetection1 = cv2.Canny(img1, 250, 250)
edgeDetection2 = cv2.Canny(img2, 300, 50)
# edgeDetection3 = cv2.Canny(img3, 250, 250)
# edgeDetection4 = cv2.Canny(img4, 250, 250)
# edgeDetection5 = cv2.Canny(img5, 250, 250)
# edgeDetection6 = cv2.Canny(img6, 250, 250)
# edgeDetection7 = cv2.Canny(img7, 250, 250)
# edgeDetection8 = cv2.Canny(img8, 250, 250)
# edgeDetection9 = cv2.Canny(img9, 250, 250)
# edgeDetection10 = cv2.Canny(img10, 250, 250)

CannyMin = cv2.getTrackbarPos("Canny Min", "TrackBars")
CannyMax = cv2.getTrackbarPos("Canny Max", "TrackBars")

lower = np.array([CannyMin])
upper = np.array([CannyMax])
mask = cv2.inRange(edgeDetection11, lower, upper)
imgResult = cv2.bitwise_and(img11, img11, mask=mask)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny 11 Image", edgeDetection11)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Erosion Image", imgEroded)
cv2.imshow("Result", imgResult)

# cv2.imshow("Canny 1 Image", edgeDetection1)
cv2.imshow("Canny 2 Image", edgeDetection2)
# cv2.imshow("Canny 3 Image", edgeDetection3)
# cv2.imshow("Canny 4 Image", edgeDetection4)
# cv2.imshow("Canny 5 Image", edgeDetection5)
# cv2.imshow("Canny 6 Image", edgeDetection6)
# cv2.imshow("Canny 7 Image", edgeDetection7)
# cv2.imshow("Canny 8 Image", edgeDetection8)
# cv2.imshow("Canny 9 Image", edgeDetection9)
# cv2.imshow("Canny 10 Image", edgeDetection10)

cv2.waitKey(0)