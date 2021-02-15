import cv2

image = cv2.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\cat_resized.jpg')

dst = cv2.fastNlMeansDenoisingColored(image, None, 20, 20, 7, 15)
cv2.imshow('',dst)

dst = cv2.fastNlMeansDenoisingColored(image, None, 5, 5, 7, 15)
cv2.imshow('',dst)

cv2.waitKey(0)