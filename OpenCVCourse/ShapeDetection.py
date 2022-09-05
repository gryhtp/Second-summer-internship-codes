import cv2
import numpy as np

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 400:
            cv2.drawContours(imgCountour, cnt, -1, (255, 0, 0), 2)
            par = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * par, True)
            objCor = len(approx)
            x, y, width, height = cv2.boundingRect(approx)
            
            if objCor == 3: 
                objectType = "Triangle"

            elif objCor == 4:
                aspRatio = width / float(height)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            else:
                objectType = "None"

            cv2.rectangle(imgCountour, (x, y), (x+width, y+height), (0, 255, 0), 2)
            cv2.putText(imgCountour, objectType, (x+width//2-10, y+height//2-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 2)

img = cv2.imread("Resources/cards.jpg")
imgCountour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)

getContours(imgCanny)

cv2.imshow("Original", img)
cv2.imshow("Gray", imgGray)
cv2.imshow("Blurred", imgBlur)
cv2.imshow("Canny", imgCanny)
cv2.imshow("Img Countour", imgCountour)



cv2.waitKey(0)