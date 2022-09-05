import cv2

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

img1Gr = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2Gr = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
img3Gr = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
img4Gr = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)
img5Gr = cv2.cvtColor(img5, cv2.COLOR_BGR2GRAY)
img6Gr = cv2.cvtColor(img6, cv2.COLOR_BGR2GRAY)
img7Gr = cv2.cvtColor(img7, cv2.COLOR_BGR2GRAY)
img8Gr = cv2.cvtColor(img8, cv2.COLOR_BGR2GRAY)
img9Gr = cv2.cvtColor(img9, cv2.COLOR_BGR2GRAY)
img10Gr = cv2.cvtColor(img10, cv2.COLOR_BGR2GRAY)

threshold1, thresh1 = cv2.threshold(img1Gr, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresholded 1", thresh1)

threshold2, thresh2 = cv2.threshold(img2Gr, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresholded 2", thresh2)

threshold3, thresh3 = cv2.threshold(img3Gr, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresholded 3", thresh3)

threshold4, thresh4 = cv2.threshold(img4Gr, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresholded 4", thresh4)

threshold5, thresh5 = cv2.threshold(img5Gr, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresholded 5", thresh5)

threshold6, thresh6 = cv2.threshold(img6Gr, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresholded 6", thresh6)

threshold7, thresh7 = cv2.threshold(img7Gr, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresholded 7", thresh7)

threshold8, thresh8 = cv2.threshold(img8Gr, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresholded 8", thresh8)

threshold9, thresh9 = cv2.threshold(img9Gr, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresholded 9", thresh9)

threshold10, thresh10 = cv2.threshold(img10Gr, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresholded 10", thresh10)

img = cv2.imread("Resources/Schaftholzklasse-11.jpg")
cv2.imshow("Original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

#Simple thresholding
threshold, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresholded", thresh)

thresholdInversed, threshInversed = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Thresholded Inverse", threshInversed)

#Adaptive thresholding
adaptiveThresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 5)
cv2.imshow("Adaptive Thresholding", adaptiveThresh)

cv2.waitKey(0)