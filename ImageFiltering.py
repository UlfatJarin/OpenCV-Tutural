import cv2
import numpy as np

#image filtering ..............................................
"""
blur- gaussian 
    - median
    - bilateral 
    - normal 
noise remove 
sharp to smoorth 
kernel

"""
#Gaussian Blur 
"""
- soft & smoth
- noise remove 
- 

cv2.GaussianBlur(image,(kernal_size_x , kernel_size_y), sigma)
   -avarage value is use

kernel_size =window size-  always odd number - (3,3) ,(5,5),(9,9)
      (3,3)= light blur
      (9,9)= strong blur
      (21,21)= super blue

sigma = howstrong blur
   0- oven cv2 decided 
"""

'''image= cv2.imread("books.jpg")

blurred = cv2.GaussianBlur(image ,(7,7), 3)

cv2.imshow("Orginal image",image)
cv2.imshow("Blurred image",blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()'''


"""
median blur 
     - spot detect & remove
     - medium value uses
blurred = cv.medianBlur(image, kernel_size)
    - 

"""
'''image= cv2.imread("cousin.jpg")

blurred = cv2.medianBlur(image , 3)

cv2.imshow("Orginal image",image)
cv2.imshow("cleand image",blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#Sharping ....................................................................
"""
cv2.filter2D(src, depth ,Kernel)
  -depth = -1 to same 
  
  sharpen_kernal = np.array([
     [ 0, -1 ,  0],
     [-1,  5 , -1],
     [ 0, -1 ,  0]  
  ])
     0= ignore


"""

'''image= cv2.imread("books.jpg")

sharpen_kernel = np.array([
    [ 0, -1 ,  0],
     [-1,  5 , -1],
     [ 0, -1 ,  0]  
])

sharpen = cv2.filter2D(image , -1 ,sharpen_kernel)

cv2.imshow("Orginal image",image)
cv2.imshow("Sharpend image",sharpen)
cv2.waitKey(0)
cv2.destroyAllWindows()'''





