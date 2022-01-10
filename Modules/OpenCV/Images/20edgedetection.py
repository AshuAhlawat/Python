import cv2 
import numpy as np 

img = cv2.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\shapes.jpg') 
  
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
corners = cv2.goodFeaturesToTrack(gray_img, 100, 0.01, 10) 

corners = np.int0(corners) 

for i in corners: 
    x, y = i.ravel() 
    cv2.circle(img, (x, y), 3, (255, 0, 0), -1) 

cv2.imshow("Edges",img) 
cv2.waitKey(0)