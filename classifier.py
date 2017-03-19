import numpy as np
import cv2
import glob

def train():
    emotions = ["sad", "happy"]
    emotionClassifier = cv2.face.createFisherFaceRecognizer()
    data = []
    labels = []
    for e in emotions:
        files = glob.glob("dataset/*_%s.png" % e)
        for f in files:
            image = cv2.imread(f)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            resizedGray = cv2.resize(gray, (350, 350))
            data.append(resizedGray)
            labels.append(emotions.index(e))
    emotionClassifier.train(data, np.asarray(labels))
    return emotionClassifier

