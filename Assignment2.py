# import
import cv2

#take a file input 
image = cv2.imread(input("Image file Name/path Name : "))

while True:
    if image is not None:
        draw =input("Want to draw? (line-l /circle-c /rectangle-r /text-t) : ").lower()
        if draw == 'l':
            pt1 = (input("start point?(x,y) : "))
            pt2 = (input("end point?(x,y) : ") )
            x1, y1 = map(int, pt1.strip('()').split(','))
            x2, y2 = map(int, pt2.strip('()').split(','))
            thickness =int(input("thickness? : "))
            cv2.line(image ,(x1,y1) , (x2,y2), (255,0,0) , thickness)
        elif draw == 'c':
            center = input("center point?(x,y) : ")
            x,y = map(int, center.strip('()').split(','))
            radius = int(input("Radius point?   : "))
            thickness =int(input("thickness? : "))
            cv2.circle(image, (x,y) , radius , (0,255,0), thickness)
        elif draw == 'r':
            pt1 = input("start point?(top-left)(x,y): ")
            pt2 = input("End point?(botom-right)(x,y)  : ")
            x1, y1 = map(int , pt1.strip('()').split(','))
            x2, y2 = map(int , pt2.strip('()').split(','))
            thickness =int(input("thickness? : "))
            cv2.rectangle(image , (x1,y1) , (x2, y2) , (0,0,255) , thickness)
        elif draw == 't':
            org = input("start point?(x,y) : ")
            x , y = map(int ,org.strip('()').split(','))
            thickness =int(input("thickness? : "))
            cv2.putText(image, "Find the Coffee MUG." , (x,y) , cv2.FONT_HERSHEY_SCRIPT_SIMPLEX , 1.5 , (155,155,155),thickness)
        else:
            print("Worng Input.. ")
            


        cv2.imshow("Image",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        save= input("what to save the image?(yes /no) : ")
        if save == "yes":
            cv2.imwrite(f'{input("file_name : ")}.jpg',image )
            if save :
                print("Image save successfully")
            else:
                print("Image cannot be saved")



    else: 
        print("Oops! Image cannot be loaded!")

    more = input("What to draw more?(yes?no)").lower()
    if more == 'no':
        print("Thanks to draw")
        break

    







# ask what to do _ line _ circle _rectangle _text 
#  save or no ?
                 