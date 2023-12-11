import cv2

img = cv2.imread(r"C:\Users\OMOLP091\Documents\OMOTECH\SESSION-1-STUD\IMAGE-LEVEL-2\Session 3\images\girlImage.jpg", 0)
rows,cols = img.shape
M = cv2.getRotationMatrix2D((cols/2,rows/2),270,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()