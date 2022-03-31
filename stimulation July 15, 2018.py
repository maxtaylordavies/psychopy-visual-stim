
def stimulation(SpatFreqDeg, TempFreq, t_before, T_During, t_after, WinWidth, DispHeight, win, Synch, Motionmode):
    
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
    
    #attaining the monitor frame rate
    #note: if the stimulation runs in windowed mode the frame rate will be 30 fps, in full screen  mode the fps will be 60
    FR = win.getActualFrameRate()
    
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
            print("Did not recieve controlmod, connection timeout.")
            return
        
        #sending 'Wait for parameters' to the second PC
        sock.sendto("Wait for parameters", (Remote_IP, Remote_Port))
        
        try:
            parasize = sock.recv(1024)
        except Exception:
            print("Did not recieve parasize, connection timeout")
            return
        
        #sending a completion transcript
        sock.sendto("read parasize", (Remote_IP, Remote_Port))
        
        #converting the string recieved into int
        parasize = conv.deleteParasize(parasize)
        
        #making the array in which the parameters will be added to
        paras = np.empty(shape=[int(parasize[0]), 9])
        
        #adding the parameters to the array
        
        #this for loop receives the 9 parameters for all the stimulations and adds them to an array
        for i in range(int(parasize[0])): #start from 0 to parasize[0] - 1
            temp = sock.recv(1024)
            temp =conv.convStr2Dig(temp)
            #adding the parameters to the array (temp) at position index
            paras[i, :] = temp
        
        
        sock.sendto("Para DONE", (Remote_IP, Remote_Port))
        
        try:
            #recieving all orientation for stimuli 1 for veritcal, 0 for horizontal
            paratemp = sock.recv(1024)
        except Exception:
            print("Did not recieve message, connection timeout.")
            return
        
        paratemp = conv.convStr2Dig(paratemp)
        
        #setting up the parameters based on what was send in the paras variable
        Ori = int(paratemp[0])
        Motionmode = int(paratemp[1])
        Amp_sinu = paratemp[2]
        addblank = paratemp[3]
        
        
        sock.sendto("Para DONE", (Remote_IP, Remote_Port))
        
        sock.settimeout(0.05)
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
                DrawTexture.setAutoDraw(False)
                square1.autoDraw = False
                square2.autoDraw = False
                return
        
        if controlmod == 'maualVS':
            return
        
        elif controlmod == 'autoVS':
            
            for m in range(int(parasize[0])):
                
                #changing screens to a grey screen depending on addblank
                if addblank == 1.0: 
                    win.color = [winClr,winClr,winClr]
                    win.flip()
                    psychopy.clock.wait(1)
                    
                
                else:
                    pass
                
                if m == 0: 
                    SpatFreqDeg = paras[m, 0]
                    TempFreq = paras[m, 1]
                    contrast = paras[m, 2]
                    MeanLum = paras[m, 3]
                    dirindex = paras[m, 4]
                    t_before = paras[m, 5]/1000.0
                    T_During = paras[m, 6]/1000.0
                    t_after = paras[m, 7]/1000.0
                    t_triginit = paras[m, 8]/1000.0
                    
                    #frames to be calculated per period
                    frames = math.ceil(FR/TempFreq)
                    
                    
                    #generating matrix that will be the place holder for every pixel 
                    pixelangle = np.empty(shape=[1, WinWidth])
                    
                    #generating the corrusponding angle of every pixel
                    for i in range(WinWidthofEachDisp):
                        angle = math.degrees(np.arctan((i - (WinWidthofEachDisp/2.0))*PixelSize*(2.0/DisplayFrameWidth))) + 45   #finding the pixle angle of each pixle in degrees (left monitor)
                        pixelangle[:, i] = angle
                        pixelangle[:, i + WinWidthofEachDisp] = angle + 90
                        pixelangle[:, i + 2*WinWidthofEachDisp] = angle + 180
                    
                    if Motionmode == 1:
                        phase = []
                        for i in range(frames):
                            x = (i/float(frames))*(2.0*np.pi)
                            phase.append(x)
                    
                    elif Motionmode == 0:
                        phase = []
                        for i in range(frames):
                            x = Amp_sinu*np.sin((i/float(frames))*2*math.pi)*SpatFreqDeg*2*math.pi
                            phase.append(x)
                    
                    inc = gray*1.0
                    
                    #creating the list that will hold all frames
                    textdata1D = []
                    for i in range(frames):
                        textdata1DTmp = np.exp(np.log((gray + inc*np.sin(pixelangle*SpatFreqDeg*2*np.pi + phase[i]))/AmpFactor)/GammaFactor)
                        pixVal = 2*(textdata1DTmp/255) - 1 #converting the pixel values from 0:255 to -1:1
                        textdata1D.append(pixVal)
                        
                        
                
                else:
                    if sum(abs(paras[m, :] - paras[m-1, :])) > 1e-7:
                        
                        SpatFreqDeg = paras[m, 0]
                        TempFreq = paras[m, 1]
                        contrast = paras[m, 2]
                        MeanLum = paras[m, 3]
                        dirindex = paras[m, 4]
                        t_before = paras[m, 5]/1000.0
                        T_During = paras[m, 6]/1000.0
                        t_afterVal = paras[m, 7]/1000.0
                        t_triginit = paras[m, 8]/1000.0
                        
                        if Motionmode == 1:
                            phase = []
                            for i in range(frames):
                                x = (i/float(frames))*(2.0*np.pi)
                                phase.append(x)
                        
                        elif Motionmode == 0:
                            phase = []
                            for i in range(frames):
                                x = Amp_sinu*np.sin((i/float(frames))*2*math.pi)*SpatFreqDeg*2*math.pi
                                phase.append(x)
                            
                        #creating the list that will hold all frames
                        textdata1D = []
                        for i in range(frames):
                            textdata1DTmp = np.exp(np.log((gray + inc*np.sin(pixelangle*SpatFreqDeg*2*np.pi + phase[i]))/AmpFactor)/GammaFactor)
                            pixVal = 2*(textdata1DTmp/255) - 1 #converting the pixel values from 0:255 to -1:1
                            textdata1D.append(pixVal)
                    
                #setting up the grating
                DrawTexture = psychopy.visual.GratingStim(
                    win=win,
                    size = [WinWidth, winHeight],
                    units = 'pix',
                    tex=pixVal
                    )
                    
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
                    elif comm[0] == "ESC1":
                        return
                        
                    if mouse.getPressed()[1]:
                        DrawTexture.setAutoDraw(False)
                        square1.autoDraw = False

                        square2.autoDraw = False
                        return
                
                
                #these functions will automatically draw the grating and the square everytime the window is flipped
                DrawTexture.setAutoDraw(True)
                square1.autoDraw = True
                square2.autoDraw = True
                DrawTexture.draw()
                win.flip()
                psychopy.core.wait(t_before)
                
                #t_triger initial timing for triggerin the camera
                for i in range(int(FR*t_triginit)):
                    if i < 3:
                        square1.fillColor = [1,1,1]
                        square2.fillColor = [-1,-1,-1]
                    
                    else:
                        square1.fillColor = [-1,-1,-1]
                        square2.fillColor = [-1,-1,-1]
                    
                    if mouse.getPressed()[1]:
                        DrawTexture.setAutoDraw(False)
                        square1.fillColor = [-1,-1,-1]
                        square2.fillColor = [-1,-1,-1]
                        square1.autoDraw = False
                        square2.autoDraw = False
                        return
                    
                    win.flip()
                
                #this variable controls the looping and frame that is to be displayed
                m = 0
                
                #drawing the frames on the window
                for frm in range(int(FR*T_During)):    #this if statement is to loop the stimulus
                    #assigning the texture using the corrusponding frame
                    DrawTexture.tex = textdata1D[m]
                    square1.fillColor = [-1,-1,-1]
                    square2.fillColor = [1,1,1]
                        
                    #this if statement is for existing the stimulation
                    if mouse.getPressed()[1]:
                        DrawTexture.setAutoDraw(False)
                        square1.fillColor = [-1,-1,-1]
                        square2.fillColor = [-1,-1,-1]
                        square1.autoDraw = False
                        square2.autoDraw = False
                        return
                        
                    m = m + 1
                    
                    if m >= len(textdata1D):
                        m = 0
                    
                
                    win.flip()
                
                #changing the characteristics of the two squares at the bottom left corner
                square1.fillColor = [-1,-1,-1]
                square2.fillColor = [-1,-1,-1]
                win.flip()
                DrawTexture.setAutoDraw(False)
                square1.autoDraw = False
                square2.autoDraw = False
                
                psychopy.clock.wait(t_after)
                
                #checking for stop button
                try:
                    comm = sock.recvfrom(1024)
                except:
                    pass
                if comm[0] == "ESC1":
                        return
                
                sock.sendto("TRLdone " + str(m), (Remote_IP, Remote_Port))
    
    if Synch == False:
        
        
        
        #generating matrix that will be the place holder for every pixel 
        pixelangle = np.empty(shape=[1, winWidth])
        
        #generating the corrusponding angle of every pixel
        for i in range(WinWidthofEachDisp):
            angle = math.degrees(np.arctan((i - (WinWidthofEachDisp/2.0))*PixelSize*(2.0/DisplayFrameWidth))) + 45   #finding the pixle angle of each pixle in degrees (left monitor)
            pixelangle[:, i] = angle
            pixelangle[:, i + WinWidthofEachDisp] = angle + 90
            pixelangle[:, i + 2*WinWidthofEachDisp] = angle + 180
        
        
        inc = gray*1
        frames = int(round(FR/TempFreq))
        
        
        if Motionmode == 1:
            phase = []
            for i in range(frames):
                x = (i/float(frames))*(2.0*np.pi)
                phase.append(x)
        
        elif Motionmode == 0:
            phase = []
            for i in range(frames):
                x = Amp_sinu*np.sin((i/float(frames))*2*math.pi)*SpatFreqDeg*2*math.pi
                phase.append(x)
            
        textdata1D = []
        for i in range(frames):
            textdata1DTmp = np.exp(np.log((gray + inc*np.sin(pixelangle*SpatFreqDeg*2*np.pi + phase[i]))/AmpFactor)/GammaFactor)
            pixVal = 2*(textdata1DTmp/255) - 1 #converting the pixel values from 0:255 to -1:1
            textdata1D.append(pixVal)
            
        #setting up the grating
        DrawTexture = psychopy.visual.GratingStim(
            win=win,
            size = [winWidth, winHeight],
            units = 'pix',
            tex=pixVal
            )
        
        #these functions will automatically draw the grating and the square everytime the window is flipped
        DrawTexture.setAutoDraw(True)
        square1.autoDraw = True
        square2.autoDraw = True
        
        win.flip()
        psychopy.core.wait(t_before)
        
        for i in range(int(FR*t_triginit)):
            if i < 3:
                square1.fillColor = [1,1,1]
                square2.fillColor = [-1,-1,-1]
            
            else:
                square1.fillColor = [-1,-1,-1]
                square2.fillColor = [-1,-1,-1]
            
            #this if statement is for existing the stimulation
            if mouse.getPressed()[1]:
                DrawTexture.setAutoDraw(False)
                square1.autoDraw = False
                square2.autoDraw = False
                square1.fillColor = [-1,-1,-1]
                square2.fillColor = [-1,-1,-1]
                return
            
            win.flip()
        
        
        #this variable controls the looping and frame that is to be displayed
        m = 0
        
        #changing the top square to be white before the stimulus
        square2.fillColor = [1,1,1]
        
        #drawing the frames on the window
        for frm in range(int(FR*T_During)):
            
            #assigning the texture using the corrusponding frame
            DrawTexture.tex = textdata1D[m]
            
            m = m + 1
            
            #looping the sequence
            if m == len(textdata1D):
                m = 0
            
            #this if statement is for existing the stimulation
            if mouse.getPressed()[1]:
                DrawTexture.setAutoDraw(False)
                square1.autoDraw = False
                square2.autoDraw = False
                square1.fillColor = [-1,-1,-1]
                square2.fillColor = [-1,-1,-1]
                return
            
            win.flip(clearBuffer = True)
    
        #changing the characteristics of the two squares at the bottom left corner
        square1.fillColor = [-1,-1,-1]
        square2.fillColor = [-1,-1,-1]
        win.flip()
        DrawTexture.setAutoDraw(False)
        square1.autoDraw = False
        square2.autoDraw = False
        
        psychopy.clock.wait(t_after)