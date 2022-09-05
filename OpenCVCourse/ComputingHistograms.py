import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Resources/Schaftholzklasse-11.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", imgGray)
blank = np.zeros(img.shape[:2], dtype='uint8')

circle = cv2.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv2.imshow("Circle", circle)

mask = cv2.bitwise_and(img, img, mask=circle)
cv2.imshow("Masked", mask)

# #Gray scale histogram
# grayHist = cv2.calcHist([imgGray],[0], mask, [256], [0,256])
# plt.figure()
# plt.title("Gray scale histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# plt.plot(grayHist)
# plt.xlim([0,256])
# plt.show()



#Color histogram
colors = ('b', 'g', 'r')
plt.figure()
plt.title("Gray scale histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
for i,col in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()






cv2.waitKey(0)