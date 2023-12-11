import cv2
import numpy as np

img = cv2.imread('images/butter.png',1)

# print(img)

# print(type(img))
# print(img.shape)
# print(img.ndim)


# img = np.zeros((500,500,3),dtype = 'uint8')
# img = np.ones((500,500,3),dtype = 'uint8')

img = np.full((500,500,3),255,dtype = 'uint8')

# broadcating
# img[250,250] = [0,0,255]

img[::,::] = [0,0,255]
print(img)

while True:
    cv2.imshow('image',img)
    key = cv2.waitKey(50)
    if key == ord('q'):
        break


cv2.destroyAllWindows()