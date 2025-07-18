import cv2
import numpy as np
import imutils
from skimage.filters import threshold_local
from scipy.spatial import distance as dist

def order_points(pts):
    # Initialize a list of coordinates that will be ordered
    rect = np.zeros((4, 2), dtype="float32")
    
    # Sum the x + y coordinates to find top-left (smallest sum) and bottom-right (largest sum)
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]  # Top-left
    rect[2] = pts[np.argmax(s)]  # Bottom-right
    
    # Compute the difference between x and y to find top-right (smallest diff) and bottom-left (largest diff)
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]  # Top-right
    rect[3] = pts[np.argmax(diff)]  # Bottom-left
    
    return rect

def perspective_transform(image, pts, ratio):
    # Order the points
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
    
    # Compute the width of the new image
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    
    # Compute the height of the new image
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    
    # Define the destination points for the perspective transform
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")
    
    # Compute the perspective transform matrix and apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    
    return warped

# Step 1: Load and resize the input image
image_path = 'images/sample.jpg'
original_img = cv2.imread(image_path)
copy = original_img.copy()  # Create a copy for later use
ratio = original_img.shape[0] / 500.0  # Calculate ratio to maintain aspect ratio
img_resize = imutils.resize(original_img, height=500)  # Resize image to height of 500 pixels

# Step 2: Convert to grayscale
gray_image = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray_image)
cv2.waitKey(0)

# Step 3: Apply Gaussian blur and edge detection
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
edged_image = cv2.Canny(blurred_image, 75, 200)
cv2.imshow("Edged Image", edged_image)
cv2.waitKey(0)

# Step 4: Find contours and identify the document
cnts = cv2.findContours(edged_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]  # Handle OpenCV version differences
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]  # Keep top 5 largest contours

doc = None
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    if len(approx) == 4:  # Look for a quadrilateral
        doc = approx
        break

# Step 5: Visualize the detected corners
if doc is not None:
    points = []
    for point in doc:
        tuple_point = tuple(point[0])
        cv2.circle(img_resize, tuple_point, 5, (0, 0, 255), -1)  # Draw red circles at corners
        points.append(tuple_point)
    cv2.imshow("Corner Points", img_resize)
    cv2.waitKey(0)

    # Step 6: Apply perspective transform
    warped_image = perspective_transform(original_img, doc.reshape(4, 2), ratio)
    
    # Step 7: Convert to grayscale and apply adaptive thresholding
    warped_gray = cv2.cvtColor(warped_image, cv2.COLOR_BGR2GRAY)
    warped_threshold = threshold_local(warped_gray, 11, offset=10, method="gaussian")
    warped_image = (warped_gray > warped_threshold).astype("uint8") * 255
    
    # Display the final scanned document
    cv2.imshow("Scanned Document", warped_image)
    cv2.waitKey(0)

cv2.destroyAllWindows()