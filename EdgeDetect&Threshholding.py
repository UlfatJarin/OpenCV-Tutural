# very importent
# 40 - 50% ques


"""
1. *canny edge detection    - image outline ( prncil sckach type)
2. *image thesh holding     - complex photo to clean blackwhile photo
     - binary thresholding
     - adaptive thresholding
3. * Bitwise Operation  - combine , shape cut with logically
    - AND
    - OR
    - NOT



#key structure 

"""

#canny edge Detection .......5* for inter view......................................................
"""
edges = cv2.Canny(image ,threshold1, threshols2)

    threshold - set cutoff boundary - brigthness
            - if pixel white theam then make it white 
            - if pixel black theam then make it black
    threshold1 -lower boundary to detect  weak edges
    threshols2- uper boundery to detect storng edges 

find detecttion when light is changing  angwith many noice
                               1st - outline draw

- to detect border 
- seperate objects
- fetures extextion
- face detection 
- lain detection 
- scatch 


"""


import cv2
import numpy as np

img = cv2. imread("bluebird.jpg", cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(img, 50,150)

cv2.imshow("orginal Image",img)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()




# Thresholding in OpenCV
"""
 thresholded_image = cv2.threshold(image, thresh-value , max-value , method)
                  img = gray scale
                  thresh-value= cut off value (udually 0-255)[best - 100,120,150]
                  max-value = assign if pic is bright enough (usually 255)
                  mathod = most common -THRESH BINARY
                            if bigger then Thresh value 
                                then 255 - all white
                            or       0   - all black

 
"""
img = cv2. imread("bluebird.jpg", cv2.IMREAD_GRAYSCALE)

ret ,thresh_img = cv2.threshold(img, 120 , 255, cv2.THRESH_BINARY)

cv2.imshow("orginal Image",img)
cv2.imshow("Edges",thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Bitwise operation...........................................
"""
-combine 2 img 
    - same img height & white
    - grayscale / binary mask (white /black)
    - 
- cut out 1st image with 2nd img
- flip specific img 
- remove 
# pixle 
# #bitwise operation
  1 cv2.bitwise_and(img1, img2)  - cutout shape 
  2 cv2.bitwise_or(img1, img2)   -combime - multiple shape marge in one frame
  3 cv2.bitwise_not(img1 )  - while to black vice varsa

syntex - 


"""
img1 = np.zeros((300,300), dtype="uint8")
img2 = np.zeros((300,300), dtype="uint8")

cv2.circle(img1,(150,150),100, 255, -1)
cv2.rectangle(img2,(100,100),(250,250),255 ,-1)

bitwise_and =cv2.bitwise_and(img1,img2)
bitwise_or =cv2.bitwise_or(img1,img2)
bitwise_not =cv2.bitwise_not(img1)

cv2.imshow("Circle",img1)
cv2.imshow("Rectangle",img2)
cv2.imshow("AND",bitwise_and)
cv2.imshow("OR",bitwise_or)
cv2.imshow("NOT",bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()




