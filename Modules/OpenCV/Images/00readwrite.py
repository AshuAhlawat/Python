import cv2 as cv

img = cv.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\cat.jpg')
cv.imshow('Cat',img)

cv.waitKey(0)

img2 = cv.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\cat.jpg',0)
cv.imshow('Cat',img2)

cv.waitKey(0)

import os
os.chdir('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV')
cv.imwrite('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\kitten.jpg',img2)
