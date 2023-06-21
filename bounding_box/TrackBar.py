import cv2 as cv
import numpy as np

def empty(a):
    pass

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv.cvtColor( imgArray[x][y], cv.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver



frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture('src/testing.webm')
cap.set(3, frameWidth)
cap.set(4, frameHeight)

path = 'src/test.png'

cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars", 640, 240)
cv.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv.createTrackbar("Val Min","TrackBars",0,255,empty)
cv.createTrackbar("Val Max","TrackBars",255,255,empty)

while True:
    success, img = cap.read()
    # img = cv.imread(path)
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv.getTrackbarPos("Val Max", "TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv.inRange(imgHSV,lower,upper)
    imgResult = cv.bitwise_and(img,img,mask=mask)

    imgStack = stackImages(0.6,([img,mask]))
    cv.imshow("Stacked Images", imgStack)

    if cv.waitKey(100) & 0xFF ==ord('q'):
        break