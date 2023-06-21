import  cv2 as cv
import numpy as np
# print("Package Imported")

# ----- Chapter 1 -----

# img = cv.imread("src/lena.png")
# 
# cv.imshow("Output", img)
# cv.waitKey(0)

# cap = cv.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10, 100)

# while True:
#     success, img = cap.read()
#     cv.imshow("Video", img)
#     if cv.waitKey(1) & 0xFF ==ord('q'):
#         break

# -----  Chapter 2 -----

# img = cv.imread("src/lena.png")
# Kernel = np.ones((5, 5), np.uint8)
# 
# 
# imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# imgBlur = cv.GaussianBlur(imgGray, (7, 7), 0)
# imgCanny = cv.Canny(img, 150, 200)
# imgDialation = cv.dilate(imgCanny, Kernel, iterations=1)
# imgEroded = cv.erode(imgDialation, Kernel, iterations=1)
# 
# cv.imshow("Gray Image", imgGray)
# cv.imshow("Blur Image", imgBlur)
# cv.imshow("Canny Image", imgCanny)
# cv.imshow("Dialation Image", imgDialation)
# cv.imshow("Eroded Image", imgEroded)
# cv.waitKey(0)

# -----  Chapter 3 -----

# img = cv.imread("src/lambo.png")
# print(img.shape)

# imgResize = cv.resize(img, (1000, 500))
# print(imgResize.shape)

# imgCropped = img[0:200, 200:500]

# cv.imshow("Image", img)
# cv.imshow("Resize Image", imgResize)
# cv.imshow("Cropped Image", imgCropped)

# cv.waitKey(0)

# -----  Chapter 4 -----

# img = np.zeros((512, 512, 3), np.uint8)
# print(img.shape)
# img[:]= 255, 0, 0

# cv.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
# cv.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)
# cv.circle(img, (400, 50), 30, (255, 255, 0), 5)
# cv.putText(img, "OPENCV ", (300, 200), cv.FONT_ITALIC, 1, (0, 150, 0), 2)

# cv.imshow("Image", img)

# cv.waitKey(0)

# -----  Chapter 5 -----

# img = cv.imread("src/cards.jpg")


# width, height = 250, 350
# pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
# pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
# matrix = cv.getPerspectiveTransform(pts1, pts2)
# imgOutput = cv.warpPerspective(img, matrix, (width, height))

# cv.imshow("Image", img)
# cv.imshow("Output Image", imgOutput)

# cv.waitKey(0)

# -----  Chapter 6 -----

# def stackImages(scale,imgArray):
#     rows = len(imgArray)
#     cols = len(imgArray[0])
#     rowsAvailable = isinstance(imgArray[0], list)
#     width = imgArray[0][0].shape[1]
#     height = imgArray[0][0].shape[0]
#     if rowsAvailable:
#         for x in range ( 0, rows):
#             for y in range(0, cols):
#                 if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
#                     imgArray[x][y] = cv.resize(imgArray[x][y], (0, 0), None, scale, scale)
#                 else:
#                     imgArray[x][y] = cv.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
#                 if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv.cvtColor( imgArray[x][y], cv.COLOR_GRAY2BGR)
#         imageBlank = np.zeros((height, width, 3), np.uint8)
#         hor = [imageBlank]*rows
#         hor_con = [imageBlank]*rows
#         for x in range(0, rows):
#             hor[x] = np.hstack(imgArray[x])
#         ver = np.vstack(hor)
#     else:
#         for x in range(0, rows):
#             if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#                 imgArray[x] = cv.resize(imgArray[x], (0, 0), None, scale, scale)
#             else:
#                 imgArray[x] = cv.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
#             if len(imgArray[x].shape) == 2: imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
#         hor= np.hstack(imgArray)
#         ver = hor
#     return ver


# img = cv.imread("src/lena.png")
# imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# imgStack = stackImages(0.5,([img,imgGray,img],[img,img,img]))


# # imgHor = np.hstack((img, img))
# # imgVer = np.vstack((img, img))

# # cv.imshow("Horizontal", imgHor)
# # cv.imshow("Vertikal", imgVer)
# cv.imshow("ImageStack",imgStack)


# cv.waitKey(0)

# -----  Chapter 7 -----

# def empty(a):
#     pass


# def stackImages(scale,imgArray):
#     rows = len(imgArray)
#     cols = len(imgArray[0])
#     rowsAvailable = isinstance(imgArray[0], list)
#     width = imgArray[0][0].shape[1]
#     height = imgArray[0][0].shape[0]
#     if rowsAvailable:
#         for x in range ( 0, rows):
#             for y in range(0, cols):
#                 if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
#                     imgArray[x][y] = cv.resize(imgArray[x][y], (0, 0), None, scale, scale)
#                 else:
#                     imgArray[x][y] = cv.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
#                 if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv.cvtColor( imgArray[x][y], cv.COLOR_GRAY2BGR)
#         imageBlank = np.zeros((height, width, 3), np.uint8)
#         hor = [imageBlank]*rows
#         hor_con = [imageBlank]*rows
#         for x in range(0, rows):
#             hor[x] = np.hstack(imgArray[x])
#         ver = np.vstack(hor)
#     else:
#         for x in range(0, rows):
#             if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#                 imgArray[x] = cv.resize(imgArray[x], (0, 0), None, scale, scale)
#             else:
#                 imgArray[x] = cv.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
#             if len(imgArray[x].shape) == 2: imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
#         hor= np.hstack(imgArray)
#         ver = hor
#     return ver


# path = 'src/lambo.png'

# cv.namedWindow("TrackBars")
# cv.resizeWindow("TrackBars", 640, 240)
# cv.createTrackbar("Hue Min","TrackBars",0,179,empty)
# cv.createTrackbar("Hue Max","TrackBars",179,179,empty)
# cv.createTrackbar("Sat Min","TrackBars",0,255,empty)
# cv.createTrackbar("Sat Max","TrackBars",255,255,empty)
# cv.createTrackbar("Val Min","TrackBars",0,255,empty)
# cv.createTrackbar("Val Max","TrackBars",255,255,empty)


# while True:
#     img = cv.imread(path)
#     imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#     h_min = cv.getTrackbarPos("Hue Min","TrackBars")
#     h_max = cv.getTrackbarPos("Hue Max", "TrackBars")
#     s_min = cv.getTrackbarPos("Sat Min", "TrackBars")
#     s_max = cv.getTrackbarPos("Sat Max", "TrackBars")
#     v_min = cv.getTrackbarPos("Val Min", "TrackBars")
#     v_max = cv.getTrackbarPos("Val Max", "TrackBars")
#     print(h_min,h_max,s_min,s_max,v_min,v_max)
#     lower = np.array([h_min,s_min,v_min])
#     upper = np.array([h_max,s_max,v_max])
#     mask = cv.inRange(imgHSV,lower,upper)
#     imgResult = cv.bitwise_and(img,img,mask=mask)


#     # cv.imshow("Original", img)
#     # cv.imshow("HSV", imgHSV)
#     # cv.imshow("Mask", mask)
#     # cv.imshow("Result", imgResult)

#     imgStack = stackImages(0.6,([img,imgHSV],[mask,imgResult]))
#     cv.imshow("Stacked Images", imgStack)

#     cv.waitKey(1)


# -----  Chapter 8 -----

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

def getContours(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        print(area)
        if area > 500:
            cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)
            print(peri)
            approx = cv.approxPolyDP(cnt, 0.05*peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv.boundingRect(approx)

            if objCor == 3:objectType="triangle"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio >0.98 and aspRatio <1.03: objectType= "Square"
                else:objectType="Rectangle"
            elif objCor>4: objectType= "Circles"
            else:objectType="None"

            cv.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv.putText(imgContour, objectType, (x, y-5), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)



path ='src/shapes.png'
img = cv.imread(path)
imgContour = img.copy()


imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv.Canny(imgBlur,50,50)
getContours(imgCanny)


imgBlank = np.zeros_like(img)
imgStack = stackImages(0.8,([img,imgGray,imgBlur], [imgCanny,imgContour,imgBlank]))

cv.imshow("Original", img)

cv.imshow("Stack", imgStack)
 
cv.waitKey(0)
 

# # -----  Chapter 9 -----

# faceCascade= cv.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
# img = cv.imread('src/lena.png')
# imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# faces = faceCascade.detectMultiScale(imgGray,1.1,4)

# for (x,y,w,h) in faces:
#     cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


# cv.imshow("Result", img)
# cv.waitKey(0)


# # -----  Project 1 -----

# frameWidth = 640
# frameHeight = 480
# cap = cv.VideoCapture(1)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)
# cap.set(10,150)

# myColors = [[5,107,0,19,255,255],
#             [133,56,0,159,156,255],
#             [57,76,0,100,255,255],
#             [90,48,0,118,255,255]]
# myColorValues = [[51,153,255],          ## BGR
#                  [255,0,255],
#                  [0,255,0],
#                  [255,0,0]]

# myPoints =  []  ## [x , y , colorId ]

# def findColor(img,myColors,myColorValues):
#     imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#     count = 0
#     newPoints=[]
#     for color in myColors:
#         lower = np.array(color[0:3])
#         upper = np.array(color[3:6])
#         mask = cv.inRange(imgHSV,lower,upper)
#         x,y=getContours(mask)
#         cv.circle(imgResult,(x,y),15,myColorValues[count],cv.FILLED)
#         if x!=0 and y!=0:
#             newPoints.append([x,y,count])
#         count +=1
#         #cv.imshow(str(color[0]),mask)
#     return newPoints

# def getContours(img):
#     contours,hierarchy = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
#     x,y,w,h = 0,0,0,0
#     for cnt in contours:
#         area = cv.contourArea(cnt)
#         if area>500:
#             #cv.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
#             peri = cv.arcLength(cnt,True)
#             approx = cv.approxPolyDP(cnt,0.02*peri,True)
#             x, y, w, h = cv.boundingRect(approx)
#     return x+w//2,y

# def drawOnCanvas(myPoints,myColorValues):
#     for point in myPoints:
#         cv.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv.FILLED)


# while True:
#     success, img = cap.read()
#     imgResult = img.copy()
#     newPoints = findColor(img, myColors,myColorValues)
#     if len(newPoints)!=0:
#         for newP in newPoints:
#             myPoints.append(newP)
#     if len(myPoints)!=0:
#         drawOnCanvas(myPoints,myColorValues)


#     cv.imshow("Result", imgResult)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# # Color Picker

# frameWidth = 640
# frameHeight = 480
# cap = cv.VideoCapture(1)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)


# def empty(a):
#     pass


# cv.namedWindow("HSV")
# cv.resizeWindow("HSV", 640, 240)
# cv.createTrackbar("HUE Min", "HSV", 0, 179, empty)
# cv.createTrackbar("HUE Max", "HSV", 179, 179, empty)
# cv.createTrackbar("SAT Min", "HSV", 0, 255, empty)
# cv.createTrackbar("SAT Max", "HSV", 255, 255, empty)
# cv.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
# cv.createTrackbar("VALUE Max", "HSV", 255, 255, empty)

# while True:

#     success, img = cap.read()
#     imgHsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#     h_min = cv.getTrackbarPos("HUE Min", "HSV")
#     h_max = cv.getTrackbarPos("HUE Max", "HSV")
#     s_min = cv.getTrackbarPos("SAT Min", "HSV")
#     s_max = cv.getTrackbarPos("SAT Max", "HSV")
#     v_min = cv.getTrackbarPos("VALUE Min", "HSV")
#     v_max = cv.getTrackbarPos("VALUE Max", "HSV")
#     print(h_min)

#     lower = np.array([h_min, s_min, v_min])
#     upper = np.array([h_max, s_max, v_max])
#     mask = cv.inRange(imgHsv, lower, upper)
#     result = cv.bitwise_and(img, img, mask=mask)

#     mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
#     hStack = np.hstack([img, mask, result])
#     cv.imshow('Horizontal Stacking', hStack)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv.destroyAllWindows()

# # -----  Project 2 -----

# ###################################
# widthImg=540
# heightImg =640
# #####################################

# cap = cv.VideoCapture(1)
# cap.set(10,150)


# def preProcessing(img):
#     imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#     imgBlur = cv.GaussianBlur(imgGray,(5,5),1)
#     imgCanny = cv.Canny(imgBlur,200,200)
#     kernel = np.ones((5,5))
#     imgDial = cv.dilate(imgCanny,kernel,iterations=2)
#     imgThres = cv.erode(imgDial,kernel,iterations=1)
#     return imgThres

# def getContours(img):
#     biggest = np.array([])
#     maxArea = 0
#     contours,hierarchy = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
#     for cnt in contours:
#         area = cv.contourArea(cnt)
#         if area>5000:
#             #cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
#             peri = cv.arcLength(cnt,True)
#             approx = cv.approxPolyDP(cnt,0.02*peri,True)
#             if area >maxArea and len(approx) == 4:
#                 biggest = approx
#                 maxArea = area
#     cv.drawContours(imgContour, biggest, -1, (255, 0, 0), 20)
#     return biggest

# def reorder (myPoints):
#     myPoints = myPoints.reshape((4,2))
#     myPointsNew = np.zeros((4,1,2),np.int32)
#     add = myPoints.sum(1)
#     #print("add", add)
#     myPointsNew[0] = myPoints[np.argmin(add)]
#     myPointsNew[3] = myPoints[np.argmax(add)]
#     diff = np.diff(myPoints,axis=1)
#     myPointsNew[1]= myPoints[np.argmin(diff)]
#     myPointsNew[2] = myPoints[np.argmax(diff)]
#     #print("NewPoints",myPointsNew)
#     return myPointsNew

# def getWarp(img,biggest):
#     biggest = reorder(biggest)
#     pts1 = np.float32(biggest)
#     pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
#     matrix = cv.getPerspectiveTransform(pts1, pts2)
#     imgOutput = cv.warpPerspective(img, matrix, (widthImg, heightImg))

#     imgCropped = imgOutput[20:imgOutput.shape[0]-20,20:imgOutput.shape[1]-20]
#     imgCropped = cv.resize(imgCropped,(widthImg,heightImg))

#     return imgCropped


# def stackImages(scale,imgArray):
#     rows = len(imgArray)
#     cols = len(imgArray[0])
#     rowsAvailable = isinstance(imgArray[0], list)
#     width = imgArray[0][0].shape[1]
#     height = imgArray[0][0].shape[0]
#     if rowsAvailable:
#         for x in range ( 0, rows):
#             for y in range(0, cols):
#                 if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
#                     imgArray[x][y] = cv.resize(imgArray[x][y], (0, 0), None, scale, scale)
#                 else:
#                     imgArray[x][y] = cv.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
#                 if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv.cvtColor( imgArray[x][y], cv.COLOR_GRAY2BGR)
#         imageBlank = np.zeros((height, width, 3), np.uint8)
#         hor = [imageBlank]*rows
#         hor_con = [imageBlank]*rows
#         for x in range(0, rows):
#             hor[x] = np.hstack(imgArray[x])
#         ver = np.vstack(hor)
#     else:
#         for x in range(0, rows):
#             if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#                 imgArray[x] = cv.resize(imgArray[x], (0, 0), None, scale, scale)
#             else:
#                 imgArray[x] = cv.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
#             if len(imgArray[x].shape) == 2: imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
#         hor= np.hstack(imgArray)
#         ver = hor
#     return ver

# while True:
#     success, img = cap.read()
#     img = cv.resize(img,(widthImg,heightImg))
#     imgContour = img.copy()

#     imgThres = preProcessing(img)
#     biggest = getContours(imgThres)
#     if biggest.size !=0:
#         imgWarped=getWarp(img,biggest)
#         # imageArray = ([img,imgThres],
#         #           [imgContour,imgWarped])
#         imageArray = ([imgContour, imgWarped])
#         cv.imshow("ImageWarped", imgWarped)
#     else:
#         # imageArray = ([img, imgThres],
#         #               [img, img])
#         imageArray = ([imgContour, img])

#     stackedImages = stackImages(0.6,imageArray)
#     cv.imshow("WorkFlow", stackedImages)

#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# # -----  Project 3 -----

# #############################################
# frameWidth = 640
# frameHeight = 480
# nPlateCascade = cv.CascadeClassifier("haarcascades/haarcascade_russian_plate_number.xml")
# minArea = 200
# color = (255,0,255)
# ###############################################
# cap = cv.VideoCapture("src/testing.webm")
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)
# cap.set(10,150)
# count = 0

# while True:
#     success, img = cap.read()
#     imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#     numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)
#     for (x, y, w, h) in numberPlates:
#         area = w*h
#         if area >minArea:
#             cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
#             cv.putText(img,"Number Plate",(x,y-5),
#                         cv.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
#             imgRoi = img[y:y+h,x:x+w]
#             cv.imshow("ROI", imgRoi)

#     cv.imshow("Result", img)
#     cv.waitKey(5)

    # if cv.waitKey(1) & 0xFF == ord('s'):
    #     cv.imwrite("Resources/Scanned/NoPlate_"+str(count)+".jpg",imgRoi)
    #     cv.rectangle(img,(0,200),(640,300),(0,255,0),cv.FILLED)
    #     cv.putText(img,"Scan Saved",(150,265),cv.FONT_HERSHEY_DUPLEX,
    #                 2,(0,0,255),2)
    #     cv.imshow("Result",img)
    #     cv.waitKey(500)
    #     count +=1
