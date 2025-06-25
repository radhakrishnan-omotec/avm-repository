import cv2
import numpy as np

cap = cv2.VideoCapture('video.mp4')
if not cap.isOpened():
    raise ValueError("Video not found!")
ret, frame = cap.read()
if not ret:
    raise ValueError("Cannot read video!")

roi_box = cv2.selectROI("Select ROI", frame, fromCenter=False)
roi = frame[int(roi_box[1]):int(roi_box[1]+roi_box[3]), int(roi_box[0]):int(roi_box[0]+roi_box[2])]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi], [0, 1], None, [180, 256], [0, 180, 0, 256])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst = cv2.calcBackProject([hsv], [0, 1], roi_hist, [0, 180, 0, 256], 1)
    _, mask = cv2.threshold(dst, 50, 255, cv2.THRESH_BINARY)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        c = max(contours, key=cv2.contourArea)
        if cv2.contourArea(c) > 500:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('Object Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
