import cv2


image = cv2.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\cat_resized.jpg',0)

#simple thresholding
ret, thresh1 = cv2.threshold(image, 127.5, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(image, 127.5, 255, cv2.THRESH_TRUNC)
ret, thresh3 = cv2.threshold(image, 127.5, 255, cv2.THRESH_TOZERO)
ret, thresh4 = cv2.threshold(image, 127.5, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#adaptive thresholding
thresh5 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 127, 5)
thresh6 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 127, 5)

cv2.imshow('Original', image)
cv2.imshow('Binary', thresh1)
cv2.imshow('Trunc', thresh2)
cv2.imshow('ToZero', thresh3)
cv2.imshow('Otsu', thresh4)

# pdf Useful
cv2.imshow('Mean_Adaptive', thresh5)
cv2.imshow('Gaussian_Adaptive', thresh6)

cv2.waitKey(0)

