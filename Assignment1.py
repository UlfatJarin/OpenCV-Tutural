import cv2

# imgae load
img =input("Enter File name : ")
image = cv2.imread(img)
# grayscale 
if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # show 
    show = input("DO you want to Display?(yes/no) : ").lower()
    if show == 'yes':
        cv2.imshow("GrayScale Image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    # save 
    save = input("DO you want to save the Image?(yes/no) : ").lower()
    if  save =='yes':
        file_name = input("File name to save the image: ")
        success = cv2.imwrite(f'{file_name}.jpg',gray)
        if success :
            print("image saved Successfully")
        else:
            print("Failed to save")
else:
    print ("couldnot load the image") 

  # take filenaem 
  # return a masssage
