#pip install opencv-python

import cv2 
from random import randrange as r
#can work with only greyscale
#only use with black and white image only
#____________________________________________________________________________________


trainedData=cv2.CascadeClassifier("Face.xml")
#load dataset
#classifer to find image from face.xml
#____________________________________________________________________________________

#start the web cam
webcam=cv2.VideoCapture(0)
while True:
    success,frame=webcam.read()
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

    #pause the img till Q,q  key is pressed.
    #show image
#____________________________________________________________________________________
webcam.release()
print("End of Code.")
#____________________________________________________________________________________

