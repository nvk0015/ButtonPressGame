from cvzone.HandTrackingModule import HandDetector
import cv2
import math
import cvzone
import numpy as np


#Setup Webcam
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

#Initialize the Hand detector
detector = HandDetector(detectionCon=0.7,maxHands=1)


#Variables
firstHand = 0
secondHand = 1
INDEX_FINGER_MCP = 5
PINKY_MCP = 17
Rawvalues = [300,245,200,170,145,130,112,103,93,87,80,75,70,67,62,59,57]
measuredValues = [20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]

#Game variables
circleColor = (255,0,255)
cx,cy = 100,100 #circle position
#Data relation
coff = np.polyfit(Rawvalues,measuredValues,deg=2)


#display image
while True:
    #read image
    success, img = cap.read()
    #recognize the hands
    hands= detector.findHands(img,draw=False)

    #if any hand is detected
    if hands:
        #extract the landmarks of detected hand to a list
        lmList = hands[firstHand]['lmList']
        #return the bounding box values of first hand
        x,y,w,h = hands[firstHand]['bbox']
        x1,y1 = lmList[INDEX_FINGER_MCP]
        x2,y2 = lmList[PINKY_MCP]

        distance = math.sqrt((y2-y1)**2+(x2-x1)**2)
        A,B,C = coff
        distanceCM = A*distance**2+B*distance+C
        if distanceCM<50:
            if x<cx<cx+w and y<cx<cy+h:
                circleColor=(0,255,0)
        else:
            circleColor=(255,0,255)
        #draw rectangle around the hand
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)    
        #draw the distance box on image
        cvzone.putTextRect(img,f'{int(distanceCM)} cm',(x+5,y-10))


    #Draw Button on the image
    cv2.circle(img,(cx,cy),30,circleColor,cv2.FILLED)
    cv2.circle(img,(cx,cy),20,(255,255,255),2)
    cv2.circle(img,(cx,cy),10,(255,255,255),cv2.FILLED)
    cv2.circle(img,(cx,cy),30,(50,50,50),2)


    # Game HUD
    cvzone.putTextRect(img,"Time: 30",(1000,75),scale=3,offset=20)
    cvzone.putTextRect(img,"Score: 04", (75,75),scale=3,offset=20)


    cv2.imshow("Image",img)

    key = cv2.waitKey(1)
    if key == ord('r'):
        break
cv2.destroyAllWindows()