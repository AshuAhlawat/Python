import cv2

cat = cv2.imread("C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\cat.jpg")
cv2.imshow('Original',cat)
cv2.waitKey(0)

cat_resized = cv2.resize(cat, (800,500))
cv2.imshow('new Cat',cat_resized)
cv2.waitKey(0)
# cv2.imwrite('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\cat_resized.jpg',cat_resized)

cat_resized = cv2.resize(cat, (0,0),fx=0.5, fy=0.5)
cv2.imshow('new Cat',cat_resized)
cv2.waitKey(0)
