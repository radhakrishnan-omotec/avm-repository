################# ORIGINAL CODE ########################

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/sudoku.png',0)
img = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img,127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,5,2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,5,2)

while True:
    cv2.imshow('original', img)
    cv2.imshow('notmal threshold', th1)
    cv2.imshow('adaptive threshold mean', th2)
    cv2.imshow('adaptive threshold Gaussian', th2)            
    
    if cv2.waitKey(50) == ord('q'):
        break
        
cv2.destroyAllWindows()


################# ORIGINAL CODE ########################
""" USE THE BELOW FUNCTIONS

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst = cv2.calcBackProject([hsv], [0, 1], hist, [0, 180, 0, 256], 1)

    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (31, 31))
    cv2.filter2D(dst, -1, disc, dst)

    ret, thresh = cv2.threshold(dst, 150, 255, cv2.THRESH_BINARY)

    thresh = cv2.merge((thresh, thresh, thresh))

    return cv2.bitwise_and(frame, thresh) """