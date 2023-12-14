import time
import pyttsx3
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
from cvzone.ClassificationModule import Classifier

def show():
    cap = cv2.VideoCapture(0)  # Change the index to access different cameras (0, 1, 2, etc.)
    if not cap.isOpened():
        print("Failed to open the camera.")
        return

    detector = HandDetector(maxHands=1)
    classifier = Classifier("model/keras_model.h5", "model/labels.txt")
    offset = 20
    imgSize = 300
    assistant = pyttsx3.init()
    labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
              "W", "X", "Y"]

    while True:
        ret, img = cap.read()
        if not ret or img is None:
            print("Failed to retrieve frame from the camera.")
            break

        outputImg = img.copy()
        hands, _ = detector.findHands(img)  # No need to modify the original 'img'

        if hands:
            hand = hands[0]
            x, y, w, h = hand['bbox']
            imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

            if h > w:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                wGap = math.ceil((imgSize - wCal) / 2)
                imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
                imgWhite[0:imgResize.shape[0], wGap:wCal + wGap] = imgResize
            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                hGap = math.ceil((imgSize - hCal) / 2)
                imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
                imgWhite[hGap:hCal + hGap, 0:imgResize.shape[1]] = imgResize

            prediction, index = classifier.getPrediction(imgWhite)
            cv2.putText(outputImg, labels[index], (x, y - 20), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 0), 2)
            assistant.say(labels[index])
            assistant.runAndWait()

        cv2.imshow("Image", outputImg)
        if cv2.waitKey(33) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

show()
