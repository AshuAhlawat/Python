import cv2

cat = cv2.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\cat.jpg')
kitten = cv2.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\kitten.jpg')

x = kitten - kitten
cv2.imshow('add',x)
cv2.waitKey(0)
x = kitten + kitten
cv2.imshow('add',x)
cv2.waitKey(0)
x = cat - cat
cv2.imshow('add',x)
cv2.waitKey(0)
x = cat + cat
cv2.imshow('add',x)
cv2.waitKey(0)
x = cat + kitten
cv2.imshow('add',x)
cv2.waitKey(0)
x = cat - kitten
cv2.imshow('add',x)
cv2.waitKey(0)
x = kitten - cat
cv2.imshow('add',x)
cv2.waitKey(0)