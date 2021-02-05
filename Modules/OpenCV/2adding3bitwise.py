import cv2

mountain = cv2.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\mountain.jpg')
dragon = cv2.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\dragon.jpg')

dragon_i = cv2.bitwise_not(dragon)
# cv2.imwrite("C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\Dragon_inverted.jpg",dragon_inverted)
cv2.imshow('cat',mountain)
cv2.waitKey(0)
cv2.imshow('dragon',dragon)
cv2.waitKey(0)

cat_and_dragon = cv2.bitwise_and(mountain,dragon,mask = None)
cv2.imshow('AND',cat_and_dragon)
cv2.waitKey(0)

cat_or_dragon = cv2.bitwise_or(mountain,dragon,mask = None)
cv2.imshow('OR',cat_or_dragon)
cv2.waitKey(0)

cat_xor_dragon = cv2.bitwise_xor(mountain,dragon_i,mask = None)
cv2.imshow('XOR',cat_xor_dragon)
cv2.waitKey(0)