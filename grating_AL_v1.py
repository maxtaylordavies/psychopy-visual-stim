import numpy as np
import psychopy.core
import VS
import socket
from psychopy import visual
from psychopy import event
from init_para import *

Motionmode = 1 #0 refers to linear motion and 1 refers to sinusoidal motion
MotionmodeB = 0
SpatFreqVal = 0.1
tempFreqVal = 1
t_beforeVal = 1000
t_stimVal = 5000
t_afterVal = 1000
SpatFreqValB = 0.01
tempFreqValB = 2
t_beforeValB = 1000
t_stimValB = 5000
t_afterValB = 1000

GammaFactor = 3.134
AmpFactor = 0.000005
contrast = 1.0
MeanLum = 30
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


win=visual.Window(fullscr=fullscrn,
    size = [winWidth, winHeight], 
    color = 2*(np.exp(np.log(MeanLum/AmpFactor)/GammaFactor)/255.0) -1
    )


planar_grating = psychopy.visual.GratingStim(
    win = win,
    units = 'pix', 
    size= [WinWidthofEachDisp,winHeight],
    tex = 'sin',
    sf = SpatFreqValB,
    texRes = 256,
    #stop = t_stimValB
    )

clock = psychopy.core.Clock()

keep_going = True

while keep_going:

    planar_grating.phase = np.mod(clock.getTime() / 0.5, 1)

    planar_grating.draw()

    win.flip()

    keys = psychopy.event.getKeys()

    if len(keys) > 0:
        keep_going = False

win.close()
