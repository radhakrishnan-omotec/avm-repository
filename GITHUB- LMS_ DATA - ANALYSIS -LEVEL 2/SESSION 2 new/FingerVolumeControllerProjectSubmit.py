##### Import necessary libraries
import cv2
import mediapipe as mp
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np

##### Capture video from webcam
cap = cv2.VideoCapture(0)

##### Initialize MediaPipe Hands
mpHands = mp.solutions.hands
hands = mpHands.Hands()
##### Initialize MediaPipe Drawing Utilities
mpDraw = mp.solutions.drawing_utils

### Python code To access speaker through the library pycaw
##### Access speaker through the library pycaw
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

##### Set initial volume bar position and percentage
volbar = 400
volper = 0


volMin, volMax = volume.GetVolumeRange()[:2]
    
    
while True:
  success, img = cap.read()

  imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

  ### Python code to Collection of gesture information
  results = hands.process(imgRGB)

  lmList = []
  ##### If hands are detected
  if results.multi_hand_landmarks:
    ##### Iterate over all detected hands
    for handlandmark in results.multi_hand_landmarks:
      ##### Iterate over all landmarks in the hand
      for id, lm in enumerate(handlandmark.landmark):
        ### Python code to Get finger joint points
        h, w, _ = img.shape
        cx, cy = int(lm.x * w), int(lm.y * h)
        ##### Add landmark to list
        lmList.append([id, cx, cy])
      ##### Draw landmarks on image
      mpDraw.draw_landmarks(img, handlandmark, mpHands.HAND_CONNECTIONS)

 
    ##### If any landmarks were found
    if lmList != []:
        ##### Get coordinates of palm base and index finger tip
        #getting the value at a point
                        #x      #y
        x1,y1 = lmList[0][1],lmList[0][2]  #palm
        x2,y2 = lmList[8][1],lmList[8][2]  #index finger
        
        ### Python code to creating circle at the tips of thumb and index finger
        cv2.circle(img,(x1,y1),13,(0,0,255),cv2.FILLED) #image #fingers #radius #rgb
        cv2.circle(img,(x2,y2),13,(255,0,0),cv2.FILLED) #image #fingers #radius #rgb
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),3)  #create a line b/w tips of index finger and thumb
        
        ### Python code to add a LIGHT BLUE box for INDEX FINGER MEDIAPIPE hand landmarks +8
        # Get the index finger landmark.
        index_finger_landmark = lmList[8]

        ### Python code to Calculate the top-left and bottom-right coordinates of the box.
        box_top_left = (index_finger_landmark[1] - 10, index_finger_landmark[2] - 10)
        box_bottom_right = (index_finger_landmark[1] + 10, index_finger_landmark[2] + 10)

        # Draw the box.
        cv2.rectangle(img, box_top_left, box_bottom_right, (255, 255, 0), 2)
  
  
  
        ### Python code to Calculate the distance between palm base and index finger tip.
        length = hypot(x2-x1,y2-y1) #distance b/w tips using hypotenuse
        # from numpy we find our length,by converting hand range in terms of volume range ie b/w -63.5 to 0
        vol = np.interp(length,[30,350],[volMin,volMax]) 
        volbar=np.interp(length,[30,350],[400,150])
        volper=np.interp(length,[30,350],[0,100])
        
        
        
        # Python code to display_vol_in_reverse(vol)
        # Convert the values in the array to a range of 0 to 100, with 0 displayed as 100, 1 as 99, etc. till 100 as 0.
        # Convert the input from negative to positive and positive to negative.
        vols = -np.abs(vol)
        vols = (100 + vols)
        print("Volume => ",vols, " Length => ",int(length))
        volume.SetMasterVolumeLevel(vol, None)
        
        
        
        
        
        # Hand range 30 - 350
        # Volume range -63.5 - 0.0
        ### Python code to creating volume bar for volume level 
        cv2.rectangle(img,(50,150),(85,400),(0,0,255),4) # vid ,initial position ,ending position ,rgb ,thickness
        cv2.rectangle(img,(50,int(volbar)),(85,400),(0,0,255),cv2.FILLED)
        #RK cv2.putText(img,f"{int(volper)}%",(10,100),cv2.FONT_ITALIC,1,(0, 255, 98),3)
        cv2.putText(img,f"Volume Level : {int(vols)}",(10,40),cv2.FONT_ITALIC,1,(255, 0, 0),3)
        
        ### Python code to tell the volume percentage ,location,font of text,length,rgb color,thickness
    cv2.imshow('Image',img) #Show the video 
    if cv2.waitKey(1) & 0xff==ord(' '): #By using spacebar delay will stop
        break
        
        
        
        
cap.release()     #stop cam       
cv2.destroyAllWindows() #close window