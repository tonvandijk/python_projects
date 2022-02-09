import cv2


facecas = cv2.CascadeClassifier("opencv/haarcascade_frontalface_default.xml")
img = cv2.imread('opencv/mensen.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = facecas.detectMultiScale(imgGray,1.1,4)


for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)



cv2.imshow("result", img)

cv2.waitKey(0)