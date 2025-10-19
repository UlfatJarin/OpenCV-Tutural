import cv2
"""
 vdo - 
    collection of images 
    each image is frame 
    fast  in every second 30_40 image

web cam 
    live vdo capcthar

Frame by frame processing 
    for detact objects by frames 
    F1 - detact person , draw box 
    F2 - detact object , draw box 

 """


#Cv2.videoCapture()..................................................................
"""
cap = cv2.VideoCapture(source)
to open vdo 
 
source = 
     open or pcapture vdo feom computer/laptop = 0
     external  device -web cam , usb connecte    = 1

ord('q') - q press korly loop exit
0xFF - bitwise and operation
waitkey= 1  means wait 1 milisecond
.release() - to close vdo
"""
'''
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()    
                            #ret(return) = True/False   #frame= image (the moment cptured)

    if not ret:
        print("Could not read frame")
        break

    cv2.imshow("webcam Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting....")
        break

cap.release()
cv2.destroyAllWindows()'''


#saving webcam video to a file with openCV..............................................
"""
 cv2.videoWriter()
 
level 1 
   videocapture(0)  # app open - start vdo
   vediowriter()    # save
   .release()       # close

level 2
   open wen cam 
   what width & height
   start + save 
   show 
   'q'  - quit 


cv2.vedioWriter(filename , codec , fps , frame_size )
       -.mp4 , .avi(picture + sound)     using XVID codec
     codec - compression formet  
     fps -   frames per second
     frame_size-

"""

# saving vdo ...............................................................
camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')
recorder = cv2.VideoWriter("my_video.avi", codec, 20, (frame_width, frame_height))

while True :
    success , image = camera.read()

    if not success:
        break

    recorder.write(image)
    cv2.imshow("Recording LIve", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


camera.release()
recorder.release()
cv2. destroyAllWindows()
