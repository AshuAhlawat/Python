import cv2

mountain = cv2.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\mountain.jpg')

mountains = cv2.copyMakeBorder(mountain,20,20,20,20,cv2.BORDER_CONSTANT)
cv2.imshow('Constant',mountains)
cv2.waitKey(0)

mountains = cv2.copyMakeBorder(mountain,20,20,20,20,cv2.BORDER_REFLECT)
cv2.imshow('Reflect',mountains)
cv2.waitKey(0)

mountains = cv2.copyMakeBorder(mountain,20,20,20,20,cv2.BORDER_DEFAULT)
cv2.imshow('Default',mountains)
cv2.waitKey(0)

mountains = cv2.copyMakeBorder(mountain,20,20,20,20,cv2.BORDER_REPLICATE)
cv2.imshow('Replicate',mountains)
cv2.waitKey(0)