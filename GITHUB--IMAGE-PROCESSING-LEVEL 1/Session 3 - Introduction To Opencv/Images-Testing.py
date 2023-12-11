from cv2 import cv2
import numpy 

image = cv2.imread("images\\lena.jpg",1)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()