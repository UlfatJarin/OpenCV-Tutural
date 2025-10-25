#find  basic  obijects shape 

import cv2 


img = cv2.imread(input(" Image  of an object : " ))
gray = cv2.cvtColor(img , cv2.COLOR_RGB2GRAY)
_ , threshold = cv2.threshold(gray, 200, 255 , cv2.THRESH_BINARY)
MedianBlur = cv2.medianBlur(threshold,3)

contours , heirarchy =cv2.findContours(MedianBlur,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img , contours , -1 , (0, 255 ,0) ,2)

for contour in contours :
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour,True) , True)

    corner = len(approx)

    if corner == 3 :
        shape_name  = "Triangle"
    elif corner == 4 :
        shape_name  = "rectangle"
    elif corner == 5 :
        shape_name  = "pentagon"
    elif corner == 6 :
        shape_name  = "hexagon"
    elif corner == 7 :
        shape_name  = "heptagon"
    elif corner > 7 :
        shape_name  = "circle"
    else:
        shape_name : "unknown"
    
    cv2.drawContours(img , [approx] , 0 ,(0,255,0), 2)
    x= approx.ravel()[0]
    y= approx.ravel()[1]
    cv2.putText(img, shape_name ,(x,y) ,cv2.FONT_HERSHEY_COMPLEX , 0.6 ,(155,155,155), 2)
    


cv2.imshow("MedianBlur", MedianBlur)

cv2.imshow("contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

