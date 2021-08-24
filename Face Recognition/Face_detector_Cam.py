import cv2
import random


trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



#img=cv2.imread('TestMate.jpg') #Choose an Image to open
webcam =cv2.VideoCapture(0)

while True:
    successful_frame_read, frame = webcam.read()

    grayscaled_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)

    for(x,y,w,h) in face_coordinates:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (random.randint(128,255),random.randint(0,255),random.randint(0,255)) ,2)

    cv2.imshow('Honey Face Detecter', frame)
    key= cv2.waitKey(1)

    if key == 81 or key==113:
        break

webcam.release()

print('code completed')