import numpy as np
import cv2
import face_recognizer
import serial
import ocr
import sys

if len(sys.argv) != 2:
    print("I need a device file path :(")
    sys.exit()
port = sys.argv[1]

ser = serial.Serial(port, 9600)

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
carding = False

# Load all of our training data

while(True):
    ret, frame = cap.read()
    k = cv2.waitKey(1)
    if carding:
        cv2.imshow('Video', ocr.threshold(frame))
        if k %256 == 32:
            ocr.getText(frame)
    else:
        label, frame = face_recognizer.labelFaces(frame)
        if label != 0:
            ser.write(b"%d" % label)
        cv2.imshow('Video', frame)
    if k & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

