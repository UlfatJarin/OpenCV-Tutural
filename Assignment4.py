import cv2
import numpy as np

image = cv2.imread("bird.jpg")
GSimg = cv2.cvtColor(image ,cv2.COLOR_BGR2GRAY)

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
            print("This is your MedianBlur (Black&Whiteimage): ")

            MedianBlur = cv2.medianBlur(image, 3)

            cv2.imshow("MedianBlur",MedianBlur)

        elif choices == "c":
            print("This is your Sharping image: ")

            Sharped_Kernel = np.array ([
                [ 0, -1,  0],
                [-1,  5, -1],
                [ 0, -1,  0]
            ])

            sharpend = cv2.filter2D(image , -1 , Sharped_Kernel)

            cv2.imshow("Sharping Image",sharpend)

        elif choices == "d":
            print("This is your canny edge detection image: ")
             
            cannyImg = cv2.Canny(GSimg, 60 ,150)

            cv2.imshow("canny edge detection", cannyImg)

        elif choices == "e":
            print("This is your thesh holding image: ")

            ret , thresholded_image= cv2.threshold(GSimg, 120, 255 ,cv2.THRESH_BINARY)

            cv2.imshow("Thresholded Image", thresholded_image)

        elif choices == "f":
            print("This is your Bitwise Operation image: ")

            img1 = np.zeros((300,300),dtype="uint8")
            img2 = np.zeros((300,300),dtype="uint8")

            cv2.circle (img1 ,(150,150), 50, 255, -1)
            cv2.rectangle(img2 ,(150, 150),(250,250), 255, -1)

            Bitwise_AND = cv2.bitwise_and(img1, img2,)
            Bitwise_OR = cv2.bitwise_or(img1, img2,)
            Bitwise_NOT = cv2.bitwise_not(img1)

            cv2.imshow("Circle", img1)
            cv2.imshow("Rectangle", img2)
            cv2.imshow("Bitwise_AND", Bitwise_AND)
            cv2.imshow("Bitwise_OR", Bitwise_OR)
            cv2.imshow("Bitwise_Not", Bitwise_NOT)


        else:
            print("Worng Input")

        
        cv2.imshow("orginal",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    MoreEdit= input("Want to more edit(y / n) : ") 
    if MoreEdit == "n":
        print ("\n Hope you Enjoy Editing")
        break




