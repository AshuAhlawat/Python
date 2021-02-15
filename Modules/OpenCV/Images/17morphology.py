import cv2
import numpy

image = cv2.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\book.png')

image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

lower_blue = numpy.array([107,60,60])
upper_blue = numpy.array([130,255,255])

mask = cv2.inRange(image_rgb, lower_blue, upper_blue)
image_final = cv2.bitwise_and(image, image, mask=mask)

kernel = numpy.ones((5, 5), numpy.uint8) 

opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
opening = cv2.bitwise_and(image,image,mask=opening)
cv2.imshow('opening',opening)

gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
gradient = cv2.bitwise_and(image,image,mask=gradient)
cv2.imshow('gradient',gradient)

closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
closing = cv2.bitwise_and(image,image,mask=closing)
cv2.imshow('closing',closing)

cv2.waitKey(0)