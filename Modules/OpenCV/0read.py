import cv2 as cv

img = cv.imread('cat.jpg')
cv.imshow('Cat',img)

cv.waitKey(0)

capture = cv.VideoCapture('RetroGrid.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow("RetroGrid", frame)

    if cv.waitKey(10) and 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
