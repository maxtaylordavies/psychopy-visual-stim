
def front():
    import numpy as np
    import psychopy.core
    import VS
    import stimulation
    import stimulationB
    import socket
    from psychopy import visual
    from psychopy import event
    from init_para import *
    
    Motionmode = 1 #0 refers to linear motion and 1 refers to sinusoidal motion
    SpatFreqVal = 0.1
    tempFreqVal = 1
    t_beforeVal = 1000
    t_stimVal = 5000
    t_afterVal = 1000
    MotionmodeB = 1 #0 refers to linear motion and 1 refers to sinusoidal motion
    SpatFreqValB = 0.1
    tempFreqValB = 1
    t_beforeValB = 1000
    t_stimValB = 5000
    t_afterValB = 1000
    
    #creating text box for Moving sin gradient with compensation (curved)
    
    #creating a textbox for spatial frequency
    SpatFreq = visual.TextBox(window=win,
        text=('Spt Frq: ' + str(SpatFreqVal)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(-2280,475),
        size=(232,37),
        units='pix',
        grid_horz_justification='center',
        grid_vert_justification='center')
    
    #creating a textbox for temporal frequency
    TempFreq = visual.TextBox(window=win,
        text=('Tmp Frq: ' + str(tempFreqVal)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(-2040,475),
        size=(232,37),
        units='pix',
        grid_horz_justification='center',
        grid_vert_justification='center')
    
    #creating a textbox for time before the stimulation
    t_Before = visual.TextBox(window=win,
        text=('T_Bef: '+ str(t_beforeVal)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(-1560,475),
        size=(232,37),
        units='pix',
        grid_horz_justification='center',
        grid_vert_justification='center')
        
    #creating a textbox for duration of stimulation
    t_stim = visual.TextBox(window=win,
        text=('T_ Dur: ' + str(t_stimVal)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(-1320,475),
        size=(232,37),
        units='pix',
        grid_horz_justification='center',
        grid_vert_justification='center')
        
    #creating a textbox for the time after the stimulation
    t_after = visual.TextBox(
        window=win,
        text=('T_Aft: ' + str(t_afterVal)),
        font_size = fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(-1080,475),
        size=(232,37),
        units='pix',
        grid_horz_justification='center',
        grid_vert_justification='center')
    
    #creating a Synch textbox
    synch = visual.TextBox(
        window=win,
        text=('Synch:' + str(syncVal)),
        font_size = fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(-2520,475),
        size=(232,37),
        units='pix',
        grid_horz_justification='center',
        grid_vert_justification='center')
    
    #creating a moationMode textbox
    mtnmode = visual.TextBox(
        window=win,
        text=("Motn Mode: " + str(Motionmode)),
        font_size = fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(-1800,475),
        size=(232,37),
        units='pix',
        grid_horz_justification='center',
        grid_vert_justification='center')
    
    #creating a name textbox
    Name = visual.TextBox(
        window=win,
        text=("CURVED sin Grdnt"),
        font_size = fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(-2760 ,475),
        size=(232,37),
        units='pix',
        grid_horz_justification='center',
        grid_vert_justification='center')
    
    #creating a waiting for signal textbox
    standBy= visual.TextBox(
        window=win,
        text=("Waiting For Signal"),
        font_size = fontSize,
        font_color=fontClr,
        pos=(-2690 ,475),
        size=(300,37),
        units='pix',
        grid_horz_justification='center',
        grid_vert_justification='center')
    
    # Creating textboxes for Moving sin gradient WITHOUT compensation (LINEAR ONLY)
    
        #creating a textbox for spatial frequency
    SpatFreqB = visual.TextBox(window=win,
        text=('Spt Frq: ' + str(SpatFreqValB)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(-2280,425),
        size=(232,37),
        units='pix',
        grid_horz_justification='center',
        grid_vert_justification='center')
    
    #creating a textbox for temporal frequency
    TempFreqB = visual.TextBox(window=win,
        text=('Tmp Frq: ' + str(tempFreqValB)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(-2040,425),
        size=(232,37),
        units='pix',
        grid_horz_justification='center',
        grid_vert_justification='center')
    
    #creating a textbox for time before the stimulation
    t_BeforeB = visual.TextBox(window=win,
        text=('T_Bef: '+ str(t_beforeValB)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(-1560,425),
        size=(232,37),
        units='pix',
        grid_horz_justification='center',
        grid_vert_justification='center')
        
    #creating a textbox for duration of stimulation
    t_stimB = visual.TextBox(window=win,
        text=('T_ Dur: ' + str(t_stimValB)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(-1320,425),
        size=(232,37),
        units='pix',
        grid_horz_justification='center',
        grid_vert_justification='center')
        
    #creating a textbox for the time after the stimulation
    t_afterB = visual.TextBox(
        window=win,
        text=('T_Aft: ' + str(t_afterValB)),
        font_size = fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(-1080,425),
        size=(232,37),
        units='pix',
        grid_horz_justification='center',
        grid_vert_justification='center')
    
    #creating a Synch textbox
    synchB = visual.TextBox(
        window=win,
        text=('Synch:' + str(syncVal)),
        font_size = fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(-2520,425),
        size=(232,37),
        units='pix',
        grid_horz_justification='center',
        grid_vert_justification='center')
    
    #creating a moationMode textbox
    mtnmodeB = visual.TextBox(
        window=win,
        text=("Motn Mode: " + str(MotionmodeB)),
        font_size = fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(-1800,425),
        size=(232,37),
        units='pix',
        grid_horz_justification='center',
        grid_vert_justification='center')
    
    #creating a name textbox
    NameB = visual.TextBox(
        window=win,
        text=("FLAT sin Grdnt"),
        font_size = fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(-2760 ,425),
        size=(232,37),
        units='pix',
        grid_horz_justification='center',
        grid_vert_justification='center')
    
    #This is where we create the necessary buttons
    
    #Create buttons for CURVED sin gradient stimulation
    
    #Spatial Frequency Butrrons
    SpatFreqBut = visual.ShapeStim(
        win = win, 
        units = "pix", 
        fillColor = [0,0,0],
        size = 1,
        ori = 0, 
        pos= (-2280, 475), 
        opacity = 0, 
        vertices = ((-120, -18), (-120, 18), (120, 18), (120,-18))
        )
    #Temporal Frequency Buttons
    TempFreqBut = visual.ShapeStim(
        win = win, 
        units = "pix", 
        fillColor = [0,0,0],
        size = 1,
        ori = 0, 
        pos = (-2040,475), 
        opacity = 0, 
        vertices = ((-120, -18), (-120, 18), (120, 18), (120,-18))
        )
    
    #Time Before stimulation Buttons
    t_beforeBut = visual.ShapeStim(
        win = win, 
        units = "pix", 
        fillColor = [0,0,0],
        size = 1,
        ori = 180, 
        pos=(-1560,475), 
        opacity = 0, 
        vertices = ((-120, -18), (-120, 18), (120, 18), (120,-18))
        )
        
    t_stimBut = visual.ShapeStim(
        win = win, 
        units = "pix", 
        fillColor = [0,0,0],
        size = 1,
        ori = 180,
        pos=(-1320,475), 
        opacity = 0, 
        vertices = ((-120, -18), (-120, 18), (120, 18), (120,-18))
        )
    
    #time After stimulation Buttons
    t_afterBut = visual.ShapeStim(
        win = win, 
        units = "pix", 
        fillColor = [0,0,0],
        size = 1,
        ori = 0, 
        pos = (-1080,475), 
        opacity = 0, 
        vertices = ((-120, -18), (-120, 18), (120, 18), (120,-18))
        )
    #Synch button
    synchBut = visual.ShapeStim(
        win = win, 
        units = "pix", 
        fillColor = [0,0,0],
        size = 1,
        ori = 0, 
        pos = (-2520,475), 
        opacity = 0, 
        vertices = ((-120, -18), (-120, 18), (120, 18), (120,-18))
        )
    
    #motion mode button
    mtnModeBut = visual.ShapeStim(
        win = win, 
        units = "pix", 
        fillColor = [0,0,0],
        size = 1,
        ori = 0, 
        pos = (-1800,475), 
        opacity = 0, 
        vertices = ((-120, -18), (-120, 18), (120, 18), (120,-18))
        )
    
    #moving sin gradient start button
    mvnSinGrdnt = visual.ShapeStim(
        win = win, 
        units = "pix", 
        fillColor = [0,0,0],
        size = 1,
        ori = 0, 
        pos = (-2760 ,475), 
        opacity = 0, 
        vertices = ((-120, -18), (-120, 18), (120, 18), (120,-18))
        )
    
    #Create buttons for FLAT sin gradient stimulation
    
    #Spatial Frequency Buttrons
    SpatFreqButB = visual.ShapeStim(
        win = win, 
        units = "pix", 
        fillColor = [0,0,0],
        size = 1,
        ori = 0, 
        pos= (-2280, 425), 
        opacity = 0, 
        vertices = ((-120, -18), (-120, 18), (120, 18), (120,-18))
        )
    #Temporal Frequency Buttons
    TempFreqButB = visual.ShapeStim(
        win = win, 
        units = "pix", 
        fillColor = [0,0,0],
        size = 1,
        ori = 0, 
        pos = (-2040,425), 
        opacity = 0, 
        vertices = ((-120, -18), (-120, 18), (120, 18), (120,-18))
        )
    
    #Time Before stimulation Buttons
    t_beforeButB = visual.ShapeStim(
        win = win, 
        units = "pix", 
        fillColor = [0,0,0],
        size = 1,
        ori = 180, 
        pos=(-1560,425), 
        opacity = 0, 
        vertices = ((-120, -18), (-120, 18), (120, 18), (120,-18))
        )
        
    t_stimButB = visual.ShapeStim(
        win = win, 
        units = "pix", 
        fillColor = [0,0,0],
        size = 1,
        ori = 180,
        pos=(-1320,425), 
        opacity = 0, 
        vertices = ((-120, -18), (-120, 18), (120, 18), (120,-18))
        )
    
    #time After stimulation Buttons
    t_afterButB = visual.ShapeStim(
        win = win, 
        units = "pix", 
        fillColor = [0,0,0],
        size = 1,
        ori = 0, 
        pos = (-1080,425), 
        opacity = 0, 
        vertices = ((-120, -18), (-120, 18), (120, 18), (120,-18))
        )
    #Synch button
    synchButB = visual.ShapeStim(
        win = win, 
        units = "pix", 
        fillColor = [0,0,0],
        size = 1,
        ori = 0, 
        pos = (-2520,425), 
        opacity = 0, 
        vertices = ((-120, -18), (-120, 18), (120, 18), (120,-18))
        )
    
    #motion mode button
    mtnModeButB = visual.ShapeStim(
        win = win, 
        units = "pix", 
        fillColor = [0,0,0],
        size = 1,
        ori = 0, 
        pos = (-1800,425), 
        opacity = 0, 
        vertices = ((-120, -18), (-120, 18), (120, 18), (120,-18))
        )
    
    #moving sin gradient start button
    mvnSinGrdntB = visual.ShapeStim(
        win = win, 
        units = "pix", 
        fillColor = [0,0,0],
        size = 1,
        ori = 0, 
        pos = (-2760 ,425), 
        opacity = 0, 
        vertices = ((-120, -18), (-120, 18), (120, 18), (120,-18))
        )
    
    
    #drawing the textboxes
    t_after.draw()
    t_stim.draw()
    t_Before.draw()
    TempFreq.draw()
    SpatFreq.draw()
    Name.draw()
    synch.draw()
    mtnmode.draw()
    t_afterB.draw()
    t_stimB.draw()
    t_BeforeB.draw()
    TempFreqB.draw()
    SpatFreqB.draw()
    NameB.draw()
    synchB.draw()
    mtnmodeB.draw()
    
    #drawing the buttons
    mvnSinGrdnt.draw()
    t_stimBut.draw()
    t_afterBut.draw()
    t_beforeBut.draw()
    TempFreqBut.draw()
    SpatFreqBut.draw()
    synchBut.draw()
    mtnModeBut.draw()
    mvnSinGrdntB.draw()
    t_stimButB.draw()
    t_afterButB.draw()
    t_beforeButB.draw()
    TempFreqButB.draw()
    SpatFreqButB.draw()
    synchButB.draw()
    mtnModeButB.draw()
    
    #drawing squares
    square1.draw()
    square2.draw()
    
    #flipping the window to display the textboxes and buttons
    win.flip()

    mouse = event.Mouse(
        visible = True, 
        win = win
        )
    
    keep_going = True
    
    #this loop is to 
    while keep_going:
        psychopy.core.wait(0.05)
        currMouse = mouse.getPressed()
        
        keys = event.getKeys() #this will retrieve key presses from the buffer and place them into a list (in the order that they were pressed)
        
        if mouse.isPressedIn(synchBut) and currMouse[0] == 1:
            syncVal = VS.VS("syncStat", 1, syncVal)
            synch = visual.TextBox(
                window=win,
                text=('Synch:' + str(syncVal)),
                font_size = fontSize,
                font_color=fontClr,
                border_color = boarderClr,
                pos=(-2520,475),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
        
        elif mouse.isPressedIn(synchBut) and currMouse[2] == 1:
            syncVal = VS.VS("syncStat", 0, syncVal)
            synch = visual.TextBox(
                window=win,
                text=('Synch:' + str(syncVal)),
                font_size = fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos=(-2520,475),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
    
        elif mouse.isPressedIn(t_stimBut) and currMouse[2]==1:
            t_stimVal = VS.VS("Duration of Stimulation", 0, t_stimVal)
            t_stim = visual.TextBox(window=win,
                text=('T_Dur: ' + str(t_stimVal)),
                font_size=fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos=(-1320,475),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
        
        elif mouse.isPressedIn(t_stimBut) and currMouse[0]==1:
            t_stimVal = VS.VS("Duration of Stimulation", 1, t_stimVal)
            t_stim = visual.TextBox(window=win,
                text=('T_Dur: ' + str(t_stimVal)),
                font_size=fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos=(-1320,475),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
    
        elif mouse.isPressedIn(t_afterBut) and currMouse[0]==1:
            t_afterVal= VS.VS("Time After Stimulation", 1, t_afterVal)
            t_after = visual.TextBox(
                window=win,
                text=('T_Aft: ' + str(t_afterVal)),
                font_size = fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos=(-1080,475),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
    
        elif mouse.isPressedIn(t_afterBut) and currMouse[2]==1:
            t_afterVal= VS.VS("Time After Stimulation", 0, t_afterVal)
            t_after = visual.TextBox(
                window=win,
                text=('T_Aft: ' + str(t_afterVal)),
                font_size = fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos=(-1080,475),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
    
        elif mouse.isPressedIn(t_beforeBut) and currMouse[2]==1:
            t_beforeVal = VS.VS("Time before Stimulation", 0, t_beforeVal)
            t_Before = visual.TextBox(window=win,
                text=('T_Bef: '+ str(t_beforeVal)),
                font_size=fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos=(-1560,475),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
    
        elif mouse.isPressedIn(t_beforeBut) and currMouse[0]==1:
            t_beforeVal = VS.VS("Time before Stimulation", 1, t_beforeVal)
            t_Before = visual.TextBox(window=win,
                text=('T_Bef: '+ str(t_beforeVal)),
                font_size=fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos=(-1560,475),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
    
        elif mouse.isPressedIn(TempFreqBut) and currMouse[2]==1:
            tempFreqVal= VS.VS("Temporal Frequency", 0, tempFreqVal)
            TempFreq = visual.TextBox(window=win,
                text=('Tmp Frq: ' + str(tempFreqVal)),
                font_size=fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos=(-2040,475),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
    
    
        elif mouse.isPressedIn(TempFreqBut) and currMouse[0]==1:
            tempFreqVal= VS.VS("Temporal Frequency", 1, tempFreqVal)
            TempFreq = visual.TextBox(window=win,
                text=('Tmp Frq: ' + str(tempFreqVal)),
                font_size=fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos=(-2040,475),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
    
        elif mouse.isPressedIn(SpatFreqBut) and currMouse[2]==1:
            SpatFreqVal = VS.VS("Spatial Frequency", 0, SpatFreqVal)
            SpatFreq = visual.TextBox(window=win,
                text=('Spt Frq: ' + str(SpatFreqVal)),
                font_size=fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos=(-2280,475),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
    
        elif mouse.isPressedIn(SpatFreqBut) and currMouse[0]==1:
            SpatFreqVal = VS.VS("Spatial Frequency", 1, SpatFreqVal)
            SpatFreq = visual.TextBox(window=win,
                text=('Spt Frq: ' + str(SpatFreqVal)),
                font_size=fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos= (-2280,475),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
        
        elif mouse.isPressedIn(mtnModeBut) and currMouse[2]==1:
            Motionmode = VS.VS("Motionmode", 0, Motionmode)
            mtnmode = visual.TextBox(
                window=win,
                text=("Motn Mode: " + str(Motionmode)),
                font_size = fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos=(-1800,475),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
    
        elif mouse.isPressedIn(mtnModeBut) and currMouse[0]==1:
            Motionmode = VS.VS("Motionmode", 1, Motionmode)
            mtnmode = visual.TextBox(
                window=win,
                text=("Motn Mode: " + str(Motionmode)),
                font_size = fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos=(-1800,475),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
        
        elif mouse.isPressedIn(mvnSinGrdnt) and currMouse[0] == 1:
            standBy.draw()
            square1.fillColor = [-1,-1,-1]
            square2.fillColor = [-1,-1,-1]
            square1.draw()
            square2.draw()
            win.flip()
            stimulation.stimulation(SpatFreqVal, tempFreqVal, t_beforeVal, t_stimVal, t_afterVal, winWidth, winHeight, win, syncVal, Motionmode)
            keys = event.getKeys() #retrieving key presses from the buffer during the stimulation
            keys = [] #clearing the key presses
            square1.fillColor = [-1,-1,-1]
            square2.fillColor = [-1,-1,-1]
            square1.draw()
            square2.draw()
            win.flip()
        #For PLANAR 
        elif mouse.isPressedIn(synchButB) and currMouse[0] == 1:
            syncValB = VS.VS("syncStatB", 1, syncValB)
            synchB = visual.TextBox(
                window=win,
                text=('Synch:' + str(syncValB)),
                font_size = fontSize,
                font_color=fontClr,
                border_color = boarderClr,
                pos=(-2520,425),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
        
        elif mouse.isPressedIn(synchButB) and currMouse[2] == 1:
            syncValB = VS.VS("syncStatB", 0, syncValB)
            synchB = visual.TextBox(
                window=win,
                text=('Synch:' + str(syncValB)),
                font_size = fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos=(-2520,425),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
    
        elif mouse.isPressedIn(t_stimButB) and currMouse[2]==1:
            t_stimValB = VS.VS("Duration of StimulationB", 0, t_stimValB)
            t_stimB = visual.TextBox(window=win,
                text=('T_Dur: ' + str(t_stimValB)),
                font_size=fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos=(-1320,425),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
        
        elif mouse.isPressedIn(t_stimButB) and currMouse[0]==1:
            t_stimValB = VS.VS("Duration of StimulationB", 1, t_stimValB)
            t_stimB = visual.TextBox(window=win,
                text=('T_Dur: ' + str(t_stimValB)),
                font_size=fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos=(-1320,425),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
    
        elif mouse.isPressedIn(t_afterButB) and currMouse[0]==1:
            t_afterValB= VS.VS("Time After StimulationB", 1, t_afterValB)
            t_afterB = visual.TextBox(
                window=win,
                text=('T_Aft: ' + str(t_afterValB)),
                font_size = fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos=(-1080,425),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
    
        elif mouse.isPressedIn(t_afterButB) and currMouse[2]==1:
            t_afterValB= VS.VS("Time After StimulationB", 0, t_afterValB)
            t_afterB = visual.TextBox(
                window=win,
                text=('T_Aft: ' + str(t_afterValB)),
                font_size = fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos=(-1080,425),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
    
        elif mouse.isPressedIn(t_beforeButB) and currMouse[2]==1:
            t_beforeValB = VS.VS("Time before StimulationB", 0, t_beforeValB)
            t_BeforeB = visual.TextBox(window=win,
                text=('T_Bef: '+ str(t_beforeValB)),
                font_size=fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos=(-1560,475),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
    
        elif mouse.isPressedIn(t_beforeButB) and currMouse[0]==1:
            t_beforeValB = VS.VS("Time before StimulationB", 1, t_beforeValB)
            t_BeforeB = visual.TextBox(window=win,
                text=('T_Bef: '+ str(t_beforeValB)),
                font_size=fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos=(-1560,425),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
    
        elif mouse.isPressedIn(TempFreqButB) and currMouse[2]==1:
            tempFreqValB= VS.VS("Temporal FrequencyB", 0, tempFreqValB)
            TempFreqB = visual.TextBox(window=win,
                text=('Tmp Frq: ' + str(tempFreqValB)),
                font_size=fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos=(-2040,425),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
    
    
        elif mouse.isPressedIn(TempFreqButB) and currMouse[0]==1:
            tempFreqValB= VS.VS("Temporal FrequencyB", 1, tempFreqValB)
            TempFreqB = visual.TextBox(window=win,
                text=('Tmp Frq: ' + str(tempFreqValB)),
                font_size=fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos=(-2040,425),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
    
        elif mouse.isPressedIn(SpatFreqButB) and currMouse[2]==1:
            SpatFreqValB = VS.VS("Spatial FrequencyB", 0, SpatFreqValB)
            SpatFreqB = visual.TextBox(window=win,
                text=('Spt Frq: ' + str(SpatFreqValB)),
                font_size=fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos=(-2280,425),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
    
        elif mouse.isPressedIn(SpatFreqButB) and currMouse[0]==1:
            SpatFreqValB = VS.VS("Spatial FrequencyB", 1, SpatFreqValB)
            SpatFreqB = visual.TextBox(window=win,
                text=('Spt Frq: ' + str(SpatFreqValB)),
                font_size=fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos= (-2280,425),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
        
        elif mouse.isPressedIn(mtnModeButB) and currMouse[2]==1:
            MotionmodeB = VS.VS("MotionmodeB", 0, MotionmodeB)
            mtnmodeB = visual.TextBox(
                window=win,
                text=("Motn Mode: " + str(MotionmodeB)),
                font_size = fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos=(-1800,425),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
    
        elif mouse.isPressedIn(mtnModeButB) and currMouse[0]==1:
            MotionmodeB = VS.VS("MotionmodeB", 1, MotionmodeB)
            mtnmodeB = visual.TextBox(
                window=win,
                text=("Motn Mode: " + str(MotionmodeB)),
                font_size = fontSize,
                font_color=fontClr,
                border_color=boarderClr,
                pos=(-1800,425),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
        
        elif mouse.isPressedIn(mvnSinGrdntB) and currMouse[0] == 1:
            standBy.draw()
            square1.fillColor = [-1,-1,-1]
            square2.fillColor = [-1,-1,-1]
            square1.draw()
            square2.draw()
            win.flip()
            stimulationB.stimulation(SpatFreqVal, tempFreqVal, t_beforeVal, t_stimVal, t_afterVal, winWidth, winHeight, win, syncVal, Motionmode, Ori)
            keys = event.getKeys() #retrieving key presses from the buffer during the stimulation
            keys = [] #clearing the key presses
            square1.fillColor = [-1,-1,-1]
            square2.fillColor = [-1,-1,-1]
            square1.draw()
            square2.draw()
            win.flip()
        
        elif keys:
            if keys[0] == 'escape':
                    break
        
        
        #these functions are to draw all the buttons and textboxes
        if sum(currMouse) > 0:
            t_after.draw()
            t_stim.draw()
            t_Before.draw()
            TempFreq.draw()
            SpatFreq.draw()
            synch.draw()
            Name.draw()
            mtnmode.draw()
            square1.draw()
            square2.draw()
            t_afterB.draw()
            t_stimB.draw()
            t_BeforeB.draw()
            TempFreqB.draw()
            SpatFreqB.draw()
            NameB.draw()
            synchB.draw()
            mtnmodeB.draw()
            win.flip()
        

    win.close()

front()
