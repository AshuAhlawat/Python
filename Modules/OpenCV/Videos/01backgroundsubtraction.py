import cv2
import numpy
cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

movement = 0

while(True):
    
    if movement > 3:
        print("motion!")
        movement = 0
    
    ret, frame = cap.read()

    #downing resoltion as a pyramid
    frame = cv2.pyrDown(frame)
    
    kernel = numpy.ones((5,5),numpy.uint8)
    frame = cv2.erode(frame, kernel)
    
    fgmask = fgbg.apply(frame)
    
    cv2.imshow('fgmask', fgmask)
    
    (height,width) = frame.shape[:2]
    res = height*width
    
    white = 0
    for i in numpy.nditer(fgmask):
        if i == 255:
            white = white +1
    
    if white > res/63:
        movement = movement+1
    else:
        movement = 0
        
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()