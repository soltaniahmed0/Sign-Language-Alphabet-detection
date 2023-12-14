import time

import cv2
import mediapipe as mp
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc

import pyttsx3
from cvzone.ClassificationModule import Classifier
def show():
    webcam = cv2.VideoCapture(0)
    mp_drawing = mp.solutions.drawing_utils
    mp_holistic = mp.solutions.holistic
    q = 0
    lables = ["Thanks", "Yes", "help", "father", "hello"]
    video = VideoWriter("v1.avi", VideoWriter_fourcc(*'MP42'), 25.0, (640, 480))
    # Initiate holistic model
    classifier = Classifier("model/keras_modelv.h5", "model/labelsv.txt")
    assistante = pyttsx3.init()
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:

        while True:

            ret, frame = webcam.read()
            # Recolor Feed
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Make Detections
            results = holistic.process(image)

            # print(results.face_landmarks)
            # print(results.pose_landmarks)

            # Recolor image back to BGR for rendering
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Right hand
            mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

            # Left Hand
            mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

            # Pose Detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

            Key = cv2.waitKey(1)
            prediction, index = classifier.getPrediction(image)
            # cv2.putText(image, lables[index], (20, 100 - 20), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 0), 2)

            cv2.imshow("Image", image)
            assistante.say(lables[index])
            assistante.runAndWait()
            time.sleep(1)
            if cv2.waitKey(33) == ord('f'):
                break
        cv2.destroyAllWindows()
    webcam.release()

show()