import cv2
import time
cpt = 0
maxFrames = 75 # if you want 5 frames only.

cap=cv2.VideoCapture(0)

while cpt < maxFrames:
    ret, frame = cap.read()
    frame=cv2.resize(frame,(1280,720))
    cv2.imshow("test window", frame) # show image in window
    cv2.imwrite("E:/hsbd/10_%d.jpg" %cpt, frame)
    time.sleep(0.5)
    cpt += 1
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()