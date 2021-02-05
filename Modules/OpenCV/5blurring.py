import cv2

jungle = cv2.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\jungle.jpg')
cv2.imshow('Original',jungle)
cv2.waitKey(0)

jungle_blur = cv2.GaussianBlur(jungle,(5,5),0)
cv2.imshow('Gaussian',jungle_blur)
cv2.waitKey(0)

jungle_blur = cv2.GaussianBlur(jungle,(9,9),1)
cv2.imshow('Gaussian',jungle_blur)
cv2.waitKey(0)

jungle_blur = cv2.GaussianBlur(jungle,(9,9),0)
cv2.imshow('Gaussian',jungle_blur)
cv2.waitKey(0)

jungle_blur = cv2.medianBlur(jungle,5)
cv2.imshow('Gaussian',jungle_blur)
cv2.waitKey(0)

bilateral = cv2.bilateralFilter(jungle, 9, 75, 75) 
cv2.imshow('Bilateral Blurring', bilateral) 
cv2.waitKey(0) 