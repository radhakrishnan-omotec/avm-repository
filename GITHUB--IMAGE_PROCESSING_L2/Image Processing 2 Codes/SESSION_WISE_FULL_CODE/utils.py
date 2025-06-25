import cv2
import numpy as np

# --------------------------
# 1. Advanced Transformations
# --------------------------
def perspective_transform(img, pts_src=None):
    """Applies perspective transformation to an image"""
    if pts_src is None:
        h, w = img.shape[:2]
        pts_src = np.float32([[0, 0], [w, 0], [w, h], [0, h]])
        pts_dst = np.float32([[w*0.1, h*0.1], [w*0.9, h*0.2], 
                             [w*0.8, h*0.9], [w*0.2, h*0.8]])
    
    matrix = cv2.getPerspectiveTransform(pts_src, pts_dst)
    result = cv2.warpPerspective(img, matrix, (w, h))
    return result

# --------------------------
# 2. Thresholding & Segmentation
# --------------------------
def adaptive_threshold(img):
    """Applies adaptive thresholding"""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                               cv2.THRESH_BINARY, 11, 2)

# --------------------------
# 3. Edge Detection
# --------------------------
def canny_edge_detection(img, low=50, high=150):
    """Applies Canny edge detection"""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    return cv2.Canny(blurred, low, high)

# --------------------------
# 4. Contour Detection
# --------------------------
def detect_contours(binary_img):
    """Finds contours in a binary image"""
    contours, _ = cv2.findContours(binary_img, cv2.RETR_TREE, 
                                  cv2.CHAIN_APPROX_SIMPLE)
    return contours

def draw_contours(img, contours):
    """Draws contours on an image"""
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
    return img

# --------------------------
# 5. Shape Detection
# --------------------------
def detect_shapes(img, contours):
    """Detects and labels shapes in an image"""
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        x, y, w, h = cv2.boundingRect(approx)
        
        if len(approx) == 3:
            shape = "Triangle"
        elif len(approx) == 4:
            aspect_ratio = float(w)/h
            shape = "Square" if 0.95 <= aspect_ratio <= 1.05 else "Rectangle"
        else:
            shape = "Circle"
        
        cv2.putText(img, shape, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 
                   0.5, (0, 255, 0), 2)
    return img

# --------------------------
# 6. Histogram Analysis
# --------------------------
def compute_histogram(img):
    """Computes and displays color histogram"""
    colors = ('b', 'g', 'r')
    for i, color in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
    plt.title('Color Histogram')
    plt.show()
    return img

# --------------------------
# 7. Motion Detection
# --------------------------
def detect_motion(frame, bg_subtractor):
    """Detects motion using background subtraction"""
    fg_mask = bg_subtractor.apply(frame)
    _, motion_mask = cv2.threshold(fg_mask, 250, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(motion_mask, cv2.RETR_EXTERNAL, 
                                 cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        if cv2.contourArea(cnt) > 500:  # Filter small contours
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    return frame

# --------------------------
# 8. Face Detection
# --------------------------
def detect_faces(img):
    """Detects faces using Haar Cascade"""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    return img

# --------------------------
# 9. Object Tracking (Color-based)
# --------------------------
def track_color_object(frame, hsv_lower, hsv_upper):
    """Tracks colored objects using HSV color space"""
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, hsv_lower, hsv_upper)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, 
                                 cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        if cv2.contourArea(cnt) > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
    
    return frame

# --------------------------
# 10. Artistic Filters
# --------------------------
def apply_cartoon_effect(img):
    """Applies cartoon effect to an image"""
    # Convert to grayscale and apply median blur
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    
    # Detect edges using adaptive threshold
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                 cv2.THRESH_BINARY, 9, 9)
    
    # Apply bilateral filter for color smoothing
    color = cv2.bilateralFilter(img, 9, 300, 300)
    
    # Combine edges with color image
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

def apply_pencil_sketch(img):
    """Converts image to pencil sketch"""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted = 255 - gray
    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
    inverted_blurred = 255 - blurred
    sketch = cv2.divide(gray, inverted_blurred, scale=256.0)
    return cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)