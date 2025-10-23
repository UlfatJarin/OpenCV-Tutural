import cv2
import numpy as np

image = cv2.imread("bird.jpg")

while True:
    if image is None:
        print("Sorry , image cannot loaded ! Try Again...")
    
    else :
        choices = input(" Services : \n 1.GaussianBlur - a \n 2.MedianBlur - b \n 3.Sharping -c \n 4.canny edge detection - d \n 5.thesh holding - e  \n 6. Bitwise Operation - f \n \n Your Choice?(a-f) : " ).lower()
        print("\n")

        if choices == "a":
            print("This is your GaussianBlur image: ")

            GaussianBlur = cv2.GaussianBlur(image , (7,7) ,5)

            cv2.imshow("GaussianBlur Image:",GaussianBlur)
            

        elif choices == "b":
            print("This is your MedianBlur image: ")

            MedianBlur = cv2.medianBlur(image, 3)

            cv2.imshow("MedianBlur",MedianBlur)

        elif choices == "c":
            print("This is your Sharping image: ")

        elif choices == "d":
            print("This is your canny edge detection image: ")

        elif choices == "e":
            print("This is your thesh holding image: ")

        elif choices == "f":
            print("This is your Bitwise Operation image: ")

        else:
            print("Worng Input")
        
        cv2.imwrite("orginal",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    MoreEdit= input("Want to more edit(y / n) : ") 
    if MoreEdit == "n":
        print ("\n Hope you Enjoy Editing")
        break




