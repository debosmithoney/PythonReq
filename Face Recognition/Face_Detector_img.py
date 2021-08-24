import cv2
import random


trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img=cv2.imread('TestMate.jpg') #Choose an Image to open

grayscaled_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)

for(x,y,w,h) in face_coordinates:
   cv2.rectangle(img, (x,y), (x+w,y+h), (random.randint(128,255),random.randint(0,255),random.randint(0,255)) ,2)


cv2.imshow('Honey Face Detecter', img)
cv2.waitKey()

print("Code Completed")