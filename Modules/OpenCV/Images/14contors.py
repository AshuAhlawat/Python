import cv2
import numpy as np

image = cv2.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\shapes.jfif')
image_bw = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

ret, image_th = cv2.threshold(image_bw, 100, 200, 0)

contours, _= cv2.findContours(image_th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = np.array(contours, dtype=object)


for approx in contours:

    cv2.drawContours(image, [approx], 0 , (50,50,255), 5)

    approx = approx.ravel()
    i = 0

    for _ in approx:
        if( i % 2 == 0 ):
            x = approx[i]
            y = approx[i+1]
            
            label = str(x) + " " + str(y)
            
            # cv2.putText(image, label, (x,y) , cv2.FONT_HERSHEY_SIMPLEX , 0.5, (255, 50, 50))
        
        i = i + 1

cv2.imshow('Contours', image)
cv2.waitKey(0)
    
    
    