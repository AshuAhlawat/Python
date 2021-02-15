import cv2

dragon = cv2.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\dragon.jpg')
jungle = cv2.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\jungle.jpg')

#literally adding the pixels RGB values
x = dragon + jungle
cv2.imshow('add',x)
cv2.waitKey(0)
x = dragon - jungle
cv2.imshow('add',x)
cv2.waitKey(0)
x = jungle - dragon
cv2.imshow('add',x)
cv2.waitKey(0)

#overlapping images
overlap = cv2.addWeighted(jungle,0.7,dragon,1,0)
cv2.imshow('overlap',overlap)
cv2.waitKey(0)