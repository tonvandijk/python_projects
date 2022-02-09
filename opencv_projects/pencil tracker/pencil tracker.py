import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4,frameHeight)
cap.set(10,130)

myPenColors = [[24,72,126,42,209,228], #dit zijn de kleuren van de dop van de pen, opgezocht met de colorpicker webcam
            [98,94,0,124,255,255]]#ze staan in volgorde [hue min,sat min, val min, hue max, sat max, val max]

myDisplayColors = [[0,255,255],[255,0,0]]

myline = [] #x,y, kleurid (1 is geel 2 is blauw)

def findColor(img, myColors, myRealColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints=[]
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y = getContours(mask)
        
        cv2.circle(imgResult, (x,y), 10,myRealColors[count], cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
        #cv2.imshow(str(color[0]), mask)
    return newPoints


def getContours(img):
    x,y,w,h = 0,0,0,0
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>400:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)#
            omtrek = cv2.arcLength(cnt,True)
            benadering = cv2.approxPolyDP(cnt,0.02*omtrek,True)
            x, y, w, h = cv2.boundingRect(benadering)
    return x+w//2,y #bepaald top pen

def drawonscherm(myline, myColorValues):
    for point in myline:
        cv2.circle(imgResult, (point[0],point[1]), 10,myColorValues[point[2]], cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myPenColors, myDisplayColors)
    if len(newPoints)!=0:
        for nieuwpunt in newPoints:
            myline.append(nieuwpunt)

    if len(myline)!=0:
        drawonscherm(myline, myDisplayColors)


    cv2.imshow("Result", cv2.flip(imgResult, 1))
    
    if cv2.waitKey(1) & 0xFF == ord('q'):#sluit camera window, als je de q toets indrukt
        break

