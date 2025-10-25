#
"""
contours  = carves , continious curve , point or eages then connect each other
#contours , hierarchy =cv2.findContours(image , mode, method)
     binary image = black& white image
                    can be used canny method
     mode = retrivle mode  - how many & what kind of contorcs returens 
                           
          * 1.RETR_TREE     -- all shapes outer inner
          * 2.RETR_EXIEROAL -- outermost shapes
            3.RETR_LIST     -- all contorus without hierarchy

     method =approximate result , how much details to return for each coutours
        -- CHAIN_APPROX_SIMPLE
           

  contours= list of all points ditect in a shape
  hirerarchy = contours all information/ relationship between (parents to child)

  ***
   ""_"" = means a placeholder , we know there will a varable but we dont care about it right now
      -- clear code 
      -- memory doesnot weaste
      -- professional way

"""

import cv2

img = cv2.imread("triangle.png")
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
_ , thresh = cv2.threshold (gray, 200 , 255 , cv2.THRESH_BINARY)

#Find CONTOURS

contours , heirarchy = cv2. findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

"""
cv2.drawContours()
cv2.drawContours(image, contours, contour_index , color ,thickness )
--  draw contours in orginal image with color and thickness
      -contours_index -  0 - only first shape 
                      -  1 - 2nd shape
                      - -1 - all shapes (commonly used)
"""
cv2.drawContours(img , contours , -1 ,(0, 255, 0) , 3)

cv2.imshow("Contours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()





#SHAPE DETACTS ....................................................................................
"""
give shape - nams the shape name 
#ApproxPolyDP() function - 
  detact shapes but counting their corners 

approx = cv2.approxPolyDP(contour, epsilon ,True)
        contour - shape outline 
        epsilon = 0.01 * cv2.ARCLength (contors , boolien value)
             0.01 - epsilon   - close to orginal shape

             |  shape           |  ARCLength  |  epsilon(0.01 * X) [/0.02/0.03]
             | small triangle   |   200px     |  2.0 px
             | large rectangle  |   800px     |  8.0 px
             | Big Circle       |   1200px    |  12.0 px


           - how close to match orginal one 
           --smaller - more presize , more points 
           --larger  - roufer , fewer points

total length = arclength / area / porishima 

true - closed  fig       - start connent with end 
false - open space in fig

"""

img = cv2.imread("hexagon.png")
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
_ , thresh = cv2.threshold (gray, 200 , 255 , cv2.THRESH_BINARY)

contours , heirarchy = cv2. findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img , contours , -1 ,(0, 255, 0) , 3)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour,True), True)

    corner = len(approx)

    if corner == 3 :
        shape_name = "Triangle"
    elif corner == 4 :
        shape_name = "Rectangle"
    elif corner == 5 :
        shape_name = "pentagon"
    elif corner == 6 :
        shape_name = "hexagon"
    elif corner == 7 :
        shape_name = "heptagon"
    elif corner >= 8 :
        shape_name = "Circle"
    else:
        shape_name ="unknown"

    cv2.drawContours(img ,[approx], 0 , (0,255,0) , 2 )  # 0 = work in first image
    x = approx.ravel()[0]            #ravel = mintidimention to 1d array
    y = approx.ravel()[1] + 10     # -10 = so that text visible upper ,, so that it can be clearly visible
    cv2.putText(img ,shape_name,(x,y), cv2.FONT_HERSHEY_COMPLEX , 0.6 , (255,0,0) , 2)


cv2.imshow("Contours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


