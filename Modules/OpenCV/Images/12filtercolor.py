import cv2
import numpy

image_o = cv2.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\cat_resized.jpg')

lower_red = numpy.array([30, 30, 30])
upper_red = numpy.array([200, 255, 255])
mask = cv2.inRange(image_o, lower_red, upper_red)
cv2.imshow('mask',mask)

result = cv2.bitwise_and(image_o, image_o, mask = mask)
cv2.imshow("Yo",result)

cv2.waitKey(0)