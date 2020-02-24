import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    
    _,frame = cap.read()
    g_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    anchina_face =  smile.detectMultiScale(g_frame,1.3,10)
    
    for rec in anchina_face:
        (x,y,w,h) = rec
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
    
    
    cv2.imshow('frame',frame)
    key = cv2.waitKey(1)
    if key == ord('c'):
        break
        
cap.release()
cv2.destroyAllWindows()
