import cv2 as cv
import numpy as np

def changeColorValue(x):
    pass

blank = np.zeros((500, 600, 3), dtype='uint8')
cv.namedWindow('Pic')

cv.createTrackbar('Red','Pic', 0, 255, changeColorValue)
cv.createTrackbar('Green','Pic', 0, 255, changeColorValue)
cv.createTrackbar('Blue','Pic', 0, 255, changeColorValue)

while True:
     r = cv.getTrackbarPos('Red', 'Pic')
     g = cv.getTrackbarPos('Green', 'Pic')
     b = cv.getTrackbarPos('Blue', 'Pic')
     blank[:] = b, g, r
     cv.imshow('Pic', blank)
     if cv.waitKey(20) & 0xFF == ord('d'):
         break