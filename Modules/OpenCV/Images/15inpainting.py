import cv2

cat = cv2.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\cat_damaged.png')
mask = cv2.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\cat_mask.png',0)

final = cv2.inpaint(cat, mask, 3, cv2.INPAINT_NS)

cv2.imshow('final',final)

cv2.waitKey(0)