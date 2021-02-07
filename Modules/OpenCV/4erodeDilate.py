import cv2
import numpy
dragon = cv2.imread("C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\dragon_inverted.jpg")

cv2.imshow('dragon', dragon)
cv2.waitKey(0)

kernel = numpy.ones((3,3),numpy.uint8)
dragon_eroded_3 = cv2.erode(dragon,kernel)
cv2.imshow('dragon_eroded',dragon_eroded_3)
cv2.waitKey(0)

kernel = numpy.ones((5,5),numpy.uint8)
dragon_eroded_5 = cv2.erode(dragon,kernel)
cv2.imshow('dragon_eroded',dragon_eroded_5)
cv2.waitKey(0)

kernel = numpy.ones((7,7),numpy.uint8)
dragon_eroded_7 = cv2.erode(dragon,kernel)
cv2.imshow('dragon_eroded',dragon_eroded_7)
cv2.waitKey(0)

# cv2.imwrite("C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\dragon_eroded.jpg",dragon_eroded_75)
kernel = numpy.ones((3,3),numpy.uint8)
dragon_eroded_3 = cv2.dilate(dragon,kernel)
cv2.imshow('dragon_eroded',dragon_eroded_3)
cv2.waitKey(0)

kernel = numpy.ones((5,5),numpy.uint8)
dragon_eroded_5 = cv2.dilate(dragon,kernel)
cv2.imshow('dragon_eroded',dragon_eroded_5)
cv2.waitKey(0)

kernel = numpy.ones((9,9),numpy.uint8)
dragon_eroded_7 = cv2.dilate(dragon,kernel)
cv2.imshow('dragon_eroded',dragon_eroded_7)
cv2.waitKey(0)
