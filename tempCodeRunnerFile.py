

blurred = cv2.GaussianBlur(image ,(7,7), 3)

cv2.imshow("Orginal image",image)
cv2.imshow("Blurred image",blurred)