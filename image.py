import cv2

# to read the Inamge........................................................................
image = cv2.imread("DSC02401.jpg")

"""if image is None:
    print("Error : Image not found")
else:
    print("Image loaded successfully")"""


#to DIsplay the Inamge...............................................................................
"""
cv2.imshow("window Title",image)  #
cv2.waitKey(0)  # until amy press in keyboard ,, windows will be open
cv2.distropAllWindowa() # close in cleany way 

"""
"""if image is not None:
    cv2.imshow("Image Showing",image) # open the window
    cv2.waitKey(0)                    # wait for a key
    cv2.destroyAllWindows()           # close the window
else:
    print("could not load the image")  """


# to save image...................................................................................
# imwrite("file name",image)

"""if image is not None:
    success= cv2.imwrite("outputimage.jpg",image)
    if success:
        print("Image saved succesfully ")
    else:
        print("Failed to save")
else:
    print("Error: Couldnot load image")"""


#image dimention.............................................................
"""
height 
width
color chanal = (gray scale(only hight width), RGB , BGR)

"""
"""if image is not None:
    h, w, c= image.shape
    print(f"Image Loaded :\nHeight: {h}\nWidth: {w}\nChannels: {c}")
else:
    print("could not load Image")"""

#grayScale conversion....................................................................
"""
#cv2.cvtcolor(image ,cv2.COLOR_BGR@)  
grayscale
   low procccesing time 
   low complexity

"""
if image is not None:
    gray =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("could not load the Image")




