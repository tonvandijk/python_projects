import cv2
import numpy as np


def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>400:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            omtrek = cv2.arcLength(cnt,True)
            #print(omtrek)
            benadering = cv2.approxPolyDP(cnt,0.02*omtrek,True)
            print(len(benadering))
            aantalHoeken = len(benadering)
            x, y, w, h = cv2.boundingRect(benadering)

            if aantalHoeken ==3: objectType ="driehoek"
            elif aantalHoeken == 4:
                vierkantheid = w/float(h)
                if vierkantheid >0.98 and vierkantheid <1.03: objectType= "vierkant"
                else:objectType="rechthoek"
            elif aantalHoeken == 5: objectType= "5 hoek"
            elif aantalHoeken == 6: objectType= "zeshoek"
            elif aantalHoeken == 7: objectType= "zevenhoek"
            #elif aantalHoeken == 8: objectType= "achthoek"
            elif aantalHoeken>7: objectType= "cirkel"
            else:objectType="None"

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,objectType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,
                        (0,0,0),2)  


path = "opencv_projects\\vorm_detectie\shapes.png"
img = cv2.imread(path)
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)

#cv2.imshow("img", img)
#cv2.imshow("imgGray", imgGray)
#cv2.imshow("imgBlur", imgBlur)
cv2.imshow("imgCanny", imgCanny)
cv2.imshow("imgresult", imgContour)


cv2.waitKey(0)