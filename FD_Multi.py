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

img1=cv2.imread('Multi.jpg')
#choose a img
#____________________________________________________________________________________

greyimg=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
#convert img to grey scale
#____________________________________________________________________________________


faceCoordinates=trainedData.detectMultiScale(greyimg)
#detecting a faces

print(faceCoordinates)
#[[281  67 286 286]
# [685 609  49  49]]
for x,y,w,h in faceCoordinates:
    cv2.rectangle(img1,(x,y),(x+w,y+h),(r(0,255),r(0,255),r(0,255)),2)

#____________________________________________________________________________________


cv2.imshow('Multiple Persons',img1)
cv2.waitKey()
#pause the img till nay key is pressed.
#show image
#____________________________________________________________________________________


print("End of Code.")
#____________________________________________________________________________________

