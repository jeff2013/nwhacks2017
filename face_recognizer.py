import cv2

faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

def getLargestFaceCoords(grayFrame):
    faces = faceCascade.detectMultiScale(grayFrame)
    (max_x, max_y, max_w, max_h) = (0,0,0,0)
    for(x,y,w,h) in faces:
        if w*h > max_w*max_h:
            (max_x, max_y, max_w, max_h) = (x,y,w,h)
    return (max_x, max_y, max_w, max_h)
