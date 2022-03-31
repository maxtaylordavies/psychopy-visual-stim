from psychopy import visual
from psychopy import visual
from psychopy import visual, event
from init_para import *
import socket
import psychopy.event
import math
import numpy as np
import psychopy.core
import conv

'''
Note: DO NOT RUN THIS PROGRAM, only modify parameters and save it from the drop down menu 
If you do, just wait and the program will exit on its own. This may take a while.
'''

#UDP Parameters
Remote_IP = '192.168.137.1'
Remote_Port = 9092
Local_IP = '192.168.137.2'
Local_Port = 9093
syncVal = False

#Monitor Patameters
GammaFactor = 3.134
AmpFactor = 0.000005
contrast = 1
gray = 50
winWidth = 5760
winHeight = 1080
ScrnNum = 3.0
DisplayFrameWidth = 566.0
Dispwidth = 522
DispHeight = 293
PixelSize = (Dispwidth*ScrnNum)/float(winWidth)
WinWidthofEachDisp = int(winWidth/ScrnNum)
fullscrn = True

#Moving sin gradient parameters
sqrLen = 30
Amp_sinu = 2
t_triginit = 1.0

#creating the window
winClr = 0
win=visual.Window(fullscr=fullscrn,
    size = [winWidth, winHeight], 
    color = [ winClr, winClr, winClr]
    )

#texbox parameters
fontSize = 15
fontClr = [0.5, 0.5, 0.5]
boarderClr = [0.5, 0.5, 0.5]

#setting the vertices for the squares
squarePos = np.array(([-sqrLen, -sqrLen], [-sqrLen, sqrLen], [sqrLen, sqrLen], [sqrLen, -sqrLen]))
#reshaping the array into a 4 by 2 matrix
squarePos.reshape(4, 2)

#setting up the squares at the bottom left
square1 = psychopy.visual.ShapeStim(
    win = win, 
    units = "pix",
    pos = (-winWidth/2 + sqrLen,-winHeight/2 + sqrLen),
    fillColor = [-1, -1, -1],
    vertices = squarePos, 
    lineWidth = 0
    )
square2 = psychopy.visual.ShapeStim(
    win = win, 
    units = "pix",
    pos = (-winWidth/2 + sqrLen,-winHeight/2 + 3*sqrLen), #the 3* is there to place the second square ontop of the first
    fillColor = [-1, -1, -1],
    vertices = squarePos, 
    lineWidth = 0
    )

