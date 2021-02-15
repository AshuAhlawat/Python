import cv2
import numpy

img = cv2.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\shapes1.jpg')
img = cv2.pyrDown(img)
img = cv2.pyrDown(img)

image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(image,50,150)

lines = cv2.HoughLines(edges,1,numpy.pi/180,200)
print(lines[0])

for r,theta in lines[0]:
    
    a = numpy.cos(theta) 
    b = numpy.sin(theta) 

    x0 = a*r 
    y0 = b*r 
  
    x1 = int(x0 + 1000*(-b)) 
    y1 = int(y0 + 1000*(a)) 

    x2 = int(x0 - 1000*(-b)) 
    y2 = int(y0 - 1000*(a)) 

    cv2.line(img,(x1,y1), (x2,y2), (0,0,255),2) 

cv2.imshow('Image', image)
cv2.waitKey(0)