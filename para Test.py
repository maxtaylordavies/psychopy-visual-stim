
import psychopy.visual
import psychopy.event
import socket
import numpy as np
import psychopy.core
import conv

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

win=psychopy.visual.Window(
    fullscr=True,
    size = [winWidth/3, winHeight], 
    color = 2*(np.exp(np.log(MeanLum/AmpFactor)/GammaFactor)/255.0) -1
    )

grating = psychopy.visual.GratingStim(
    win=win,
    units = "pix",
    size = [winWidth/3, winHeight],
    sf= (5.0*3)/winWidth
)

clock = psychopy.core.Clock()
phase = 0.75

keep_going = True

while keep_going:
    
    grating.phase= np.mod(clock.getTime() / phase, 1)
    
    grating.draw()
    
    win.flip()
    
    keys = psychopy.event.getKeys()
    
    if len(keys) > 0:
        keep_going = False
        
        win.close()

