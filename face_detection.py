import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
images = cv2.imread("resources/alif3.jpg",1)
image = cv2.resize(images, (1080,720))
#gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(image, 1.3, 5)
print(type(faces))
print(faces)

for x,y,w,h in faces:
    image = cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 3)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()