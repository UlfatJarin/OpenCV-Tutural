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

img = cv2. imread("books.jpg", cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(img, 50,150)

cv2.imshow("orginal Image",img)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()