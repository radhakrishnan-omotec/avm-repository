#DA2
'''
import cv2

# Read an image
img = cv2.imread('C:\\Users\\OMOTEC041\\Desktop\\Doctor-Strange-Filter-main\\Models\\inner_circles\\orange.png')

# Define the region of interest (ROI) for cropping
x, y, width, height = 100, 100, 200, 200
roi = img[y:y+height, x:x+width]

# Display the cropped image
cv2.imshow('cropped', roi)

# Wait for a key event to close the window
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()

import cv2

# Read an image
img = cv2.imread('C:\\Users\\OMOTEC041\\Desktop\\Doctor-Strange-Filter-main\\Models\\inner_circles\\orange.png')

start_x = 100
start_y = 100
end_x = 200
end_y = 200
center_x = 100
center_y = 100
radius = 50
thickness = 10
x=100
y=100
width=200
height=200

# Draw a line on the image
cv2.line(img, (start_x, start_y), (end_x, end_y), (255, 0, 0), thickness)

# Draw a rectangle on the image
cv2.rectangle(img, (x, y), (x+width, y+height), (0, 255, 0), thickness)

# Draw a circle on the image
cv2.circle(img, (center_x, center_y), radius, (0, 0, 255), thickness)

# Display the image with the shapes drawn on it
cv2.imshow('image', img)

# Wait for a key event to close the window
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()


import cv2

# Read an image
img = cv2.imread('C:\\Users\\OMOTEC041\\Desktop\\Doctor-Strange-Filter-main\\Models\\inner_circles\\orange.png')

# Get the dimensions of the image
height, width, channels = img.shape
print('Image dimensions: {}x{} with {} channels'.format(width, height, channels))

import cv2
import numpy as np

# Load an image from file
img = cv2.imread("C:\\Users\\OMOTEC041\\Pictures\\istockphoto-125141307-612x612.jpg")

# Rotate the image
rows, cols, _ = img.shape
M = cv2.getRotationMatrix2D((cols/2, rows/2), -45, 1)
rotated_img = cv2.warpAffine(img, M, (cols, rows))

# Apply a perspective transform 
pts1 = np.float32([[200,100],[368,52],[50,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,400]])
M = cv2.getPerspectiveTransform(pts1,pts2)
transformed_img = cv2.warpPerspective(img,M,(300,300))

# Adjust the brightness and contrast
alpha = 10
beta = 20
adjusted_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

# Display the images on screen
cv2.imshow('Original Image', img)
cv2.imshow('Rotated Image', rotated_img)
cv2.imshow('Transformed Image', transformed_img)
cv2.imshow('Adjusted Image', adjusted_img)

# Wait for a key press
cv2.waitKey(0)

# Close the windows
cv2.destroyAllWindows()


import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread('C:\\Users\\OMOTEC041\\Pictures\\istockphoto-147290529-612x612.jpg', cv2.IMREAD_GRAYSCALE)

# Perform contrast stretching
normalized_img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

# Display images
cv2.imshow('Original', img)
cv2.imshow('Normalized', normalized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()



import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread('C:\\Users\\OMOTEC041\\Pictures\\istockphoto-147290529-612x612.jpg', 0)

# Perform contrast stretching
normalized_img = cv2.normalize(img, None, 0, 100, cv2.NORM_MINMAX)

# Display images
cv2.imshow('Original', img)
cv2.imshow('Normalized', normalized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2

# Read image
img = cv2.imread('C:\\Users\\OMOTEC041\\Pictures\\istockphoto-147290529-612x612.jpg')

# Perform Gaussian blur
blurred_img = cv2.GaussianBlur(img,(3,3),0)

# Display images
cv2.imshow('Original', img)
cv2.imshow('Blurred', blurred_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

# Read image in grayscale
img = cv2.imread('C:\\Users\\OMOTEC041\\Pictures\\istockphoto-147290529-612x612.jpg', cv2.IMREAD_GRAYSCALE)

# Perform thresholding
threshold_value = 127
max_value = 255
ret, thresholded_img = cv2.threshold(img, threshold_value, max_value, cv2.THRESH_BINARY)

# Display images
cv2.imshow('Original', img)
cv2.imshow('Thresholded', thresholded_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2

# Read image
img = cv2.imread('C:\\Users\\OMOTEC041\\Pictures\\istockphoto-147290529-612x612.jpg')

# Save image in JPEG format
cv2.imwrite('C:\\Users\\OMOTEC041\\Pictures\\compressed_image.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])


import cv2

# Read image
img = cv2.imread("C:\\Users\\OMOTEC041\\Pictures\\Screenshot 2023-10-17 111718.png")

# Save image in PNG format
cv2.imwrite('C:\\Users\\OMOTEC041\\Pictures\\Screenshot2023-10-17 111718compressed_image.png', img, [cv2.IMWRITE_PNG_COMPRESSION,50])


import cv2
import numpy as np

# Load the image
img = cv2.imread('C:\\Users\\OMOTEC041\\Pictures\\Screenshot 2023-10-17 111718.png')

# Define the kernel for the filter
kernel = np.ones((5,5), np.float32)/25

# Apply the filter to the image
filtered_img = cv2.filter2D(img, -1, kernel)

# Display the original and filtered image
cv2.imshow('Original Image', img)
cv2.imshow('Filtered Image', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
import numpy as np

# Load the images
img1 = cv2.imread("C:\\Users\\OMOTEC041\\Pictures\\istockphoto-125141307-612x612.jpg")
img2 = cv2.imread("C:\\Users\\OMOTEC041\\Pictures\\id-photo2.jpg")

# Resize the images to the same size
img1 = cv2.resize(img1, (640, 480))
img2 = cv2.resize(img2, (640, 480))

# Create a mask for blending
mask = np.zeros_like(img1)
mask[200:400, 200:400] = 255

# Apply the mask to the images
masked_img1 = cv2.bitwise_and(img1, mask)
masked_img2 = cv2.bitwise_and(img2, cv2.bitwise_not(mask))

# Blend the images using addWeighted function
blended_img = cv2.addWeighted(masked_img1, 0.2, masked_img2, 0.2, 0)

# Display the images
cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.imshow('Mask', mask)
cv2.imshow('Blended Image', blended_img)
cv2.imshow("masked1",masked_img1)
cv2.imshow("masked2",masked_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

# Load the image in BGR format
image_bgr = cv2.imread("C:\\Users\\OMOTEC041\\Pictures\\istockphoto-125141307-612x612.jpg")

# Convert BGR to Gray
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

# Display the images
cv2.imshow('BGR Image', image_bgr)
cv2.imshow('Gray Image', image_gray)
cv2.waitKey(0)



import cv2
import numpy as np

# Load the image
image = cv2.imread("C:\\Users\\OMOTEC041\\Pictures\\istockphoto-125141307-612x612.jpg")

# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the range of red color in HSV
lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])
mask1 = cv2.inRange(hsv, lower_red, upper_red)

lower_red = np.array([170,50,50])
upper_red = np.array([180,255,255])
mask2 = cv2.inRange(hsv, lower_red, upper_red)

# Combine the masks
mask = mask1 + mask2

# Apply the mask to the image
result = cv2.bitwise_and(image, image, mask=mask)

# Display the images
cv2.imshow('Original Image', image)
cv2.imshow('Mask', mask)
cv2.imshow('Result', result)
cv2.waitKey(0)


import cv2
import numpy as np

# Load the image
img = cv2.imread("C:\\Users\\OMOTEC041\\Pictures\\istockphoto-125141307-612x612.jpg")
# Convert the image to LAB color space
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# Split the LAB color space into its 3 channels: L, a, and b
l, a, b = cv2.split(lab)

# Apply CLAHE to the L channel of the LAB color space
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
l_clahe = clahe.apply(l)

# Merge the L, a, and b channels back into a single image
lab_clahe = cv2.merge((l_clahe, a, b))

# Convert the image back to the original color space
color_corrected_img = cv2.cvtColor(lab_clahe, cv2.COLOR_LAB2BGR)

# Display the original image and the color-corrected image side by side
cv2.imshow('Original Image', img)
cv2.imshow('Color-Corrected Image', color_corrected_img)
cv2.imshow('Original Imagecs', lab_clahe)
cv2.waitKey(0)
cv2.destroyAllWindows()



import numpy as np
import cv2

# Load image
img = cv2.imread('C:\\Users\\OMOTEC041\\Pictures\\istockphoto-125141307-612x612.jpg')

# Define font and text to add
font = cv2.FONT_HERSHEY_SIMPLEX
text = 'kyaa be'

# Get text size
text_size, _ = cv2.getTextSize(text, font,1,1)

# Calculate text position
text_x = int((img.shape[1] - text_size[0]) / 2)
text_y = int((img.shape[0] + text_size[1]) / 2)

# Add text to image
cv2.putText(img, text, (text_x, text_y), font, 3, (0,0,0), 2, cv2.LINE_AA)

# Display image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


import numpy as np
import cv2

# Load image
img = cv2.imread('C:\\Users\\OMOTEC041\\Pictures\\istockphoto-125141307-612x612.jpg')

# Define font and text to add
font = cv2.FONT_HERSHEY_SIMPLEX
text = 'kyaa be'

# Get image dimensions
img_height, img_width, _ = img.shape

# Calculate text position at the center
text_x = int(img_width / 2 - len(text)*10)  # Adjust factor based on font and desired spacing
text_y = int(img_height / 2)

# Add text to image
cv2.putText(img, text, (text_x, text_y), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

# Display image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



import cv2
import mediapipe as mp

# Load the Mediapipe hand landmark model
mp_hands = mp.solutions.hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

# Initialize the video capture object
cap = cv2.VideoCapture(0)

while True:
    # Read a new frame from the video capture object
    ret, frame = cap.read()

    # Convert the color space from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect the hand landmarks in the current frame
    results = mp_hands.process(frame)

    # Draw the hand landmarks on the current frame
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp.drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display the current frame in a window
    cv2.imshow('Hand Landmarks', frame)

    # Check for a key event and exit if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture object and destroy all windows
cap.release()
cv2.destroyAllWindows()
'''



import cv2
import mediapipe as mp

# Initialize the MediaPipe face detection module
mp_face_detection = mp.solutions.face_detection

# Initialize the MediaPipe drawing module
mp_draw = mp.solutions.drawing_utils

# Initialize the VideoCapture object
cap = cv2.VideoCapture(0)

# Loop over the frames
while True:
    # Read the frame from the camera
    success, img = cap.read()
    if not success:
        break

    # Convert the image to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Detect faces in the image
    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
        results = face_detection.process(img_rgb)
        if results.detections:
            for detection in results.detections:
                # Draw the bounding box around the face
                mp_draw.draw_detection(img, detection)

    # Display the image
    cv2.imshow("Face Detection", img)

    # Wait for a key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and destroy the windows
cap.release()
cv2.destroyAllWindows()


