import numpy as np
import cv2
import classifier
import ocr

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

# Load all of our training data
emotionClassifier = classifier.train()

emotions = ["happy", "neutral", "sad"]


while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray)
    for(x,y,w,h) in faces:
        # Extract the face
        resizedGray = cv2.resize(gray[y:y+h, x:x+w], (350, 350))
        # Draw a rectangle for the face
        label, conf = emotionClassifier.predict(resizedGray)
        print("Label %s, Conf %.2f" % (emotions[label], conf))
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(
                frame, 
                "label %s, conf %d" % (emotions[label], conf), 
                (x+w +5,y+h//2), 
                cv2.FONT_HERSHEY_PLAIN, 
                1, 
                (0,255,0))
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
