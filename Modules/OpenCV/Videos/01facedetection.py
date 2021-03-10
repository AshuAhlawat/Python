import cv2

face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

def detect(gray, frame):
    faces = face.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces: 
        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2) 
        roi_gray = gray[y:y + h, x:x + w] 
        roi_color = frame[y:y + h, x:x + w]
        
        smiles = smile.detectMultiScale(roi_gray, 1.8, 20)
        eyes = eye.detectMultiScale(roi_gray, 1.8, 20)
  
        for (sx, sy, sw, sh) in smiles: 
            cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
            
        for (sx, sy, sw, sh) in eyes: 
            cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
            
    return frame 

video_capture = cv2.VideoCapture(0)

while True: 
    _, frame = video_capture.read()  
                
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   
      
    canvas = detect(gray, frame)    
              
    cv2.imshow('Video', canvas)  
    cv2.waitKey(1)

video_capture.release()                                  
cv2.destroyAllWindows() 