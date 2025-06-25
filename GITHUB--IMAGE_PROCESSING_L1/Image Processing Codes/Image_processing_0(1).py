import numpy as np
import cv2

img = np.zeros((512, 512, 3), dtype = np.uint8)  #Create a black image zero means 0 for all BGR

cv2.imshow("Window", img) # Show the window
cv2.waitKey(0)  # holds the window 
cv2.destroyAllWindows()  # close the window properly
