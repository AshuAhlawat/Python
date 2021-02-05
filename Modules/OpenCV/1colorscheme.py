import cv2

img = cv2.imread("C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\rainbow.jpg")
img_b, img_g, img_r = cv2.split(img)

cv2.imshow('Original',img)
cv2.waitKey(0)
cv2.imshow('Red Scheme',img_r)
cv2.waitKey(0)
cv2.imshow('Green Scheme',img_g)
cv2.waitKey(0)
cv2.imshow('Blue Scheme',img_b)
cv2.waitKey(0)