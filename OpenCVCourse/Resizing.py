import cv2

img = cv2.imread("Resources/Schaftholzklasse-11.jpg")
print(img.shape)

imgResize = cv2.resize(img, (800, 276))

imgCropped = img[0:200, 200:500]

cv2.imshow("Resized", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)