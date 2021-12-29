# ButtonPressGame

Introduction

This project is build alongside the tutorials of cvzone and a part of this course. The main intention behind this project is to improve my Image processing, and Object oriented programming skills.
This repository has two files namely main.py and Game.py. 
- main.py
   - It is built to estimate distance from monocular camera to the hand. 
   - Google Mediapipe's Hands module is been used to detect the hand and also landmarks on it.
   - Distance from camera to the detected hand is estimated in the following steps.
     1. Selection of 2 different landmarks on the hand (5, 17 in our case)
     2. Distance measurement among them (the diagonal value).
     3. Using a measuring tape, took a note of the distances from camera to hand and also the diagonal distances from the above step while moving the hand towards and away from the camera. and assigned them to variables called measuredValues and Rawvalues respectively.
     4. It was found that these variables are not related linearly but polynomial with a degree 2 when plotted them using matplotlib.
     5. A ML algorithm could be used to estimate new vlaues in the future but a simple polynomial equation was sufficient to fit our purpose. Using this approach the program now ready to estimate the distance between our camera to hand.

- Game.py
  A simple button press game was developed using the hand distance calculated from main.py script. The idea behind this game development are follows
  - A simple button is placed randomly with in the specified region of interest.
  - The button is written as pressed when the hand distance to camera is below 50cm and the button lies inside the bounding box of the hand.
  - Once the button's state changes to pressed, the color of button changes to green and then randomly placed at a different location with in the region of interest before its state changes back to not pressed. 
  - The new button's state is changed again to pressed only after the hand's distance to camera increases above 50 cm and all the rules mentioned in step 2 are satisfied.
  - Score, Time left, Total score variables are initialized to return the player's score.
  
