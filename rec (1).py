import cv2
import numpy as np
import pyttsx3
#engine = pyttsx3.init()
import serial

ser=serial.Serial("COM3",9600)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);


cam = cv2.VideoCapture(0)
# recognizer = cv2.face.LBPHFaceRecognizer_create()
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, im =cam.read()
  #  im=cv2.imread("Ammu.jpg")
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        print(Id,conf)
        if(conf<65):
            if(Id==1):
                Id="sriram"
            elif(Id==2):
                Id="vyshnavi"
  
        else:
            Id="Unknown"
            ser.write(b"i#")
        cv2.putText(im, str(Id), (x,y-40), font, 1, (255,255,255), 3)
        #engine.say(Id)
    #engine.runAndWait()
    im=cv2.resize(im,(600,400))
    
    cv2.imshow('face',im) 
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
