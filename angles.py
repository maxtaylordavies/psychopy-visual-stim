import numpy as np
from psychopy import visual 
from psychopy import event

Rep = 5
localflag = 1
randomseq = 1
ledstate = 2

angle0 = 0
angle1 = 330
DirNum = 12

localgrid = [7,4]

angles = np.linspace(angle0, angle1, DirNum)

locations = np.arange(2, np.product(localgrid))

#create ID for every repetition of all every stimuli (Rep)
for rep in range(Rep):
    
    if localflag:
        stimId = np.ones(len(locations*ledstate)) #create array of nan of size stimulus type * LED state (so that for each stimuli location will be presented in all cases of Led state (on or off)
         
        if randomseq:
            for iled in range(0,ledstate): #for each ledstate, one of each location will be assoign in random order
                
                np.random.shuffle(locations)
                
                for n in xrange(iled,len(locations),2):
                    print stimId[n] = locations[n]
                    
                    

print 'done'
print locations
print stimId