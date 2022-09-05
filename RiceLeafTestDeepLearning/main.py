import cv2
import cvzone
from cvzone.ClassificationModule import Classifier

cap = cv2.VideoCapture(0)
myClassifier = Classifier('MyModel/keras_model.h5', 'MyModel/labels.txt')

while True:
    _, img = cap.read()
    predictions, index = myClassifier.getPrediction(img)
    print(predictions)

    cv2.imshow("Image", img)
    cv2.waitKey(1)