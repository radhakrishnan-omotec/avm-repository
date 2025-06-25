import numpy as np
import cv2

# Function to create a black-and-white pixel grid
def create_grid(rows=10, cols=10, size=20):
    # Create a white background grid
    grid = np.ones((rows*size, cols*size), dtype=np.uint8) * 255
    
    # Fill alternating squares with black to create a checkerboard pattern
    for i in range(rows):
        for j in range(cols):
            if (i+j) % 2 == 0:  # Alternate black and white squares
                grid[i*size:(i+1)*size, j*size:(j+1)*size] = 0
    
    return grid

# Display the generated grid using OpenCV
cv2.imshow('Grid', create_grid())
cv2.waitKey(0)
cv2.destroyAllWindows()
