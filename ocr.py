from pytesseract import image_to_string
from PIL import Image
import numpy as np
import cv2 

def getText(frame):
    thresh = threshold(frame)
    print(image_to_string(Image.fromarray(thresh)))
    #channels = cv2.text.computeNMChannels(frame)
    #out = []
    #for channel in channels:
    #    ecr1 = cv2.text.loadClassifierNM1('./trained_classifierNM1.xml')
    #    er1 = cv2.text.createERFilterNM1(
    #            ecr1,
    #            minArea = 0.00025,
    #            maxArea = 0.13,
    #            minProbability = 0.4,
    #            nonMaxSuppression = True,
    #            minProbabilityDiff = 0.1)
    #    ecr2 = cv2.text.loadClassifierNM2('./trained_classifierNM2.xml')
    #    er2 = cv2.text.createERFilterNM1(
    #            ecr2,
    #            minProbability = 0.3)
    #    regions = cv2.text.detectRegions(channel, er1, er2)
    #    out.append(cv2.text.erGrouping(frame, channel, [r.tolist() for r in regions]))
    #return out
def threshold(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # create black and white image
    #thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
    return gray


#print("Loading Image...")
#i = np.array(Image.open('Img.png'))
#print("Image Loaded")
#cv2.imshow('Video', threshold(i))
#k = cv2.waitKey(0)
#getText(i)
