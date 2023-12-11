import cv2
import numpy as np
img = cv2.imread(r"C:\Users\OMOLP091\Documents\OMOTECH\SESSION-1-STUD\IMAGE-LEVEL-2\Session 3\images\girlImage.jpg", 1)
rows,cols,dim = img.shape
M = np.float32([[1,0,100],[0,1,150]])
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()