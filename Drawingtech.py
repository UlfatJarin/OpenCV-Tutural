import cv2
image = cv2.imread("books.jpg")


#line drawing
"""
cv2.line()
cv2.line(img , pt1, p2 ,color, thickness)

pt1 = start point (x,y = (right , down))
pt2 = end point

"""
'''if image is None:
    print("Oops! Image is not working ..")
else :
    print("Image loaded successfully")

    pt1 = (50,100)
    pt2 = (300,100)
    color = (255,0,0)
    thickness = 1

    cv2.line(image, pt1 ,pt2, color, thickness)

    cv2.imshow("line",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''



#rectangle drawing....................................................
"""
cv2.rectangle(img ,pt1 .pt2, color, thickness)

pt1 = top left corner
pt2 = botom right conner

"""
'''
if image is None:
    print("Oops! Image is not working ..")
else :
    print("Image loaded successfully")

    pt2 = (50,50)
    pt1 = (250,200)
    color = (0,0, 255)
    thickness = 4

    cv2.rectangle(image , pt1, pt2, color, thickness)
    cv2.imshow("focusing Rectangle",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''


#Circle drawing..........................................................
"""
cv2.circle(img, center , radius ,color , thickness)

thickness = -1 ( color fillup)
"""
'''
if image is None:
    print("Oops! Image is not working ..")
else :
    print("Image loaded successfully")

    cv2.circle(image ,(200,150), 100 , (255, 0,0), -1)

    cv2.imshow("Image focusing Circle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''


# adding text ..........................................................
"""
cv2.putText(img , org , font, fontscale , color, thickness)

org - botom left
font - font type
fontscale - font size  -1.0 (normal)
                       -2.0(big)
"""

if image is None:
    print("Oops! Image is not working ..")
else :
    print("Image loaded successfully")

    cv2.putText(image ,"Hello python programner",(50,300), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,255) , 2)

    cv2.imshow("add Text", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


