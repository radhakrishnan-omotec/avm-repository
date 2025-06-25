import cv2
import numpy as np
from utils import *

def main():
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Set webcam resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Initialize background subtractor for motion detection
    bg_subtractor = cv2.createBackgroundSubtractorMOG2()

    # Define color range for object tracking (blue color in this example)
    hsv_lower = np.array([100, 100, 100])
    hsv_upper = np.array([140, 255, 255])

    # Available processing modes
    modes = [
        "original", 
        "perspective", 
        "threshold", 
        "edge", 
        "contour", 
        "shape", 
        "face", 
        "motion", 
        "tracking", 
        "cartoon", 
        "sketch"
    ]
    current_mode = 0

    print("""
    SmartVision Analyzer - Real-Time Mode
    Press:
    - 'M' to cycle through processing modes
    - 'Q' to quit
    """)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Flip frame horizontally for mirror effect
        frame = cv2.flip(frame, 1)

        # Get current mode
        mode = modes[current_mode]

        # Process frame based on selected mode
        if mode == "original":
            processed = frame.copy()
        elif mode == "perspective":
            processed = perspective_transform(frame)
        elif mode == "threshold":
            processed = adaptive_threshold(frame)
            processed = cv2.cvtColor(processed, cv2.COLOR_GRAY2BGR)
        elif mode == "edge":
            processed = canny_edge_detection(frame)
            processed = cv2.cvtColor(processed, cv2.COLOR_GRAY2BGR)
        elif mode == "contour":
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            binary = adaptive_threshold(gray)
            contours = detect_contours(binary)
            processed = draw_contours(frame.copy(), contours)
        elif mode == "shape":
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            binary = adaptive_threshold(gray)
            contours = detect_contours(binary)
            processed = detect_shapes(frame.copy(), contours)
        elif mode == "face":
            processed = detect_faces(frame.copy())
        elif mode == "motion":
            processed = detect_motion(frame.copy(), bg_subtractor)
        elif mode == "tracking":
            processed = track_color_object(frame.copy(), hsv_lower, hsv_upper)
        elif mode == "cartoon":
            processed = apply_cartoon_effect(frame)
        elif mode == "sketch":
            processed = apply_pencil_sketch(frame)

        # Display active mode and instructions
        cv2.putText(processed, f"Mode: {mode}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.putText(processed, "Press 'M' to change mode", (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 1)
        cv2.putText(processed, "Press 'Q' to quit", (10, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)

        # Show processed frame
        cv2.imshow("SmartVision Analyzer", processed)

        # Key controls
        key = cv2.waitKey(1) & 0xFF
        if key == ord('m') or key == ord('M'):
            current_mode = (current_mode + 1) % len(modes)
        elif key == ord('q') or key == ord('Q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()