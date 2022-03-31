import numpy as np
from init_para import(MovSinGrat_angles_list, MovSinGrat_spat_list, MovSinGrat_temp_lin_list, MovSinGrat_temp_osc_list, MovSinGrat_features_val, MovSinGrat_location_list,
MovSinGrat_Rep, MovSinGrat_ledstate, MovSinGrat_randomseq) #if needed also import MovSinGrat_contrast_list


#TUNING FEATURE VALUES are defined as follows: # ori = 0, spat_freq = 1, temp_freq_lin = 2, temp_freq_osc = 3, contrast = 4, location = 5
MovSinGrat_ledstate = 2
MovSinGrat_Rep = 3

#creating generalized sequence of randomely shuffled stimuli for tuning, given a particular feature 

#This firt if loop will create two varialbes: 
#tuning_stim_types and tuning_stim_ind which contains all unique stimulus and corresponding index, respectively, given the tuning feature selected.

if MovSinGrat_features_val == 0:
    tuning_stim_types = map(float, MovSinGrat_angles_list) #map applies the float() function to all elements of the list, therefore converting strings to float
    tuning_stim_ind = range(len(tuning_stim_types))
elif MovSinGrat_features_val == 1:
    tuning_stim_types = map(float, MovSinGrat_spat_list)
    tuning_stim_ind = range(len(tuning_stim_types))
elif MovSinGrat_features_val == 2:
    tuning_stim_types = map(float, MovSinGrat_temp_lin_list) 
    tuning_stim_ind = range(len(tuning_stim_types))
elif MovSinGrat_features_val == 3: 
    tuning_stim_types = map(float, MovSinGrat_temp_osc_list) 
    tuning_stim_ind = range(len(tuning_stim_types))
elif MovSinGrat_features_val == 4: 
    tuning_stim_types = map(float, MovSinGrat_location_list) 
    tuning_stim_ind = range(len(tuning_stim_types))
#elif MovSinGrat_features_val == 5: 
#    tuning_stim_types = MovSinGrat_contrast_list #HAS NOT BEEN CREATED IN INIT_PARA YET; 
#    tuning_stim_ind = range(len(tuning_stim_types))
else:
    print 'ERROR: MovSinGrat_features_val outside range. Tuning Feature Value must an integer be between 0 and 4.'

#print 'tuning_stim_ind: ', tuning_stim_ind
#print 'tuning_stim_types: ', tuning_stim_types


for rep_ind in xrange(MovSinGrat_Rep): 
                
    stimId = np.empty(len(tuning_stim_ind)*MovSinGrat_ledstate)
    #for localstimind in xrange(0,(len(tuning_stim_ind)*MovSinGrat_ledstate)):
        #stimId.append(1)
                        
    if MovSinGrat_randomseq:
        
        for iled in xrange(0,MovSinGrat_ledstate): #for each ledstate, one of each angle will be assoign in random order
            np.random.shuffle(tuning_stim_ind)
            
            for n in xrange(iled,len(stimId),MovSinGrat_ledstate): #assign tuning_stim_ind elements to stimId by hops of size ledstate (if ledstate = 1), stimId = tuning_stim_ind;
                stimId[n] = tuning_stim_ind[n/MovSinGrat_ledstate] #
                        
    else:
        for iled in xrange(0,MovSinGrat_ledstate): 
                                   
            for n in xrange(iled,len(stimId),MovSinGrat_ledstate):
                stimId[n] = tuning_stim_ind[n/MovSinGrat_ledstate]
    
    print stimId[1:len(stimId):2]
    temp = stimId[0:len(stimId):2].tolist()
    print temp.sort()           

    


#print 'this is stimId: ', stimId
#print 'this is tuning_stim_types: ', tuning_stim_types
#print 'this is tuning_stim_ind: ', tuning_stim_ind
#print 'this is tuning_stim_types[stimId[1]]: ', tuning_stim_types[stimId[1]]
