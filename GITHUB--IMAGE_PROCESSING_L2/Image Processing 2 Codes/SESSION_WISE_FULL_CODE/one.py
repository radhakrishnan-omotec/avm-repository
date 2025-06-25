import cv2
import numpy as np

def adjust_brightness(value):
    """Callback function for trackbar to adjust brightness"""
    global gray_image, brightness
    brightness = value - 100  # Center at 0 (range: -100 to +100)
    adjusted = np.clip(gray_image.astype(np.int16) + brightness, 0, 255).astype(np.uint8)
    cv2.imshow('Brightness Control', adjusted)

# Load image and convert to grayscale
image = cv2.imread('input.jpg')  # Replace with your image path
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a window with a trackbar
cv2.namedWindow('Brightness Control')
cv2.createTrackbar('Brightness', 'Brightness Control', 100, 200, adjust_brightness)  # Default: 100 (brightness=0)

# Initial display
cv2.imshow('Brightness Control', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()