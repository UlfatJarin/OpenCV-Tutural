import cv2

face_cascade = cv2.CascadeClassifier("face&object detection\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("face&object detection\haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("face&object detection\haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1 ,7)

    for (x,y,w,h) in faces :
        cv2.rectangle(frame , (x,y) , (x+w , y+h) , (0,255,0), 2)

    roi_gray = gray[y:y+h , x:x+w]
    roi_color = frame[ y:y+h , x:x+w]
    """
    roi - reason of interest
    cut face area 

    roi_gray = gray[y:y+h , x:x+w]
    gray [150 : 150 +80 , 100: 100+80]
     - cut the gray part in theface 

    roi_color = frame[y:y+h , x:x+w]
     - also need color version
     - text or boxes draw 


    """
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.1 ,10)
    if len(eyes)>0:
        cv2.putText(frame , "Eyes Detected",(x, y - 30) , cv2.FONT_HERSHEY_SIMPLEX , 0.6 , (0,0,255), 2)

    smile = smile_cascade.detectMultiScale(roi_gray, 1.7 ,20)
    if len(smile) > 0:
        cv2.putText(frame , "Smiling" ,(x, y - 10) , cv2.FONT_HERSHEY_SIMPLEX , 0.6 , (0,0,255), 2)


    cv2.imshow("Smart face Detecttion", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()