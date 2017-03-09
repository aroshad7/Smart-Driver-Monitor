import numpy as np
import cv2
import winsound, platform, thread
face_cascade = cv2.CascadeClassifier('C:\\Users\\Arosha\\Downloads\\Programs\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_alt.xml')
#eye_cascade = cv2.CascadeClassifier('C:/Python27/Lib/site-packages/opencv/build/etc/haarcascades/haarcascade_eye_tree_eyeglasses.xml')
#lefteye_cascade = cv2.CascadeClassifier('C:/Python27/Lib/site-packages/opencv/build/etc/haarcascades/haarcascade_lefteye_2splits.xml')

video_capture = cv2.VideoCapture(0)
count = 0
iters = 0

def beep():
  for i in range(4):
    winsound.Beep(1500, 250)


while True:
    ret, frame = video_capture.read()
    if(ret==True):
      grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
      faces = face_cascade.detectMultiScale(grayFrame, 1.3, 5)
      for(x,y,w,h) in faces:
          frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
          roi_gray = grayFrame[y:y+h,x:x+w]
          roi_color = frame[y:y+h,x:x+w]
          #eyes = eye_cascade.detectMultiScale(roi_gray)
          #if len(eyes) == 0:
           # print ("Eyes closed")
          #else:
          #  print ("Eyes open")
          #count += len(eyes)
          #iters += 1
          #if iters == 2:
            #iters = 0
            #if count == 0:
             # print ("Drowsiness Detected!!!")
              #thread.start_new_thread(beep,())
            #count = 0
          #for (ex,ey,ew,eh) in eyes:
             # cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh), (0,255,0),2)


              
      cv2.imshow("Image",frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
