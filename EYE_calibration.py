def calibration(win, Synch):   # modified >>>>>>>>>>>>>>>>>>>>>>
    '''
    input: win (define a window)
    output: vis stim with varying lum val changing based on log scale
    
    This function will generate static grating will changing luminance (using log scale). 
    This visual stim will be used to calibrate the eye tracking system.
    
    NOTE: the relationship beteen pupil size and luminance is logarithmic; 
    therefore the steps by which the liminance is increase follow a log scale; 

    '''

    import numpy as np
    from psychopy import event, visual, core 
    import socket


    from init_para import (MovSinGrat_Amp_sinu, GammaFactor, AmpFactor, MovSinGrat_contrast, MovSinGrat_MeanLum, win,
    winWidth , winHeight, ScrnNum, PixelSize, winWidthofEachDisp, DisplayFrameWidth, FR, square1, square2, fontSize, fontClr, win, Local_IP, Local_Port, Remote_IP, Remote_Port)

    #define parameters
    WholeWinwidth = winWidth
    WinWidthofEachdisp = winWidth/ScrnNum
    
    #set the type of pattern for the calibration:
    calib_pattern = 0

    if calib_pattern: #1 = gratting, 0 = uniform
        maximum = (AmpFactor*250**GammaFactor)/2 #the max elgible val for MeanLum in cd/m^2 
    else:
        maximum = (AmpFactor*250**GammaFactor) #the max elgible val for MeanLum in cd/m^2
        
    #minimum = (MovSinGrat_AmpFactor*1**MovSinGrat_GammaFactor)/2 #the min elgible val for MeanLum incd/m^2 
    minimum = 2
    log_max = np.log(maximum)
    log_min = np.log(minimum)

    num_step = 8 #but total steps plus 2 0
    log_step = (log_max - log_min)/num_step
    Contrast = 1

    temp = np.array(range(0, (num_step+1)))
    log_lum_val = log_min + log_step*(temp)
    lum_val_list = np.exp(log_lum_val)
    lum_val_list = np.append([0], lum_val_list)
    lum_val = lum_val_list[0]
    step_count = 0 #counter to loop around lum values
    
    if Synch:
        
        #creating the socket in which communications will take place
        sock = socket.socket(
            socket.AF_INET, 
            socket.SOCK_DGRAM
        )
        
        #binding the local IP address and local port 
        sock.bind((Local_IP, Local_Port))
        #creating textbox showing that this VS computer is waiting for UDP signal
        standBy= visual.TextBox(
            window=win,
            text=("Waiting for starting the control computer."),
            font_size = fontSize,
            font_color=fontClr,
            pos=(-2690 ,475),
            size=(300,37),
            units='pix',
            grid_horz_justification='center',
            grid_vert_justification='center')
        
        standBy.draw()
        square1.draw()
        square2.draw()
        win.flip()
        try:
            #wait for the command 'calibration'
            info = sock.recv(1024)
        except Exception:
            sock.close()
            print("Did not recieve info, connection timeout.")
            return        
        #send lum value list to the eyetracker
        sock.sendto(str(len(lum_val_list)), (Remote_IP, Remote_Port))
        sock.sendto(str(lum_val_list), (Remote_IP, Remote_Port))
        
#    inc = lum_val* Contrast #increase the step by this variable
#    SpatFreqDeg = 0.1
#    #MeanLum = (maximum)/2
#    phase = 0 #in radius 

    #generating matrix that will be the place holder for every pixel 
#    pixelangle = np.empty(shape=[1, winWidth]) #pixel has to be 2D since the image is 2D
#    temp = np.array(range(winWidthofEachDisp)) 
#    temp.reshape(1,winWidthofEachDisp)# the temp must be 2D 
#    tempPixelAngle = np.degrees(np.arctan((temp - (winWidthofEachDisp/2.0))*PixelSize*(2.0/DisplayFrameWidth))) + 45 #calculating the pixel angle for first monitor


#    for i in range(ScrnNum):
#        pixelangle[:,i*winWidthofEachDisp: (i + 1)*winWidthofEachDisp ] = tempPixelAngle + 90*i #taking specific ranges within the full winWidth and replacing the values with the corresponding angles
#
#    #generating the pixel values for vertical stimulus 
#    texdata1DTmp = np.exp(np.log((lum_val + inc*np.sin(pixelangle*SpatFreqDeg*2*np.pi + phase))/AmpFactor)/GammaFactor)
#    pixVal = 2*(texdata1DTmp/255) - 1 #converting the pixel values from 0:255 to -1:1
    pixVal=np.empty(shape=[1, winWidth])
    if not calib_pattern: #for uniform mask, set pixval to single lum_val
        uniform_pix = np.exp(np.log(lum_val/AmpFactor)/GammaFactor)
        pixVal[:] = 2*(uniform_pix/255) - 1

    #setting up the grating
    DrawTexture = visual.GratingStim(
        win=win,
        size = [winWidth, winHeight],
        units = 'pix',
        tex=pixVal
        )

    #display current lumninance value
    lum_text = visual.TextBox(
        window=win,
        text=(str('%.1f'%(lum_val))),
        font_size = fontSize + 7,
        font_color=[1, 1, 1],
        pos=(WholeWinwidth/2*(-1) + 50 ,winHeight/2-25),
        size=(300,37),
        units='pix',
        grid_horz_justification='center',
        grid_vert_justification='center')

    #draw grating and lum val
    DrawTexture.draw()
    lum_text.draw()

    #flip window and display gratting and lum val
    win.flip()

    mouse = event.Mouse(
            visible = True, 
            win = win
            )

    #display grating; and allow user to modify luminance of the grating according to right and left clic  
    if Synch:
        sock.settimeout(0.0)
    while True:
        core.wait(0.02)

        #get keys
        currMouse = mouse.getPressed()
        
         #clicking the middle button causes program to close
        if Synch:
            if currMouse[1]:
                break
            else:
                try:
                    indextemp = sock.recv(1024)
                except Exception:
                    indextemp=''
                    
                if len(indextemp)>0:
                    if indextemp=='stop':
                        break
                    else:
                        step_count=int(indextemp)
        else:
            if currMouse[1]:
                break
            #left clic: increase lum
            elif currMouse[0]: 
                #increase counter (starts at 0)
                step_count += 1
            elif currMouse[2]: #right clic: decrease lum
                #decrease counter (starts at 0)
                step_count -= 1

        #increase by increment value
        lum_val = lum_val_list[step_count%(len(lum_val_list))]
#        inc = lum_val*Contrast
        
#        #regenerating the pixel values from luminance val 
#        texdata1DTmp = np.exp(np.log((lum_val + inc*np.sin(pixelangle*SpatFreqDeg*2*np.pi + phase))/AmpFactor)/GammaFactor)
#        pixVal = 2*(texdata1DTmp/255) - 1 #converting the pixel values from 0:255 to -1:1
            
        if not calib_pattern: #for uniform mask, set all of pixval to lum_val
            uniform_pix = np.exp(np.log(lum_val/AmpFactor)/GammaFactor)
            pixVal[:] = 2*(uniform_pix/255) - 1
            
        #redraw texture and new lum val
        #setting up the grating
        DrawTexture = visual.GratingStim(
            win=win,
            size = [winWidth, winHeight],
            units = 'pix',
            tex=pixVal)
        #display current lumninance value
        lum_text = visual.TextBox(
            window=win,
            text=(str('%.1f'%(lum_val))),
            font_size = fontSize + 7,
            font_color=[1, 1, 1],
            pos=(WholeWinwidth/2*(-1) + 50 ,winHeight/2-25),
            size=(300,37),
            units='pix',
            grid_horz_justification='center',
            grid_vert_justification='center')
                
        #draw grating and lum val
        DrawTexture.draw()
        lum_text.draw()
            
        #flip window and display gratting and lum val
        win.flip()
            
        while any(currMouse):
            currMouse = mouse.getPressed()
    if Synch:
        sock.close()