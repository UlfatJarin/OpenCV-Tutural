#import 
import cv2

cap = cv2.VideoCapture(0)

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

save = input("Wanna save the recorded video?(yes /no) ").lower()
if save == 'yes':
    codec = cv2.VideoWriter_fourcc(*'XVID')
    recorder = cv2.VideoWriter(f"{input("filename : ")}.avi",codec,20,(frame_width, frame_height))
else :
   recorder =None

    
while True:
    ret , frame = cap.read()
    if not ret:
        print("video cannot loaded")
        break

    if recorder is not None:
        recorder.write(frame)
    
    cv2.imshow("Live vedio", frame)    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('Quiting...')
        break

cap.release()
if recorder is not None:
    recorder.release()
cv2.destroyAllWindows()

