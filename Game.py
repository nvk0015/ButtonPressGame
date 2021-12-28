from cvzone.HandTrackingModule import HandDetector
import cv2
import math
import cvzone
import numpy as np
import time


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
counter = 0
score = 0
startTime = time.time()
gameTime = 10

#Data relation
coff = np.polyfit(Rawvalues,measuredValues,deg=2)

#display image
while True:
    #read image
    success, img = cap.read()
    img = cv2.flip(img,1)

    if time.time()-startTime < gameTime:
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
                counter = 1
            #draw rectangle around the hand
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)    
            #draw the distance box on image
            cvzone.putTextRect(img,f'{int(distanceCM)} cm',(x+5,y-10))
        if counter:
            counter +=1
            circleColor = (0,255,0)
            if counter == 5:
                score += 1
                circleColor=(255,0,255)
                cx = np.random.randint(100,1100)
                cy = np.random.randint(100,600)
                color = (255,0,255)
                counter = 0



        #Draw Button on the image
        cv2.circle(img,(cx,cy),30,circleColor,cv2.FILLED)
        cv2.circle(img,(cx,cy),20,(255,255,255),2)  
        cv2.circle(img,(cx,cy),10,(255,255,255),cv2.FILLED)
        cv2.circle(img,(cx,cy),30,(50,50,50),2)


        # Game HUD
        cvzone.putTextRect(img,f'Time Left: {int(gameTime-(time.time()-startTime))}',(800,75),scale=3,offset=20)
        cvzone.putTextRect(img,f'Score: {str(score).zfill(2)}', (75,75),scale=3,offset=20)
    else:
        cvzone.putTextRect(img,"Game Over",(400,400),5,offset=20)
        cvzone.putTextRect(img,f'Final score: {score}',(400,500),5,offset=20)
        cvzone.putTextRect(img,'Press R to restart or Q to exit',(400,100),2,offset=10)

    cv2.imshow("Image",img)
    key = cv2.waitKey(1)
    if key == ord('r'):
        startTime = time.time()
        score = 0
    elif key == ord('q'):
        break
cv2.destroyAllWindows()