from psychopy import visual
from psychopy import visual, event

import psychopy.event
import math
import numpy as np
import psychopy.core

'''
This program is calibrate the monitors
It displays 10 different levels of brightness
It displays the current level of brightness on the top left part of the screen 
'''

def MonCalib():
    
    #settint the starting brightness of the monitor
    startBrtness = -1
    
    #creating the window
    win = visual.Window(
        fullscr = True, 
        size = [5760, 1080],
        color = -1, #this corrusponds to level 0
        mon = 'Triple Monitor'
        )
    
    #creating variable to display on the top left corner
    level = 0
    
    #creating the textbox to display the level of brightness
    levelText = visual.TextBox(window=win,
        text=(str(level)),
        font_size=55,
        font_color=[-1,-1,1],
        pos=(-2620,515),size=(250,75),
        units='pix',
        grid_horz_justification='left',
        grid_vert_justification='left',
        border_color = None
        )
    
    #drawing the textbox
    levelText.draw()
    win.flip()
    print(win.color)
    print(level)
    #settint the starting brightness of the monitor
    startBrtness = -1
    
    #creating the button for the mouse click
    mouse = event.Mouse(
        visible = True, 
        win = win
        )
    
    #this is the increment that the pixel brightness will be changed by 
    incr = 10 #the value 9 was chosen instead of 10 because the value of 0 corrusponds to grey
    
    #creating a boolean to keep the while loop running during the calibration
    keep_going = True
    prevMouse = [0,0,0]
    while keep_going:
        currMouse = mouse.getPressed()
        #if the left mouse button is clicked, increase the win.color by the incr
        if currMouse[0] == 1 and prevMouse[0] == 0:
            if (level + incr <= 250): #if the pixel value is greater than or equal to 250
                level = level + incr
                win.color = (level/255.0)*2 -1
                levelText.setText(str(level))
                levelText.draw()
                win.color = win.color
                print(win.color)
                print(level)
                win.flip()
            
        #if the right mouse button is clicked, decrease the win.color by the incr
        elif currMouse[2] == 1 and prevMouse[2] == 0:
            if (level - incr >= 0): #if the pixel value is less than or equal to 0
                level = level - incr
                win.color = (level/255.0)*2 -1
                levelText.setText(str(level))
                levelText.draw()
                win.color = win.color
                print(win.color)
                print(level)
                win.flip()
        
        #if the scroll wheel is pressed break the while loop
        elif mouse.getPressed()[1]:
            keep_going = False
        
        
        prevMouse = currMouse


MonCalib()