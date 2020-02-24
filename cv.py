import cv2
import numpy

cap = cv2.VideoCapture(0)

_,first_vids = cap.read()
x = 300
y = 305
width = 100
height = 115
the_focus = first_vids[x:x+width,y:y+height]      
focus_hsv = cv2.cvtColor(the_focus,cv2.COLOR_BGR2HSV)
focus_hist = cv2.calcHist([focus_hsv],[0],None,[180],[0,180])
focus_hist = cv2.normalize(focus_hist,focus_hist,0,255,cv2.NORM_MINMAX)


term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,1)



while True:
    
    _,frame = cap.read()
    
    
    frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.calcBackProject([frame_hsv],[0],focus_hist,[0,180],1)
    
    _,trackwindow = cv2.meanShift(mask,(x,y,width,height),term_criteria)
    x,y,w,h = trackwindow
    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow('focus',the_focus)
    cv2.imshow('frame',frame)
    key = cv2.waitKey(1)
    if key == ord('c'):
        break
        
cap.release()
cv2.destroyAllWindows()
