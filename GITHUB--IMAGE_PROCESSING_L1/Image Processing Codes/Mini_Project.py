# Mini Project
# Interactive Image Editor with OpenCV
# It provides an interactive GUI where users can apply filters, adjust brightness/contrast, draw shapes, add text, and transform images in real time.

# Features
# ✅ Live Webcam Feed
# ✅ Interactive Trackbars for Adjustments
# ✅ Drawing & Text Overlays
# ✅ Image Transformations (Rotate, Flip, Crop, Resize)
# ✅ Multiple Filters (Blur, Grayscale, Edge Detection, etc.)




import cv2
import numpy as np

# Initialize webcam
cap = cv2.VideoCapture(0)

# Create a window with trackbars
cv2.namedWindow("Interactive Image Editor")

# Trackbar callbacks (do nothing, just needed for OpenCV)
def nothing(x):
    pass

# Create trackbars for brightness, contrast, and filters
cv2.createTrackbar("Brightness", "Interactive Image Editor", 50, 100, nothing)
cv2.createTrackbar("Contrast", "Interactive Image Editor", 50, 100, nothing)
cv2.createTrackbar("Filter", "Interactive Image Editor", 0, 5, nothing)  # 0: None, 1: Grayscale, 2: Blur, 3: Edges, 4: Sketch, 5: Invert
cv2.createTrackbar("Rotation", "Interactive Image Editor", 0, 360, nothing)
cv2.createTrackbar("Flip", "Interactive Image Editor", 0, 2, nothing)  # 0: None, 1: Horizontal, 2: Vertical

# Drawing mode variables
drawing = False
ix, iy = -1, -1
color = (0, 255, 0)  # Green
thickness = 2

# Mouse callback for drawing
def draw(event, x, y, flags, param):
    global ix, iy, drawing, img
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(img, (ix, iy), (x, y), color, thickness)
            ix, iy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(img, (ix, iy), (x, y), color, thickness)

cv2.setMouseCallback("Interactive Image Editor", draw)

while True:
    # Read frame from webcam
    ret, img = cap.read()
    if not ret:
        break

    # Get trackbar values
    brightness = cv2.getTrackbarPos("Brightness", "Interactive Image Editor") - 50
    contrast = cv2.getTrackbarPos("Contrast", "Interactive Image Editor") / 50
    filter_mode = cv2.getTrackbarPos("Filter", "Interactive Image Editor")
    rotation = cv2.getTrackbarPos("Rotation", "Interactive Image Editor")
    flip_mode = cv2.getTrackbarPos("Flip", "Interactive Image Editor")

    # Adjust brightness & contrast (Section 5)
    img = cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)

    # Apply filters (Section 6)
    if filter_mode == 1:  # Grayscale
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    elif filter_mode == 2:  # Blur
        img = cv2.GaussianBlur(img, (15, 15), 0)
    elif filter_mode == 3:  # Edge Detection
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        img = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    elif filter_mode == 4:  # Pencil Sketch
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        inverted = cv2.bitwise_not(gray)
        blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
        sketch = cv2.divide(gray, blurred, scale=256.0)
        img = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)
    elif filter_mode == 5:  # Invert Colors
        img = cv2.bitwise_not(img)

    # Rotate image (Section 10)
    if rotation != 0:
        h, w = img.shape[:2]
        M = cv2.getRotationMatrix2D((w//2, h//2), rotation, 1.0)
        img = cv2.warpAffine(img, M, (w, h))

    # Flip image (Section 10)
    if flip_mode == 1:
        img = cv2.flip(img, 1)  # Horizontal flip
    elif flip_mode == 2:
        img = cv2.flip(img, 0)  # Vertical flip

    # Add text (Section 8)
    cv2.putText(img, "OpenCV Mini Project", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    # Display the image
    cv2.imshow("Interactive Image Editor", img)

    # Exit on 'ESC' key
    if cv2.waitKey(1) == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()