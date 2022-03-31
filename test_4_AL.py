import numpy as np

repetition = 2
num_dif_stim = 48*2 #number of location the stimulus (6 x 8 = 48) will be displayed in two colours values with 100% contrast => 48*2 = 96
tot_num_stim = repetition * num_dif_stim #total number of stiumuli that will be displayed in one experiment 

#contrast parameters
meanLum = 35
minLum = 0
maxLum = meanLum * 2
gammaFactor = 2.251
ampFactor = 0.0007181

winClr = 2*(np.exp(np.log(meanLum/ampFactor)/gammaFactor)/255.0) -1  #colour of background (in pix val)
white = 2*(np.exp(np.log(maxLum/ampFactor)/gammaFactor)/255.0) -1 #convert maxLum into pix value
black =  -1

#stim order parameters
index = range(num_dif_stim) #number 0-95 representing each location in 6 x 8 screen and black or white colour
x_pos = ([0]*6 + [1]*6 +[2]*6 +[3]*6 +[4]*6 +[5]*6 +[6]*6 +[7]*6) * 2  #list of all possible x-coordinate for stim
y_pos = range(6)*16  #list of all possible y-coordinate for stim
colour_list = [white]*48 + [black]*48 

#reshape data into numpy array
x_pos = np.asarray(x_pos)
y_pos = np.asarray(y_pos)
colour_list = np.asarray(colour_list)

#creating a matrix to store all stim ID (index), position and colour information
stim_order = np.ones((96,4), dtype=int)

stim_order[:,0] = index
stim_order[:,1] = x_pos
stim_order[:,2] = y_pos
stim_order[:,3] = colour_list

#create ramdom order for stimuli presentation
np.random.shuffle(index) #this function automatically shuffles the input (no need to assign a new var)

#loop over each stim and display it
for rep in range(len(index)*repetition):  #will loop around for total Repetitions (96*repetition)
    
    stim_ind = rep % len(index)  #give a number between 0 and 95 which represents each stimuli, allowing to continuouly loop around for total repetitions
    
    #assign postion of stimulus
    i, j = stim_order[index[stim_ind]][1], stim_order[index[stim_ind]][2]

    #assing colour of stimulus
    colour = stim_order[index[stim_ind]][3]
    
    print i, j, colour
    
    #add save functionality 
    
    #add while loop
    
    

