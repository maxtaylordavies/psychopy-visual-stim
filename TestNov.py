import numpy as np


def change():
    import time
    import psychopy.clock
    drumgrating_Motionmode = 10 #0 refers to linear motion and 1 refers to sinusoidal motion
    tic = time.time()
    tic1 = psychopy.clock.getTime()
    psychopy.clock.wait(2)
    tic2 = time.time()
    tic3 = psychopy.clock.getTime()
    print(tic2 - tic)
    print(tic3- tic1)
    
    

change()
    
    
    

