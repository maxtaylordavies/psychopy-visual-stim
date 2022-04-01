import numpy as np
from psychopy import core, visual, event
import VS
import drumgrating
import movSinGrat_tuning
import movSinGrat_tuning_fix
import EYE_calibration
import socket
from init_para import *
import TestNov
import Vdrumgrating_OA
import Rf6x8
import os
import crossline


def front():
    global drumgrating_tempFreqVal
    global drumgrating_SpatFreqVal
    global drumgrating_t_beforeVal
    global drumgrating_t_DuringVal
    global drumgrating_t_afterVal
    global drumgrating_syncVal
    global drumgrating_Motionmode
    global MovSinGrat_Motionmode
    global MovSinGrat_SpatFreqVal
    global MovSinGrat_tempFreqVal
    global MovSinGrat_t_beforeVal
    global MovSinGrat_t_stimVal
    global MovSinGrat_t_afterVal
    global MovSinGrat_contrast
    global MovSinGrat_ori
    global MovSinGrat_syncVal
    global MovSinGrat_ledstate
    global MovSinGrat_features
    global MovSinGrat_Rep
    global calibration_syncVal
    # CREATING TEXTBOXES

    # DRUMGRATING

    # creating a name textbox
    Name_Obj = visual.TextBox(
        window=win,
        text=("Movn sin Grdnt"),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(origin_x + 0.5 * front_textbox_size[0], origin_y - button_init_y),
        size=front_textbox_size,
        units="norm",
        grid_horz_justification="center",
        grid_vert_justification="center",
    )

    # creating a textbox for temporal frequency
    TempFreq_Obj = visual.TextBox(
        window=win,
        text=("Tmp Frq: " + str(drumgrating_tempFreqVal)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(origin_x + 1.5 * front_textbox_size[0], origin_y - button_init_y),
        size=front_textbox_size,
        units="norm",
        grid_horz_justification="center",
        grid_vert_justification="center",
    )

    # creating a textbox for spatial frequency
    SpatFreq_Obj = visual.TextBox(
        window=win,
        text=("Spt Frq: " + str(drumgrating_SpatFreqVal)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        units="norm",
        pos=(origin_x + 2.5 * front_textbox_size[0], origin_y - button_init_y),
        size=front_textbox_size,
        grid_horz_justification="center",
        grid_vert_justification="center",
    )

    # creating a textbox for time before the stimulation
    t_Before_Obj = visual.TextBox(
        window=win,
        text=("T_Bef: " + str(drumgrating_t_beforeVal)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(origin_x + 3.5 * front_textbox_size[0], origin_y - button_init_y),
        size=front_textbox_size,
        units="norm",
        grid_horz_justification="center",
        grid_vert_justification="center",
    )

    # creating a textbox for duration of stimulation
    t_stim_Obj = visual.TextBox(
        window=win,
        text=("T_Dur: " + str(drumgrating_t_DuringVal)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(origin_x + 4.5 * front_textbox_size[0], origin_y - button_init_y),
        size=front_textbox_size,
        units="norm",
        grid_horz_justification="center",
        grid_vert_justification="center",
    )

    # creating a textbox for the time after the stimulation
    t_after_Obj = visual.TextBox(
        window=win,
        text=("T_Aft: " + str(drumgrating_t_afterVal)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(origin_x + 5.5 * front_textbox_size[0], origin_y - button_init_y),
        size=front_textbox_size,
        units="norm",
        grid_horz_justification="center",
        grid_vert_justification="center",
    )

    # creating a Synch textbox
    synch_ObjDRUM = visual.TextBox(
        window=win,
        text=("Synch:" + str(drumgrating_syncVal)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(origin_x + 6.5 * front_textbox_size[0], origin_y - button_init_y),
        size=front_textbox_size,
        units="norm",
        grid_horz_justification="center",
        grid_vert_justification="center",
    )

    # creating a moationMode textbox
    mtnmode_Obj = visual.TextBox(
        window=win,
        text=("Motn Mode: " + str(drumgrating_Motionmode)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(origin_x + 7.5 * front_textbox_size[0], origin_y - button_init_y),
        size=front_textbox_size,
        units="norm",
        grid_horz_justification="center",
        grid_vert_justification="center",
    )

    # ANGLE ORIENTATION

    # creating a name textbox
    Name_ObjORI = visual.TextBox(
        window=win,
        text=("Movn ORI Grdnt"),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(
            origin_x + 0.5 * front_textbox_size[0],
            origin_y - button_init_y - 1 * (front_textbox_size[1] + button_spacing),
        ),
        size=front_textbox_size,
        units="norm",
        grid_horz_justification="center",
        grid_vert_justification="center",
    )

    # creating a textbox for temporal frequency
    TempFreq_ObjORI = visual.TextBox(
        window=win,
        text=("Tmp Frq: " + str(MovSinGrat_tempFreqVal)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(
            origin_x + 2.5 * front_textbox_size[0],
            origin_y - button_init_y - 1 * (front_textbox_size[1] + button_spacing),
        ),
        size=front_textbox_size,
        units="norm",
        grid_horz_justification="center",
        grid_vert_justification="center",
    )

    # creating a textbox for spatial frequency
    SpatFreq_ObjORI = visual.TextBox(
        window=win,
        text=("Spt Frq: " + str(MovSinGrat_SpatFreqVal)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        units="norm",
        pos=(
            origin_x + 3.5 * front_textbox_size[0],
            origin_y - button_init_y - 1 * (front_textbox_size[1] + button_spacing),
        ),
        size=front_textbox_size,
        grid_horz_justification="center",
        grid_vert_justification="center",
    )

    # creating a textbox for time before the stimulation
    t_Before_ObjORI = visual.TextBox(
        window=win,
        text=("T_Bef: " + str(MovSinGrat_t_beforeVal)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(
            origin_x + 4.5 * front_textbox_size[0],
            origin_y - button_init_y - 1 * (front_textbox_size[1] + button_spacing),
        ),
        size=front_textbox_size,
        units="norm",
        grid_horz_justification="center",
        grid_vert_justification="center",
    )

    # creating a textbox for duration of stimulation
    t_stim_ObjORI = visual.TextBox(
        window=win,
        text=("T_Dur: " + str(MovSinGrat_t_stimVal)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(
            origin_x + 5.5 * front_textbox_size[0],
            origin_y - button_init_y - 1 * (front_textbox_size[1] + button_spacing),
        ),
        size=front_textbox_size,
        units="norm",
        grid_horz_justification="center",
        grid_vert_justification="center",
    )

    # creating a textbox for the time after the stimulation
    t_after_ObjORI = visual.TextBox(
        window=win,
        text=("T_Aft: " + str(MovSinGrat_t_afterVal)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(
            origin_x + 6.5 * front_textbox_size[0],
            origin_y - button_init_y - 1 * (front_textbox_size[1] + button_spacing),
        ),
        size=front_textbox_size,
        units="norm",
        grid_horz_justification="center",
        grid_vert_justification="center",
    )

    # creating a Synch textbox
    synch_ObjORI = visual.TextBox(
        window=win,
        text=("Synch:" + str(MovSinGrat_syncVal)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(
            origin_x + 7.5 * front_textbox_size[0],
            origin_y - button_init_y - 1 * (front_textbox_size[1] + button_spacing),
        ),
        size=front_textbox_size,
        units="norm",
        grid_horz_justification="center",
        grid_vert_justification="center",
    )

    # creating a moationMode textbox
    mtnmode_ObjORI = visual.TextBox(
        window=win,
        text=("Motn Mode: " + str(MovSinGrat_Motionmode)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(
            origin_x + 8.5 * front_textbox_size[0],
            origin_y - button_init_y - 1 * (front_textbox_size[1] + button_spacing),
        ),
        size=front_textbox_size,
        units="norm",
        grid_horz_justification="center",
        grid_vert_justification="center",
    )

    # creating a ledstate textbox
    ledstate_Obj = visual.TextBox(
        window=win,
        text=("Ledstate: " + str(MovSinGrat_ledstate)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(
            origin_x + 9.5 * front_textbox_size[0],
            origin_y - button_init_y - 1 * (front_textbox_size[1] + button_spacing),
        ),
        size=front_textbox_size,
        units="norm",
        grid_horz_justification="center",
        grid_vert_justification="center",
    )

    # creating a tuning textbox
    MovSinGrat_Tuning_Obj = visual.TextBox(
        window=win,
        text=("Feature: " + str(MovSinGrat_features)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(
            origin_x + 1.5 * front_textbox_size[0],
            origin_y - button_init_y - 1 * (front_textbox_size[1] + button_spacing),
        ),
        size=front_textbox_size,
        units="norm",
        grid_horz_justification="center",
        grid_vert_justification="center",
    )

    # creating a repetition textbox
    MovSinGrat_Rep_Obj = visual.TextBox(
        window=win,
        text=("Rep: " + str(MovSinGrat_Rep)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(
            origin_x + 10.5 * front_textbox_size[0],
            origin_y - button_init_y - 1 * (front_textbox_size[1] + button_spacing),
        ),
        size=front_textbox_size,
        units="norm",
        grid_horz_justification="center",
        grid_vert_justification="center",
    )

    # creating a  textbox for calibration code
    Calibration_Obj = visual.TextBox(
        window=win,
        text=("Calibration"),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(
            origin_x + 0.5 * front_textbox_size[0],
            origin_y - button_init_y - 2 * (front_textbox_size[1] + button_spacing),
        ),
        size=front_textbox_size,
        units="norm",
        grid_horz_justification="center",
        grid_vert_justification="center",
    )
    # create a textbox for calibration synch
    CalibrationSync_Obj = visual.TextBox(
        window=win,
        text=("Synch:" + str(calibration_syncVal)),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(
            origin_x + 1.5 * front_textbox_size[0],
            origin_y - button_init_y - 2 * (front_textbox_size[1] + button_spacing),
        ),
        size=front_textbox_size,
        units="norm",
        grid_horz_justification="center",
        grid_vert_justification="center",
    )

    Name_vdrumgrating = visual.TextBox(
        window=win,
        text=("VdrumGrating"),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(
            origin_x + 0.5 * front_textbox_size[0],
            origin_y - button_init_y - 3 * (front_textbox_size[1] + button_spacing),
        ),
        size=front_textbox_size,
        units="norm",
        grid_horz_justification="center",
        grid_vert_justification="center",
    )

    # RF 6X8 TEXTBOX
    Name_rf6x8 = visual.TextBox(
        window=win,
        text=("rf 6x8"),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(
            origin_x + 0.5 * front_textbox_size[0],
            origin_y - button_init_y - 4 * (front_textbox_size[1] + button_spacing),
        ),
        size=front_textbox_size,
        units="norm",
        grid_horz_justification="center",
        grid_vert_justification="center",
    )
    Name_crossline = visual.TextBox(
        window=win,
        text=("crossline"),
        font_size=fontSize,
        font_color=fontClr,
        border_color=boarderClr,
        pos=(
            origin_x + 0.5 * front_textbox_size[0],
            origin_y - button_init_y - 5 * (front_textbox_size[1] + button_spacing),
        ),
        size=front_textbox_size,
        units="norm",
        grid_horz_justification="center",
        grid_vert_justification="center",
    )

    # This is where we create the necessary buttons

    # DRUMGRATING

    # moving sin gradient start button
    mvnSinGrdnt = visual.ShapeStim(
        win=win,
        units="norm",
        fillColor=[0, 0, 0],
        ori=0,
        pos=Name_Obj.getPosition(),
        opacity=0,
        vertices=front_button_size,
    )

    # Spatial Frequency Butrrons
    SpatFreqBut = visual.ShapeStim(
        win=win,
        units="norm",
        fillColor=[0, 0, 0],
        ori=0,
        pos=SpatFreq_Obj.getPosition(),
        opacity=0,
        vertices=front_button_size,
    )
    # Temporal Frequency Buttons
    TempFreqBut = visual.ShapeStim(
        win=win,
        units="norm",
        fillColor=[0, 0, 0],
        ori=0,
        pos=TempFreq_Obj.getPosition(),
        opacity=0,
        vertices=front_button_size,
    )

    # Time Before stimulation Buttons
    t_beforeBut = visual.ShapeStim(
        win=win,
        units="norm",
        fillColor=[0, 0, 0],
        ori=180,
        pos=t_Before_Obj.getPosition(),
        opacity=0,
        vertices=front_button_size,
    )

    t_stimBut = visual.ShapeStim(
        win=win,
        units="norm",
        fillColor=[0, 0, 0],
        ori=180,
        pos=t_stim_Obj.getPosition(),
        opacity=0,
        vertices=front_button_size,
    )

    # time After stimulation Buttons
    t_afterBut = visual.ShapeStim(
        win=win,
        units="norm",
        fillColor=[0, 0, 0],
        ori=0,
        pos=t_after_Obj.getPosition(),
        opacity=0,
        vertices=front_button_size,
    )
    # Synch button
    synchButDRUM = visual.ShapeStim(
        win=win,
        units="norm",
        fillColor=[0, 0, 0],
        ori=0,
        pos=synch_ObjDRUM.getPosition(),
        opacity=0,
        vertices=front_button_size,
    )

    # motion mode button
    mtnModeBut = visual.ShapeStim(
        win=win,
        units="norm",
        fillColor=[0, 0, 0],
        ori=0,
        pos=mtnmode_Obj.getPosition(),
        opacity=0,
        vertices=front_button_size,
    )

    # MOVSINGRAT TUNING

    # Tuning button
    MovSinGrat_TuningBut = visual.ShapeStim(
        win=win,
        units="norm",
        fillColor=[0, 0, 0],
        ori=0,
        pos=MovSinGrat_Tuning_Obj.getPosition(),
        opacity=0,
        vertices=front_button_size,
    )

    # Spatial Frequency Butrrons
    SpatFreqButORI = visual.ShapeStim(
        win=win,
        units="norm",
        fillColor=[0, 0, 0],
        ori=0,
        pos=SpatFreq_ObjORI.getPosition(),
        opacity=0,
        vertices=front_button_size,
    )
    # Temporal Frequency Buttons
    TempFreqButORI = visual.ShapeStim(
        win=win,
        units="norm",
        fillColor=[0, 0, 0],
        ori=0,
        pos=TempFreq_ObjORI.getPosition(),
        opacity=0,
        vertices=front_button_size,
    )

    # Time Before stimulation Buttons
    t_beforeButORI = visual.ShapeStim(
        win=win,
        units="norm",
        fillColor=[0, 0, 0],
        ori=180,
        pos=t_Before_ObjORI.getPosition(),
        opacity=0,
        vertices=front_button_size,
    )

    t_stimButORI = visual.ShapeStim(
        win=win,
        units="norm",
        fillColor=[0, 0, 0],
        ori=180,
        pos=t_stim_ObjORI.getPosition(),
        opacity=0,
        vertices=front_button_size,
    )

    # time After stimulation Buttons
    t_afterButORI = visual.ShapeStim(
        win=win,
        units="norm",
        fillColor=[0, 0, 0],
        ori=0,
        pos=t_after_ObjORI.getPosition(),
        opacity=0,
        vertices=front_button_size,
    )
    # Synch button
    synchButORI = visual.ShapeStim(
        win=win,
        units="norm",
        fillColor=[0, 0, 0],
        ori=0,
        pos=synch_ObjORI.getPosition(),
        opacity=0,
        vertices=front_button_size,
    )

    # motion mode button
    mtnModeButORI = visual.ShapeStim(
        win=win,
        units="norm",
        fillColor=[0, 0, 0],
        ori=0,
        pos=mtnmode_ObjORI.getPosition(),
        opacity=0,
        vertices=front_button_size,
    )

    # moving sin gradient start button
    mvnSinGrdntORI = visual.ShapeStim(
        win=win,
        units="norm",
        fillColor=[0, 0, 0],
        ori=0,
        pos=Name_ObjORI.getPosition(),
        opacity=0,
        vertices=front_button_size,
    )

    # ledflag button
    ledstateBut = visual.ShapeStim(
        win=win,
        units="norm",
        fillColor=[0, 0, 0],
        ori=0,
        pos=ledstate_Obj.getPosition(),
        opacity=0,
        vertices=front_button_size,
    )

    # rep button
    RepBut = visual.ShapeStim(
        win=win,
        units="norm",
        fillColor=[0, 0, 0],
        ori=0,
        pos=MovSinGrat_Rep_Obj.getPosition(),
        opacity=0,
        vertices=front_button_size,
    )

    # calibration start button
    calibration_button = visual.ShapeStim(
        win=win,
        units="norm",
        fillColor=[0, 0, 0],
        ori=0,
        pos=Calibration_Obj.getPosition(),
        opacity=0,
        vertices=front_button_size,
    )
    # calibration synch button  added>>>>>>>>>>>>>>>>>>>>>
    CalibrationSynch_button = visual.ShapeStim(
        win=win,
        units="norm",
        fillColor=[0, 0, 0],
        ori=0,
        pos=CalibrationSync_Obj.getPosition(),
        opacity=0,
        vertices=front_button_size,
    )

    # drumgrating with mask, direcitional split, and rotation
    vdrumGrating_But = visual.ShapeStim(
        win=win,
        units="norm",
        fillColor=[0, 0, 0],
        ori=0,
        pos=Name_vdrumgrating.getPosition(),
        opacity=0,
        vertices=front_button_size,
    )

    rf6x8_But = visual.ShapeStim(
        win=win,
        units="norm",
        fillColor=[0, 0, 0],
        ori=0,
        pos=Name_rf6x8.getPosition(),
        opacity=0,
        vertices=front_button_size,
    )
    crossline_But = visual.ShapeStim(
        win=win,
        units="norm",
        fillColor=[0, 0, 0],
        ori=0,
        pos=Name_crossline.getPosition(),
        opacity=0,
        vertices=front_button_size,
    )

    # drawing the textboxes
    t_after_Obj.draw()
    t_stim_Obj.draw()
    t_Before_Obj.draw()
    TempFreq_Obj.draw()
    SpatFreq_Obj.draw()
    Name_Obj.draw()
    synch_ObjDRUM.draw()
    mtnmode_Obj.draw()
    t_after_ObjORI.draw()
    t_stim_ObjORI.draw()
    t_Before_ObjORI.draw()
    TempFreq_ObjORI.draw()
    SpatFreq_ObjORI.draw()
    Name_ObjORI.draw()
    synch_ObjORI.draw()
    mtnmode_ObjORI.draw()
    ledstate_Obj.draw()
    MovSinGrat_Tuning_Obj.draw()
    Calibration_Obj.draw()
    CalibrationSync_Obj.draw()  # added>>>>>>>>>>>>>>>>>>>>>>>>>
    Name_vdrumgrating.draw()
    Name_rf6x8.draw()
    MovSinGrat_Rep_Obj.draw()
    Name_crossline.draw()

    # drawing the buttons
    mvnSinGrdnt.draw()
    t_stimBut.draw()
    t_afterBut.draw()
    t_beforeBut.draw()
    TempFreqBut.draw()
    SpatFreqBut.draw()
    synchButDRUM.draw()
    mtnModeBut.draw()
    mvnSinGrdntORI.draw()
    t_stimButORI.draw()
    t_afterButORI.draw()
    t_beforeButORI.draw()
    TempFreqButORI.draw()
    SpatFreqButORI.draw()
    synchButORI.draw()
    mtnModeButORI.draw()
    ledstateBut.draw()
    MovSinGrat_TuningBut.draw()
    calibration_button.draw()
    CalibrationSynch_button.draw()  # added>>>>>>>>>>>>>>>>>>>>a
    vdrumGrating_But.draw()
    rf6x8_But.draw()
    RepBut.draw()
    crossline_But.draw()

    # drawing squares
    square1.draw()
    square2.draw()

    # flipping the window to display the textboxes and buttons
    win.flip()

    mouse = event.Mouse(visible=True, win=win)

    keep_going = True

    # this loop is to
    while keep_going:
        psychopy.core.wait(0.1)
        currMouse = mouse.getPressed()

        keys = (
            event.getKeys()
        )  # this will retrieve key presses from the buffer and place them into a list (in the order that they were pressed)

        if (mouse.isPressedIn(mvnSinGrdnt) and currMouse[0] == 1) or (
            keys and keys[0] == drumgrating_hotkey
        ):  # modified >>>>>>>>>>>>>>>>>>>>>>>>>>>>
            square1.fillColor = [-1, -1, -1]
            square2.fillColor = [-1, -1, -1]
            square1.draw()
            square2.draw()
            win.flip()
            drumgrating.drumgrating(
                win,
                drumgrating_SpatFreqVal,
                drumgrating_tempFreqVal,
                drumgrating_t_beforeVal,
                drumgrating_t_DuringVal,
                drumgrating_t_afterVal,
                drumgrating_syncVal,
                drumgrating_Motionmode,
            )
            # add orientation values:  angle0, angle1, randomseq, ledstate)
            #            keys = event.getKeys() #retrieving key presses from the buffer during the stimulation
            #            keys = [] #clearing the key presses
            square1.fillColor = [-1, -1, -1]
            square2.fillColor = [-1, -1, -1]
            square1.draw()
            square2.draw()
            win.flip()

        elif mouse.isPressedIn(synchButDRUM) and currMouse[0] == 1:
            drumgrating_syncVal = VS.VS("syncStat", 1, drumgrating_syncVal)
            synch_ObjDRUM.setText("Synch:" + str(drumgrating_syncVal))

        elif mouse.isPressedIn(synchButDRUM) and currMouse[2] == 1:
            drumgrating_syncVal = VS.VS("syncStat", 0, drumgrating_syncVal)
            synch_ObjDRUM.setText("Synch:" + str(drumgrating_syncVal))

        elif mouse.isPressedIn(t_stimBut) and currMouse[2] == 1:
            drumgrating_t_DuringVal = VS.VS(
                "Duration of Stimulation", 0, drumgrating_t_DuringVal
            )
            t_stim_Obj.setText("T_Dur: " + str(drumgrating_t_DuringVal)),

        elif mouse.isPressedIn(t_stimBut) and currMouse[0] == 1:
            drumgrating_t_DuringVal = VS.VS(
                "Duration of Stimulation", 1, drumgrating_t_DuringVal
            )
            t_stim_Obj.setText("T_Dur: " + str(drumgrating_t_DuringVal))

        elif mouse.isPressedIn(t_afterBut) and currMouse[0] == 1:
            drumgrating_t_afterVal = VS.VS(
                "Time After Stimulation", 1, drumgrating_t_afterVal
            )
            t_after_Obj.setText("T_Aft: " + str(drumgrating_t_afterVal))

        elif mouse.isPressedIn(t_afterBut) and currMouse[2] == 1:
            drumgrating_t_afterVal = VS.VS(
                "Time After Stimulation", 0, drumgrating_t_afterVal
            )
            t_after_Obj.setText("T_Aft: " + str(drumgrating_t_afterVal))

        elif mouse.isPressedIn(t_beforeBut) and currMouse[2] == 1:
            drumgrating_t_beforeVal = VS.VS(
                "Time before Stimulation", 0, drumgrating_t_beforeVal
            )
            t_Before_Obj.setText("T_Bef: " + str(drumgrating_t_beforeVal))

        elif mouse.isPressedIn(t_beforeBut) and currMouse[0] == 1:
            drumgrating_t_beforeVal = VS.VS(
                "Time before Stimulation", 1, drumgrating_t_beforeVal
            )
            t_Before_Obj.setText("T_Bef: " + str(drumgrating_t_beforeVal))

        elif mouse.isPressedIn(TempFreqBut) and currMouse[2] == 1:
            drumgrating_tempFreqVal = VS.VS(
                "Temporal Frequency", 0, drumgrating_tempFreqVal
            )
            TempFreq_Obj.setText("Tmp Frq: " + str(drumgrating_tempFreqVal))

        elif mouse.isPressedIn(TempFreqBut) and currMouse[0] == 1:
            drumgrating_tempFreqVal = VS.VS(
                "Temporal Frequency", 1, drumgrating_tempFreqVal
            )
            TempFreq_Obj.setText("Tmp Frq: " + str(drumgrating_tempFreqVal))

        elif mouse.isPressedIn(SpatFreqBut) and currMouse[2] == 1:
            drumgrating_SpatFreqVal = VS.VS(
                "Spatial Frequency", 0, drumgrating_SpatFreqVal
            )
            SpatFreq_Obj.setText("Spt Frq: " + str(drumgrating_SpatFreqVal))

        elif mouse.isPressedIn(SpatFreqBut) and currMouse[0] == 1:
            drumgrating_SpatFreqVal = VS.VS(
                "Spatial Frequency", 1, drumgrating_SpatFreqVal
            )
            SpatFreq_Obj.setText("Spt Frq: " + str(drumgrating_SpatFreqVal))

        elif mouse.isPressedIn(mtnModeBut) and currMouse[2] == 1:
            drumgrating_Motionmode = VS.VS("Motionmode", 0, drumgrating_Motionmode)
            mtnmode_Obj.setText("Motn Mode: " + str(drumgrating_Motionmode))

        elif mouse.isPressedIn(mtnModeBut) and currMouse[0] == 1:
            drumgrating_Motionmode = VS.VS("Motionmode", 1, drumgrating_Motionmode)
            mtnmode_Obj.setText("Motn Mode: " + str(drumgrating_Motionmode))

        elif mouse.isPressedIn(synchButORI) and currMouse[0] == 1:
            MovSinGrat_syncVal = VS.VS("syncStatORI", 1, MovSinGrat_syncVal)
            synch_ObjORI.setText("Synch:" + str(MovSinGrat_syncVal))

        elif mouse.isPressedIn(synchButORI) and currMouse[2] == 1:
            MovSinGrat_syncVal = VS.VS("syncStatORI", 0, MovSinGrat_syncVal)
            synch_ObjORI.setText("Synch:" + str(MovSinGrat_syncVal))

        elif mouse.isPressedIn(t_stimButORI) and currMouse[2] == 1:
            MovSinGrat_t_stimVal = VS.VS(
                "Duration of StimulationORI", 0, MovSinGrat_t_stimVal
            )
            t_stim_ObjORI.setText("T_Dur: " + str(MovSinGrat_t_stimVal)),

        elif mouse.isPressedIn(t_stimButORI) and currMouse[0] == 1:
            MovSinGrat_t_stimVal = VS.VS(
                "Duration of StimulationORI", 1, MovSinGrat_t_stimVal
            )
            t_stim_ObjORI.setText("T_Dur: " + str(MovSinGrat_t_stimVal))

        elif mouse.isPressedIn(t_afterButORI) and currMouse[0] == 1:
            MovSinGrat_t_afterVal = VS.VS(
                "Time After Stimulation", 1, MovSinGrat_t_afterVal
            )
            t_after_ObjORI.setText("T_Aft: " + str(MovSinGrat_t_afterVal))

        elif mouse.isPressedIn(t_afterButORI) and currMouse[2] == 1:
            MovSinGrat_t_afterVal = VS.VS(
                "Time After StimulationORI", 0, MovSinGrat_t_afterVal
            )
            t_after_ObjORI.setText("T_Aft: " + str(MovSinGrat_t_afterVal))

        elif mouse.isPressedIn(t_beforeButORI) and currMouse[2] == 1:
            MovSinGrat_t_beforeVal = VS.VS(
                "Time before StimulationORI", 0, MovSinGrat_t_beforeVal
            )
            t_Before_ObjORI.setText("T_Bef: " + str(MovSinGrat_t_beforeVal))

        elif mouse.isPressedIn(t_beforeButORI) and currMouse[0] == 1:
            MovSinGrat_t_beforeVal = VS.VS(
                "Time before StimulationORI", 1, MovSinGrat_t_beforeVal
            )
            t_Before_ObjORI.setText("T_Bef: " + str(MovSinGrat_t_beforeVal))

        elif mouse.isPressedIn(TempFreqButORI) and currMouse[2] == 1:
            MovSinGrat_tempFreqVal = VS.VS(
                "Temporal FrequencyORI", 0, MovSinGrat_tempFreqVal
            )
            TempFreq_ObjORI.setText("Tmp Frq: " + str(MovSinGrat_tempFreqVal))

        elif mouse.isPressedIn(TempFreqButORI) and currMouse[0] == 1:
            MovSinGrat_tempFreqVal = VS.VS(
                "Temporal FrequencyORI", 1, MovSinGrat_tempFreqVal
            )
            TempFreq_ObjORI.setText("Tmp Frq: " + str(MovSinGrat_tempFreqVal))

        elif mouse.isPressedIn(SpatFreqButORI) and currMouse[2] == 1:
            MovSinGrat_SpatFreqVal = VS.VS(
                "Spatial FrequencyORI", 0, MovSinGrat_SpatFreqVal
            )
            SpatFreq_ObjORI.setText("Spt Frq: " + str(MovSinGrat_SpatFreqVal))

        elif mouse.isPressedIn(SpatFreqButORI) and currMouse[0] == 1:
            MovSinGrat_SpatFreqVal = VS.VS(
                "Spatial FrequencyORI", 1, MovSinGrat_SpatFreqVal
            )
            SpatFreq_ObjORI.setText("Spt Frq: " + str(MovSinGrat_SpatFreqVal))

        elif mouse.isPressedIn(mtnModeButORI) and currMouse[2] == 1:
            MovSinGrat_Motionmode = VS.VS("MotionmodeORI", 0, MovSinGrat_Motionmode)
            mtnmode_ObjORI.setText("Motn Mode: " + str(MovSinGrat_Motionmode))

        elif mouse.isPressedIn(mtnModeButORI) and currMouse[0] == 1:
            MovSinGrat_Motionmode = VS.VS("MotionmodeORI", 1, MovSinGrat_Motionmode)
            mtnmode_ObjORI.setText("Motn Mode: " + str(MovSinGrat_Motionmode))

        elif mouse.isPressedIn(ledstateBut) and currMouse[2] == 1:
            MovSinGrat_ledstate = VS.VS("Ledstate", 0, MovSinGrat_ledstate)
            ledstate_Obj.setText("Ledstate :" + str(MovSinGrat_ledstate))

        elif mouse.isPressedIn(ledstateBut) and currMouse[0] == 1:
            MovSinGrat_ledstate = VS.VS("Ledstate", 1, MovSinGrat_ledstate)
            ledstate_Obj.setText("Ledstate :" + str(MovSinGrat_ledstate))

        elif mouse.isPressedIn(RepBut) and currMouse[2] == 1:
            MovSinGrat_Rep = VS.VS("Rep", 0, MovSinGrat_Rep)
            MovSinGrat_Rep_Obj.setText("Rep :" + str(MovSinGrat_Rep))

        elif mouse.isPressedIn(RepBut) and currMouse[0] == 1:
            MovSinGrat_Rep = VS.VS("Rep", 1, MovSinGrat_Rep)
            MovSinGrat_Rep_Obj.setText("Rep :" + str(MovSinGrat_Rep))

        elif mouse.isPressedIn(MovSinGrat_TuningBut) and currMouse[2] == 1:
            MovSinGrat_features = VS.VS("Tuning feature: ", 0, MovSinGrat_features)
            MovSinGrat_Tuning_Obj.setText("Feature: " + str(MovSinGrat_features))

        elif mouse.isPressedIn(MovSinGrat_TuningBut) and currMouse[0] == 1:
            MovSinGrat_features = VS.VS("Tuning feature: ", 1, MovSinGrat_features)
            MovSinGrat_Tuning_Obj.setText("Feature: " + str(MovSinGrat_features))

        # change to -fix
        elif mouse.isPressedIn(mvnSinGrdntORI) and currMouse[0] == 1:
            square1.fillColor = [-1, -1, -1]
            square2.fillColor = [-1, -1, -1]
            square1.draw()
            square2.draw()
            win.flip()
            movSinGrat_tuning.movSinGrat(
                MovSinGrat_SpatFreqVal,
                MovSinGrat_tempFreqVal,
                MovSinGrat_t_beforeVal,
                MovSinGrat_t_stimVal,
                MovSinGrat_t_afterVal,
                MovSinGrat_syncVal,
                MovSinGrat_Motionmode,
                MovSinGrat_features,
                MovSinGrat_ledstate,
            )  # MovSinGrat_Rep)
            # add orientation values:  angle0, angle1, randomseq, ledstate)
            keys = (
                event.getKeys()
            )  # retrieving key presses from the buffer during the stimulation
            keys = []  # clearing the key presses
            square1.fillColor = [-1, -1, -1]
            square2.fillColor = [-1, -1, -1]
            square1.draw()
            square2.draw()
            win.flip()

        elif mouse.isPressedIn(vdrumGrating_But) and currMouse[0] == 1:
            square1.fillColor = [-1, -1, -1]
            square2.fillColor = [-1, -1, -1]
            square1.draw()
            square2.draw()
            win.flip()
            Vdrumgrating_OA.Vdrumgrating(
                MovSinGrat_SpatFreqVal,
                MovSinGrat_tempFreqVal,
                MovSinGrat_t_beforeVal,
                MovSinGrat_t_stimVal,
                MovSinGrat_t_afterVal,
                drumgrating_syncVal,
                MovSinGrat_Motionmode,
            )
            keys = (
                event.getKeys()
            )  # retrieving key presses from the buffer during the stimulation
            keys = []  # clearing the key presses
            square1.fillColor = [-1, -1, -1]
            square2.fillColor = [-1, -1, -1]
            square1.draw()
            square2.draw()
            win.flip()

        elif (mouse.isPressedIn(calibration_button) and currMouse[0] == 1) or (
            keys and keys[0] == calibration_hotkey
        ):  # modified >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            EYE_calibration.calibration(win, calibration_syncVal)
            win.flip()

        elif (
            mouse.isPressedIn(CalibrationSynch_button) and currMouse[0] == 1
        ):  # added>>>>>>>>>>>>>>>>>>>>>>>>>
            calibration_syncVal = VS.VS("syncStatORI", 1, calibration_syncVal)
            CalibrationSync_Obj.setText("Synch:" + str(calibration_syncVal))

        elif (
            mouse.isPressedIn(CalibrationSynch_button) and currMouse[2] == 1
        ):  # added>>>>>>>>>>>>>>>>>>>>>>>>>
            calibration_syncVal = VS.VS("syncStatORI", 0, calibration_syncVal)
            CalibrationSync_Obj.setText("Synch:" + str(calibration_syncVal))

        elif mouse.isPressedIn(rf6x8_But) and currMouse[0] == 1:
            square1.fillColor = [-1, -1, -1]
            square2.fillColor = [-1, -1, -1]
            square1.draw()
            square2.draw()
            win.flip()
            Rf6x8.rf6x8(win)
            keys = (
                event.getKeys()
            )  # retrieving key presses from the buffer during the stimulation
            keys = []  # clearing the key presses
            square1.fillColor = [-1, -1, -1]
            square2.fillColor = [-1, -1, -1]
            square1.draw()
            square2.draw()
            win.flip()
        elif mouse.isPressedIn(crossline_But) and currMouse[0] == 1:
            square1.fillColor = [-1, -1, -1]
            square2.fillColor = [-1, -1, -1]
            square1.draw()
            square2.draw()
            crossline.crossline()
            win.flip()

        elif keys:
            if keys[0] == "escape":
                break

        # these functions are to draw all the buttons and textboxes
        if sum(currMouse) > 0 or keys:
            t_after_Obj.draw()
            t_stim_Obj.draw()
            t_Before_Obj.draw()
            TempFreq_Obj.draw()
            SpatFreq_Obj.draw()
            synch_ObjDRUM.draw()
            Name_Obj.draw()
            mtnmode_Obj.draw()
            t_after_ObjORI.draw()
            t_stim_ObjORI.draw()
            t_Before_ObjORI.draw()
            TempFreq_ObjORI.draw()
            SpatFreq_ObjORI.draw()
            synch_ObjORI.draw()
            Name_ObjORI.draw()
            Name_crossline.draw()
            mtnmode_ObjORI.draw()
            ledstate_Obj.draw()
            MovSinGrat_Tuning_Obj.draw()
            Calibration_Obj.draw()
            CalibrationSync_Obj.draw()  # added >>>>>>>>>>>>>>>>>>>
            vdrumGrating_But.draw()
            Name_vdrumgrating.draw()
            Name_rf6x8.draw()
            MovSinGrat_Rep_Obj.draw()
            RepBut.draw()
            RepBut.draw()
            square1.draw()
            square2.draw()
            win.flip()

    win.close()


front()
