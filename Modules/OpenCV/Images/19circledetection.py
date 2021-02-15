import cv2 
import numpy as np 
  
# Read image. 
img = cv2.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\eyes.png') 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

gray_blurred = cv2.blur(gray, (3, 3)) 

detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30) 

if detected_circles is not None: 
  
    # Convert the circle parameters a, b and r to integers. 
    detected_circles = np.uint16(np.around(detected_circles)) 
  
    for pt in detected_circles[0, :]: 
        a, b, r = pt[0], pt[1], pt[2] 
  
        # Draw the circumference of the circle. 
        cv2.circle(img, (a, b), r, (0, 0, 0), 2) 
  
        # Draw a small circle (of radius 1) to show the center. 
        cv2.circle(img, (a, b), 1, (255, 255, 255), 3) 
        cv2.imshow("Detected Circle", img) 
        cv2.waitKey(0)