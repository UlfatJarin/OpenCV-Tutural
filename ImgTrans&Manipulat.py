
##..............................................................................................
#IMAGE TRansformations & Manipulation Techniques...................................................


#resizing & Scaling Image .................................................................

#resize..................................................
"""
cv2.resize()
zoom in / zoom out
smaller img - fast working 
ML - img size - 224* 224

resized = cv2.resize(src(orginalimg),dsize(new pixle size),fx(width), fy(Height), interpolation(for quality) )

"""
import cv2
image = cv2.imread("bird.jpg")

'''
if image is None:
    print("Image not found")
else :
    print("image Loaded")

    resize =cv2.resize(image, (300,300))
    cv2.imshow("Orginal Image",image)
    cv2.imshow("Resized Image",resize)
    cv2.imwrite("resize_output.jpg", resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''


#cropped by Slicing in OPenCV.................................................................
"""
y-axis = rows = top to bottom
x-axis = colum = left to right

image(start y : end y ,start x : end x)

"""

'''if image is not None :
    cropped = image[100:200, 50:150]

    cv2.imshow("Original",image)
    cv2.imshow("Cropped",cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''



#Image rotation and flipping....................................................................
#rotation .. 
"""
M= cv2.getRotationMatrix2d(center, angle , scale)
rotated_image = cv2.warpAffine(image, M , (width,height))


angle =  90deg - anticolckwise
        -90deg - clockwise

scale = integer divition  1.0 ,2.0 
 
center point = (width//2 , height//2)


"""
'''if image is None:
    print("Could not Load Image")
else:
    (h,w)=image.shape[:2]
    center = (w//2, h//2)
    M =cv2.getRotationMatrix2D(center, 90 , 1.0)
    rotated = cv2.warpAffine(image, M,(w,h))

    cv2.imshow("orginal",image)
    cv2.imshow("rotated 90 degree", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows( )'''


#flipting.....................................................................
"""
fliping = mirror image
0 = top to buttom 
1 = left to right
-1 = both

"""
if image is None:
    print("could nor load image")
else :
    flipped_horizontal = cv2.flip(image, 1)
    flipped_vertical = cv2.flip(image, 0)
    flipped_both = cv2.flip(image, -1)

    cv2.imshow("Orginal",image)
    cv2.imshow("Flip Horizontal",flipped_horizontal)
    cv2.imshow("Flipped Vertical",flipped_vertical)
    cv2.imshow("Flip Both",flipped_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows(  )