from pytesseract import *
from PIL import Image
import numpy as np
import cv2 

def getText(frame, rects):
    for r in range(0, np.shape(rects)[0]):
        rect = rects[r]
        img = frame[rect[1]:rect[1] + rect[3], rect[0]:rect[0] + rect[2]]
        fi = adaptiveThreshold(img)
        print(image_to_string(Image.fromarray(fi)))

def getTextAreas(frame):
    channels = cv2.text.computeNMChannels(frame)
    out = []
    for channel in channels:
        ecr1 = cv2.text.loadClassifierNM1('./trained_classifierNM1.xml')
        er1 = cv2.text.createERFilterNM1(
                ecr1,
                minArea = 0.00025,
                maxArea = 0.13,
                minProbability = 0.4,
                nonMaxSuppression = True,
                minProbabilityDiff = 0.1) 
        ecr2 = cv2.text.loadClassifierNM2('./trained_classifierNM2.xml')
        er2 = cv2.text.createERFilterNM1(
                ecr2,
                minProbability = 0.3)
        regions = cv2.text.detectRegions(channel, er1, er2)
        rects = cv2.text.erGrouping(frame,channel,[r.tolist() for r in regions])
        for r in range(0, np.shape(rects)[0]):
            rect = rects[0]
            cv2.rectangle((rect[0], rect[1]), ())
        getText(frame, rects)
    return frame, []

def adaptiveThreshold(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 2)
    # initial global thresh
    # create black and white image
    #blur = cv2.GaussianBlur(gray,(5,5),0)
    #r, thresh = cv2.threshold(blur, 30, 255, cv2.THRESH_BINARY)
    return thresh

def thresholdOtsu(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #blur = cv2.GaussianBlur(gray,(5,5),0)
    ret3,th3 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return th3

def binaryThreshold(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret1,th1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    return th1



cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    k = cv2.waitKey(1)
    i1 = adaptiveThreshold(frame)
    cv2.imshow('otsu', i1)
    if k %256 == 32:
        f, r = getTextAreas(frame)
        break

