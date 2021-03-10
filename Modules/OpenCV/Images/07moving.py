import cv2
import numpy

dragon = cv2.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\dragon.jpg')

height = dragon.shape[0]
width = dragon.shape[1]

M = numpy.float32([
        [1,0,300],#x
        [0,1,500],#y
    ])
dragon_translated = cv2.warpAffine(dragon,M,(width,height))
cv2.imshow('Dragon_Translated',dragon_translated)
cv2.waitKey(0)

M = cv2.getRotationMatrix2D((width/2,height/2),90,1)
dragon_rotated = cv2.warpAffine(dragon,M,(width,height))
cv2.imshow('Dragon_Rotated',dragon_rotated)
cv2.waitKey(0)