import cv2
import numpy as np
import pyttsx3
import time

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
engine = pyttsx3.init()

cam = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX

names = ['None', 'shreyy']  # Add more if you train more users

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    for (x, y, w, h) in faces:
        id_, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        if confidence < 50:
            name = names[id_]
            label = f"{name} - {round(100 - confidence)}%"
            engine.say(f"Hello {name}")
            engine.runAndWait()
        else:
            label = "Unknown"
            engine.say("Intruder detected")
            engine.runAndWait()

        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, label, (x+5, y-5), font, 1, (255, 255, 255), 2)

    cv2.imshow('Recognizing...', img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
