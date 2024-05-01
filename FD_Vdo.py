#pip install opencv-python
import cv2 
from random import randrange as r
#can work with only greyscale
#only use with black and white image only
#____________________________________________________________________________________
trainedData=cv2.CascadeClassifier("Face.xml")
#load dataset

#start the web cam
cam=cv2.VideoCapture('vdo.mp4')

while True:
    success,frame=cam.read()
    greyimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #convert img to grey scale
    faceCoordinates=trainedData.detectMultiScale(greyimg)
    #detecting a faces
    print(faceCoordinates)
    for x,y,w,h in faceCoordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(r(0,255),r(0,255),r(0,255)),2)
    cv2.imshow('Window',frame)

    key=cv2.waitKey(1)
    if(key==81 or key==113):
        break

#____________________________________________________________________________________
cam.release()
print("End of Code.")
#____________________________________________________________________________________

