import cv2 as cv

def rescale(frame, h , w):
    height = int(frame.shape[0]*h/100)
    width = int(frame.shape[1]*w/100)
    
    dimensions = (width,height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INNER_AREA)

img = cv.imread('cat.jpg')

img = rescale(img,50,50)
cv.imshow("Cat",img)

cv.waitKey(0)

