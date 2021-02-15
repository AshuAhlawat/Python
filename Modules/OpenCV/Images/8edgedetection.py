import cv2

cat = cv2.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\cat_resized.jpg')

edges = cv2.Canny(cat,200,200)
cv2.imshow("Edgy", edges)
cv2.waitKey(0)

edges = cv2.Canny(cat,100,100)
cv2.imshow("Edgy", edges)
cv2.waitKey(0)

edges = cv2.Canny(cat,50,50)
cv2.imshow("Edgy", edges)
cv2.waitKey(0)


