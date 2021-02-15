import cv2
import numpy as np
 
image = cv2.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\cat_resized.jpg')

gamma_corrected = np.array(255 *(image/255) ** 0.1, dtype='uint8')
cv2.imshow('0.1 Gamma', gamma_corrected)

gamma_corrected = np.array(255 *(image/255) ** 0.5, dtype='uint8')
cv2.imshow('0.5 Gamma', gamma_corrected)

gamma_corrected = np.array(255 *(image/255) ** 1.1, dtype='uint8')
cv2.imshow('1.1 Gamma', gamma_corrected)

gamma_corrected = np.array(255 *(image/255) ** 2.2, dtype='uint8')
cv2.imshow('2.2 Gamma', gamma_corrected)

cv2.waitKey(0)