import cv2
import numpy as np

def nothing(x):
    pass

image = cv2.imread('image.jpg')
if image is None:
    raise ValueError("Image not found!")

cv2.namedWindow('Artistic Filters')
cv2.createTrackbar('Diameter', 'Artistic Filters', 9, 15, nothing)
cv2.createTrackbar('Sigma Color', 'Artistic Filters', 75, 150, nothing)
cv2.createTrackbar('Edge Thresh', 'Artistic Filters', 2, 10, nothing)
cv2.createTrackbar('Mode (0=Cartoon, 1=Sketch)', 'Artistic Filters', 0, 1, nothing)

while True:
    d = cv2.getTrackbarPos('Diameter', 'Artistic Filters') | 1  # Ensure odd
    sigma = cv2.getTrackbarPos('Sigma Color', 'Artistic Filters')
    edge_thresh = cv2.getTrackbarPos('Edge Thresh', 'Artistic Filters')
    mode = cv2.getTrackbarPos('Mode (0=Cartoon, 1=Sketch)', 'Artistic Filters')

    if mode == 0:
        blurred = cv2.bilateralFilter(image, d, sigma, sigma)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, edge_thresh)
        output = cv2.bitwise_and(blurred, blurred, mask=edges)
    else:
        output, _ = cv2.pencilSketch(image, sigma_s=60, sigma_r=0.07, shade_factor=0.05)

    cv2.imshow('Artistic Filters', output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
