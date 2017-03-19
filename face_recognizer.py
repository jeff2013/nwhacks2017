import cv2
import classifier

LABEL_NEUTRAL = 0
LABEL_SAD = 1
LABEL_HAPPY = 2

faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
emotionClassifier = classifier.train()
emotions = ["sad", "happy"]

def getLargestFaceCoords(grayFrame):
    faces = faceCascade.detectMultiScale(grayFrame)
    (max_x, max_y, max_w, max_h) = (0,0,0,0)
    for(x,y,w,h) in faces:
        if w*h > max_w*max_h:
            (max_x, max_y, max_w, max_h) = (x,y,w,h)
    return (max_x, max_y, max_w, max_h)

def labelFaces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray)
    label = 0
    (x,y,w,h) = getLargestFaceCoords(gray)
    if(w*h == 0):
        return None, None, None
    # Extract the face
    resizedGray = cv2.resize(gray[y:y+h, x:x+w], (350, 350))
    # Draw a rectangle for the face
    label, conf = emotionClassifier.predict(resizedGray)
    # Do label confidence bounding
    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
    # Do confidence bounding
    labelStr = emotions[label]
    if(conf > 700):
        labelStr = "neutral"
    cv2.putText(
            frame, 
            "label %s, conf %d" % (labelStr, conf), 
            (x+w +5,y+h//2), 
            cv2.FONT_HERSHEY_PLAIN, 
            1, 
            (0,255,0))
    return label, conf, frame
