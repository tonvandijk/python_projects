import cv2

cap = cv2.VideoCapture(0)

facecas = cv2.CascadeClassifier("opencv/haarcascade_frontalface_default.xml")

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = facecas.detectMultiScale(imgGray,1.1,4)
    
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),3)

    if cv2.waitKey(1) & 0xFF == ord('q'):#sluit camera window, als je de q toets indrukt
        break

    cv2.imshow("orginal", img)
    cv2.waitKey(1)
