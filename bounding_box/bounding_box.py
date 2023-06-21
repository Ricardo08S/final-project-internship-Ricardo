import cv2 as cv
import numpy as np

#############################################
frameWidth = 640
frameHeight = 480
red_lower = np.array([165, 155, 55])
red_upper = np.array([179, 255, 255])
green_lower = np.array([30, 10, 0])
green_upper = np.array([120, 255, 255])
blue_lower = np.array([])
blue_upper = np.array([])
yellow_lower = np.array([])
yellow_upper = np.array([])
###############################################

cap = cv.VideoCapture("src/testing.webm")
cap.set(3, frameWidth)
cap.set(4, frameHeight)
# cap.set(10,150)

def getContours(img1, img2):
    contours1, hierarchy1 = cv.findContours(img1, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    contours2, hierarchy2 = cv.findContours(img2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    # contours3, hierarchy3 = cv.findContours(img3, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    # contours4, hierarchy4 = cv.findContours(img4, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours1:
        area = cv.contourArea(cnt)
        # print(area)
        if area > 50.0:
            # cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)
            # print(peri)
            approx = cv.approxPolyDP(cnt, 0.02*peri, True)
            # print(len(approx))
            
            objectType = "Red Balls"
            x, y, w, h = cv.boundingRect(approx)
            cv.rectangle(imgContour, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv.putText(imgContour, objectType, (x, y-5), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)
    
    for cnt in contours2:
        area = cv.contourArea(cnt)
        # print(area)
        if (area > 100.0) & (area < 300):
            # cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)
            # print(peri)
            approx = cv.approxPolyDP(cnt, 0.02*peri, True)
            # print(len(approx))
            
            objectType = "Green Balls"
            x, y, w, h = cv.boundingRect(approx)
            cv.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv.putText(imgContour, objectType, (x, y-5), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)

    # for cnt in contours3:
    #     area = cv.contourArea(cnt)
    #     # print(area)
    #     if area > 50.0:
    #         # cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
    #         peri = cv.arcLength(cnt, True)
    #         print(peri)
    #         approx = cv.approxPolyDP(cnt, 0.02*peri, True)
    #         # print(len(approx))
            
    #         objectType = "Blue Balls"
    #         x, y, w, h = cv.boundingRect(approx)
    #         cv.rectangle(imgContour, (x, y), (x+w, y+h), (255, 0, 0), 2)
    #         cv.putText(imgContour, objectType, (x, y-5), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
    
    # for cnt in contours4:
    #     area = cv.contourArea(cnt)
    #     # print(area)
    #     if area > 50.0:
    #         # cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
    #         peri = cv.arcLength(cnt, True)
    #         print(peri)
    #         approx = cv.approxPolyDP(cnt, 0.02*peri, True)  
    #         # print(len(approx))
            
    #         objectType = "Yellow Balls"
    #         x, y, w, h = cv.boundingRect(approx)
    #         cv.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 255), 2)
    #         cv.putText(imgContour, objectType, (x, y-5), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 255), 1)

            



while True:
    success, img = cap.read()
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    imgBlur = cv.GaussianBlur(imgHSV,(7,7),1)
    imgCanny = cv.Canny(imgBlur,200,200)
    imgContour = img.copy()
    mask_red = cv.inRange(imgHSV, red_lower, red_upper)
    mask_green = cv.inRange(imgHSV, green_lower, green_upper)
    # mask_blue = cv.inRange(imgHSV, blue_lower, blue_upper)
    # mask_yellow = cv.inRange(imgHSV, yellow_lower, yellow_upper)
    getContours(mask_red, mask_green)

    cv.imshow("Result", imgContour)

    if cv.waitKey(5) & 0xFF ==ord('q'):
        break