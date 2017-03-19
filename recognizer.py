import cv2

faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

def getFaceCoords(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray)

def getLargestFaceCoords(frame, faceCascade)

    
