#cv2 non trouvé, c'est "opencv"
import cv2

image = cv2.imread('C:\\')
cv2.imshow('Original', image)
cv2.waiKey()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)

cv2.destroyeAllWindows()
