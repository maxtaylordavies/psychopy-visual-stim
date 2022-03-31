#from psychopy import visual
#import numpy as np
#
#MeanLum = 55
#GammaFactor = 2.306
#AmpFactor = 0.0005283
#fullscrn = True
#
#creating the window
#winClr = 2*(np.exp(np.log(MeanLum/AmpFactor)/GammaFactor)/255.0) -1
#win=visual.Window(fullscr=fullscrn,
#    units = 'norm', 
#    color = winClr
#    )


#Linehorz=psychopy.visual.Line(win, start=(-1, 0), end=(1, 0))
#Linevert=psychopy.visual.Line(win, start=(0, 1), end=(0, -1))
#
#Linehorz.draw()
#Linevert.draw()
#win.flip()
#
#
#keys = event.getKeys()
#while True:
#    if keys[0] == 'escape':
#        break
#    else:
#        win.flip()
#win.close()


def crossline():
    import numpy as np
    from psychopy import core, visual, event
    import VS
    import drumgrating
    import movSinGrat_tuning
    import EYE_calibration
    import socket
    from init_para import *
    import TestNov
    import Vdrumgrating
    import Rf6x8
    
    #CREATING TEXTBOXES
    
    #DRUMGRATING
    
    Linehorz=psychopy.visual.Line(win, start=(-1, 0), end=(1, 0))
    Linevert1=psychopy.visual.Line(win, start=(0, 1), end=(0, -1))  # vertical line on middle monitor
    Linevert2=psychopy.visual.Line(win, start=(-4/6.0, 1), end=(-4/6.0, -1))  # vertical line on left monitor
    Linevert3=psychopy.visual.Line(win, start=(4/6.0, 1), end=(4/6.0, -1))  # vertical line on right monitor
    #drawing the textboxes
    Linehorz.draw()
    Linevert1.draw()
    Linevert2.draw()
    Linevert3.draw()
    
    
    win.flip()

    mouse = event.Mouse(
        visible = True, 
        win = win
        )
    
    keep_going = True
    
    while keep_going:
        psychopy.core.wait(0.1)
        currMouse = mouse.getPressed()
        
        keys = event.getKeys() #this will retrieve key presses from the buffer and place them into a list (in the order that they were pressed)
        
        
        if keys:
            if keys[0] == 'escape':
                    break
        
        #these functions are to draw all the buttons and textboxes
        if sum(currMouse) > 0:
            Linehorz.draw()
            Linevert1.draw()
            Linevert2.draw()
            Linevert3.draw()
            win.flip()
        
    
    win.close()

#front()