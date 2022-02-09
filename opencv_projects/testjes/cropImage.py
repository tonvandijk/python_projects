import cv2
import numpy as np

print(cv2.__version__)

img = cv2.imread("")

print(img.shape)

imgResize = cv2.resize(img, (230,300))

imgCropped = img[0:500, 200:500]
cv2.imshow("image", img)
cv2.imshow("cropped", imgCropped)

cv2.waitKey(0)