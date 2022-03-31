
def front():
    
    import psychopy.event
    import math
    import numpy as np
    import psychopy.core
    import VS
    import stimulation
    import socket
    from psychopy import visual
    from psychopy import visual, event
    from init_para import *
    
    #Moving Sin gradient Parameters
    SpatFreqVal = 0.1
    tempFreqVal = 1
    t_beforeVal = 0
    t_stimVal = 5
    t_afterVal = 0
    Motionmode = 1 #0 refers to linear motion and 1 refers to sinusoidal motion
    
    #creating a textbox for spatial frequency
    SpatFreq = visual.TextBox(window=win,
        text=('Spt Frq: ' + str(SpatFreqVal)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(-1080,475),
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
        pos=(-2520,475),
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
        pos=(-2280,475),
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
        pos=(-2040,475),
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
        pos=(-1800,475),
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
        pos=(-1560,475),
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
        pos=(-1320,475),
        size=(232,37),
        units='pix',
        grid_horz_justification='center',
        grid_vert_justification='center')
    
    #creating a name textbox
    Name = visual.TextBox(
        window=win,
        text=("Mov1n sin Grdnt"),
        font_size = fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(-2760 ,475),
        size=(232,37),
        units='pix',
        grid_horz_justification='center',
        grid_vert_justification='center')
    
    
    
    #This is where we create the necessary buttons
    
    #Spatial Frequency Butrrons
    SpatFreqBut = visual.ShapeStim(
        win = win, 
        units = "pix", 
        fillColor = [0,0,0],
        size = 1,
        ori = 0, 
        pos= (-1080, 475), 
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
        pos = (-2520,475), 
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
        pos=(-2280,475), 
        opacity = 0, 
        vertices = ((-120, -18), (-120, 18), (120, 18), (120,-18))
        )
        
    t_stimBut = visual.ShapeStim(
        win = win, 
        units = "pix", 
        fillColor = [0,0,0],
        size = 1,
        ori = 180,
        pos=(-2040,475), 
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
        pos = (-1800,475), 
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
        pos = (-1560,475), 
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
        pos = (-1320,475), 
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
    
    
    #drawing the textboxes
    t_after.draw()
    t_stim.draw()
    t_Before.draw()
    TempFreq.draw()
    SpatFreq.draw()
    Name.draw()
    synch.draw()
    mtnmode.draw()
    
    
    #drawing the buttons
    mvnSinGrdnt.draw()
    t_stimBut.draw()
    t_afterBut.draw()
    t_beforeBut.draw()
    TempFreqBut.draw()
    SpatFreqBut.draw()
    synchBut.draw()
    mtnModeBut.draw()

    
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
        
        keys = event.getKeys()
        
        if mouse.isPressedIn(synchBut) and currMouse[0] == 1:
            syncVal = VS.VS("syncStat", 1, syncVal)
            synch = visual.TextBox(
                window=win,
                text=('Synch:' + str(syncVal)),
                font_size = fontSize,
                font_color=fontClr,
                border_color = boarderClr,
                pos=(-1560,475),
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
                pos=(-1560,475),
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
                pos=(-2040,475),
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
                pos=(-2040,475),
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
                pos=(-1800,475),
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
                pos=(-1800,475),
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
                pos=(-2280,475),
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
                pos=(-2280,475),
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
                pos=(-2520,475),
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
                pos=(-2520,475),
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
                pos=(-1080,475),
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
                pos= (-1080,475),
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
                pos=(-1320,475),
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
                pos=(-1320,475),
                size=(232,37),
                units='pix',
                grid_horz_justification='center',
                grid_vert_justification='center')
        
        elif mouse.isPressedIn(mvnSinGrdnt) and currMouse[0] == 1:
            stimulation.stimulation(SpatFreqVal, tempFreqVal, t_beforeVal, t_stimVal, t_afterVal, winWidth, winHeight, win, syncVal, Motionmode)
            keys = event.getKeys()
            keys = []
        
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
            win.flip()
        

    win.close()

front()
