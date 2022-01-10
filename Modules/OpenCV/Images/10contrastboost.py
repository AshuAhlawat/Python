import cv2

image = cv2.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\cat.jpg',0)

image = cv2.resize(image,(1000,500))
cv2.imshow('Original',image)
cv2.waitKey(0)

equ = cv2.equalizeHist(image)
cv2.imshow('Equalized',equ)
cv2.waitKey(0)
