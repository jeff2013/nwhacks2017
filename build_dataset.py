import cv2
import pickle
import face_recognizer

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

emotions = ["happy", "neutral", "sad"]
emotion_count = 0

try:
    with open("sample_count.txt", 'rb') as sampleFile:
        sample_count = pickle.load(sampleFile)
except FileNotFoundError:
    sample_count = 0

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (x,y,w,h) = face_recognizer.getLargestFaceCoords(gray)

    k = cv2.waitKey(1)

    if(w*h > 0):
        resizedGray = cv2.resize(gray[y:y+h, x:x+w], (350, 350))
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        if k %256 == 32:
            img_name = "dataset/subject_%d_%s.png" % (sample_count, emotions[emotion_count])
            cv2.imwrite(img_name, resizedGray)
            print("%s was written" % img_name)
            emotion_count += 1
            if(emotion_count >= len(emotions)):
                emotion_count = 0
                sample_count += 1

    cv2.imshow('Video', frame)

    if k%256 == 27:
        with open("sample_count.txt", 'wb') as sampleFile:
            pickle.dump(sample_count, sampleFile)
        break
cap.release()
cv2.destroyAllWindows()

