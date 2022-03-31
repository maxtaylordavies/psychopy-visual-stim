def stimulation(SpatFreqDegB, TempFreqB, t_beforeB, t_DuringB, t_afterB, WinWidth, DispHeight, win, Synch, MotionmodeB, Ori):
    
    from psychopy import visual
    from psychopy import event
    from init_para import *
    import socket
    import numpy as np
    import conv
    
    #crating mouse functionality
    mouse = event.Mouse(
        visible = True, 
        win = win
        )
    
    if Synch:
        
        #creating the socket in which communications will take place
        sock = socket.socket(
            socket.AF_INET, 
            socket.SOCK_DGRAM
        )
        
        
        #binding the local IP address and local port 
        sock.bind((Local_IP, Local_Port))
        
        try:
            #wait for the command 'gammacorrection'
            info = sock.recv(1024)
        except Exception:
            sock.close()
            print("Did not recieve info, connection timeout.")
            return
            
        
        #sending 'gammafloatampfloat' to the second PC
        sock.sendto(("gamma" + str(GammaFactor) + "amp" + str(AmpFactor)), (Remote_IP, Remote_Port))
        
        try:
            #waiting for the signal autoVs
            controlmod = sock.recv(1024)
        except Exception:
            sock.close()
            print("Did not recieve controlmod, connection timeout.")
            return
        
        #sending 'Wait for parameters' to the second PC
        sock.sendto("Wait for parameters", (Remote_IP, Remote_Port))
        
        try:
            parasize = sock.recv(1024) #This is equivalent to Rep >> can you set Rep num in Eye tracking software???
        except Exception:
            sock.close()
            print("Did not recieve parasize, connection timeout.")
            return
        
        #sending a completion transcript
        sock.sendto("read parasize", (Remote_IP, Remote_Port))
        
        #converting the string recieved into int
        parasize = conv.deleteParasize(parasize)
        
        #making the array in which the parameters will be added to
        paras = np.empty(shape=[parasize, 9])
        
        #adding the parameters to the array
        
        #this for loop receives the 9 parameters for all the stimulations and adds them to an array
        for i in range(parasize): #start from 0 to parasize[0] - 1
            temp = sock.recv(1024)
            temp =conv.convStr2Dig(temp)
            #adding the parameters to the array (temp) at position index
            paras[i, :] = temp
        
        sock.sendto("Para DONE", (Remote_IP, Remote_Port))
        
        try:
            #recieving all orientation for stimuli 1 for veritcal, 0 for horizontal
            paratemp = sock.recv(1024)
        except Exception:
            sock.close()
            print("Did not recieve message, connection timeout.")
            return
        
        paratemp = conv.convStr2Dig(paratemp)
        
        #setting up the parameters based on what was send in the paras variable
        Ori = int(paratemp[0])
        Motionmode = int(paratemp[1])
        Amp_sinu = paratemp[2]
        addblank = paratemp[3]
        
        sock.sendto("Para DONE", (Remote_IP, Remote_Port))
    
    #if Synch is False, this else condition will make the parameters in the same format as if Synch was True
    else:
        
        #making the array in which the parameters will be added to
        paras = np.empty(shape=[parasize, 9])
        
        #adding the parameters to the array
        for i in range(parasize): #start from 0 to parasize[0] - 1
            
            #adding the parameters as an array at index i
            paras[i, :] = [SpatFreqDegB, TempFreqB, contrast, MeanLum, dirindex, t_beforeB, t_DuringB, t_afterB, t_triginit]
        
        paratemp = [Ori, MotionmodeB, Amp_sinu, addblank]
        
        #setting up the parameters based on what was send in the paras variable
        Ori = int(paratemp[0])
        MotionmodeB = int(paratemp[1])
        Amp_sinu = paratemp[2]
        addblank = paratemp[3]
        
    if Synch:
        
        #waiting for "STR"
        while True:
            try:
                info = sock.recv(1024)
            except:
                pass
            if info == "STR":
                sock.sendto(("VS is running"), (Remote_IP, Remote_Port))
                break
            if mouse.getPressed()[1]:
                sock.close()
                return
    
    #generating the pixel angles relaive to the mouse position based on the orientation of the stimulus
    if Ori == 1:
        #generating matrix that will be the place holder for every pixel 
        pixelangle = np.empty(shape=[1, WinWidth])
        
        #generating the corresponding angle of every pixel
        for i in range(WinWidthofEachDisp):
            angle = np.degrees((i - (WinWidthofEachDisp/2.0))*PixelSize*(2.0/DisplayFrameWidth)) #+ 45   #finding the pixle angle for central pixels and then multiplying all other pixels by central pixel angle
            #pixelangle[:, i + WinWidthofEachDisp] = angle + 90
            #pixelangle[:, i + 2*WinWidthofEachDisp] = angle + 180
                    
        else:
            return
    
    else:
        return
    
    if controlmod == 'maualVS':
        return
    
    elif controlmod == 'autoVS':
        
        for m in range(parasize):
            
            
            if m == 0: 
                SpatFreqDegB = paras[m, 0]
                TempFreqB = paras[m, 1]
                contrast = paras[m, 2]
                MeanLum = paras[m, 3]
                dirindex = paras[m, 4]
                t_beforeB = paras[m, 5]/1000.0
                t_DuringB = paras[m, 6]/1000.0
                t_afterB = paras[m, 7]/1000.0
                t_triginit = paras[m, 8]/1000.0
                pixelformeanlum = 2*(np.exp(np.log(MeanLum/AmpFactor)/GammaFactor)/255.0) -1
                gray = MeanLum
                inc = gray*contrast
                
                #frames to be calculated per period
                frames = int(np.ceil(FR/TempFreqB))
                
                if MotionmodeB == 1:
                    phase = []
                    for i in range(frames):
                        x = (i/float(frames))*(2.0*np.pi)
                        phase.append(x)
                
                elif MotionmodeB == 0:
                    phase = []
                    for i in range(frames):
                        x = Amp_sinu*np.sin((i/float(frames))*2*np.pi)*SpatFreqDegB*2*np.pi
                        phase.append(x)
                
                #generating the pixel values for the stimulus depending on the orientation of the stimulus 
                if Ori == 1:
                    
                    #creating the list that will hold all frames
                    textdata1D = []
                    
                    #generating the pixel values for vertical stimulus
                    for i in range(frames):
                        textdata1DTmp = np.exp(np.log((gray + inc*np.sin(pixelangle*SpatFreqDegB*2*np.pi + phase[i]))/AmpFactor)/GammaFactor)
                        pixVal = 2*(textdata1DTmp/255) - 1 #converting the pixel values from 0:255 to -1:1
                        textdata1D.append(pixVal)
                
                else:
                    return
            
            else:
                if sum(abs(paras[m, :] - paras[m-1, :])) > 1e-7:
                #if (not all([v == 0  for v in abs(paras[m, :] - paras[m-1, :])])):
                    
                    SpatFreqDegB = paras[m, 0]
                    TempFreqB = paras[m, 1]
                    contrast = paras[m, 2]
                    MeanLum = paras[m, 3]
                    dirindex = paras[m, 4]
                    t_beforeB = paras[m, 5]/1000.0
                    t_DuringB = paras[m, 6]/1000.0
                    t_afterValB = paras[m, 7]/1000.0
                    t_triginit = paras[m, 8]/1000.0
                    pixelformeanlum = 2*(np.exp(np.log(MeanLum/AmpFactor)/GammaFactor)/255.0) -1
                    gray = MeanLum
                    inc = gray*contrast
                    
                    #frames to be calculated per period
                    frames = int(np.ceil(FR/TempFreqB))
            
                if MotionmodeB == 1:
                    phase = []
                    for i in range(frames):
                        x = (i/float(frames))*(2.0*np.pi)
                        phase.append(x)
                
                elif MotionmodeB == 0:
                    phase = []
                    for i in range(frames):
                        x = Amp_sinu*np.sin((i/float(frames))*2*np.pi)*SpatFreqDegB*2*np.pi
                        phase.append(x)
                
                #generating the pixel values for the stimulus depending on the orientation of the stimulus 
                if Ori == 1:
                    
                    #creating the list that will hold all frames
                    textdata1D = []
                    
                    #generating the pixel values for vertical stimulus
                    for i in range(frames):
                        textdata1DTmp = np.exp(np.log((gray + inc*np.sin(pixelangle*SpatFreqDegB*2*np.pi + phase[i]))/AmpFactor)/GammaFactor)
                        pixVal = 2*(textdata1DTmp/255) - 1 #converting the pixel values from 0:255 to -1:1
                        textdata1D.append(pixVal)
                
                else:
                    return
                    
            
            #setting up the grating
            DrawTexture = psychopy.visual.GratingStim(
                win=win,
                size = [WinWidth, winHeight],
                units = 'pix',
                tex=pixVal
                )
            
            if Synch:
                
                #waiting for "TRLstart", if TRLstart is sent this loop will send "TRLstart m" then break
                sock.settimeout(0.5)
                comm = [""]
                while True:
                    try:
                        comm = sock.recvfrom(1024)
                    except Exception:
                        pass
                        
                    if comm[0] == "TRLstart":
                        sock.sendto(("TRLstart " + str(m)), (Remote_IP, Remote_Port))
                        break
                        
                    elif comm[0] == "ESC1": #if 'ESC1' is in the buffer, return to front
                        sock.close()
                        return
                        
                    if mouse.getPressed()[1]:
                        sock.close()
                        return
            
            # Generating sequence of angles and corresponding stimID that will change the orientation of the stimuli:
            for rep in xrange(0,len(Rep)):
                stimId = [] 
                for i in xrange(0,(len(angles)*ledstate)):
                    stimId.append(1)
                    
                if randomseq:
                    np.random.shuffle(num_angles)
                    for iled in xrange(0,ledstate): #for each ledstate, one of each angle will be assoign in random order
                        
                        for n in xrange(iled,len(stimId),2):
                            stimId[n] = num_angles[n/2]
                        
                else:
                    for iled in xrange(0,ledstate): 
                       
                        for n in xrange(iled,len(stimId),2):
                            stimId[n] = num_angles[n/2]
                            
                #For each stimulus, angle will be the ith number in stimId
                #Run trial (includes: time_before, time_during (stimuli presentation) and time_after (pause))
                for stimnum in xrange(1,len(stimId)):
                    
                    #orientation of stimuli corresponds to stimnum index in stimId
                    DrawTexture.ori = stimId[stimnum] #should it be angle[stimId[stimnum]]??? if so, need to change above so that it is range(0, len(angles)) 
                            
                    #time before the stimulation
                    for toc in range(int(t_beforeB*FR)):
                        
                        if addblank == 1.0:
                            win.color = pixelformeanlum
                            square1.draw()
                            square2.draw()
                            
                        elif addblank == 0.0:
                            DrawTexture.draw()
                            square1.draw()
                            square2.draw()
                        win.flip()
                    
                    #t_triger initial timing for triggerin the camera
                    for i in range(int(FR*t_triginit)):
                        if i < 3:
                            square1.fillColor = [1,1,1]
                            square2.fillColor = [-1,-1,-1]
                        
                        else:
                            square1.fillColor = [-1,-1,-1]
                            square2.fillColor = [-1,-1,-1]
                        
                        if addblank == 1.0:
                            win.color = pixelformeanlum
                            square1.draw()
                            square2.draw()
                        
                        elif addblank == 0.0:
                            DrawTexture.draw()
                        
                        if mouse.getPressed()[1]:
                            if Synch:
                                sock.close()
                            return
                        
                        square1.draw()
                        square2.draw()
                        win.flip()
                    
                    #making the top square white
                    square1.fillColor = [-1,-1,-1]
                    square2.fillColor = [1,1,1]
                    
                    #this variable controls the looping and frame that is to be displayed
                    m = 0
                    
                    #drawing the frames on the window
                    for frm in range(int(FR*t_DuringB)):
                        
                        #assigning the texture using the corrusponding frame
                        DrawTexture.tex = textdata1D[m]
                        
                        
                        #this if statement is for existing the stimulation
                        if mouse.getPressed()[1]:
                            
                            if Synch:
                                sock.close()
                            return
                        
                        m = m + 1
                        
                        if m >= len(textdata1D):
                            m = 0
                        
                        DrawTexture.draw()
                        square1.draw()
                        square2.draw()
                        win.flip()
                    
                    #changing the characteristics of the two squares at the bottom left corner
                    square1.fillColor = [-1,-1,-1]
                    square2.fillColor = [-1,-1,-1]
                    
                    #time after the stimulation
                    for toc in range(int(t_afterB*FR)):
                        
                        if addblank == 1.0:
                            win.color = pixelformeanlum
                            square1.draw()
                            square2.draw()
                            
                        elif addblank == 0.0:
                            DrawTexture.draw()
                            square1.draw()
                            square2.draw()
                        
                        win.flip()
                    
                    if Synch:
                        
                        #checking for stop button
                        while True:
                            
                            try:
                                comm = sock.recvfrom(1024)
                            except:
                                pass
                            
                            if comm[0] == "ESC1":
                                sock.close()
                                return 
                            
                            elif comm[0] == "ESC0":
                                break
                            
                            elif mouse.getPressed()[1]:
                                sock.close()
                                return 
                        
                        sock.sendto("TRLdone " + str(m), (Remote_IP, Remote_Port))0

