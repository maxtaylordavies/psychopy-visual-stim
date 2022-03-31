def movSinGrat(
    MovSinGrat_SpatFreqVal,
    MovSinGrat_tempFreqVal,
    MovSinGrat_t_before,
    MovSinGrat_t_During,
    MovSinGrat_t_after,
    Synch,
    MovSinGrat_Motionmode,
    MovSinGrat_features,
    MovSinGrat_ledstate,
):  # , MovSinGrat_Rep):
    """ 
    INPUT: paramterS that are potentially changed by user in front.py by clicking buttons on the UI
    
    OUTPUT: vs stimuli for tuning, depending on the feature selected; default is 'ori' which can be changed in init_para.py;
    
    Note >> TUNING FEATURE VALUES are defined as follows:  # ori = 0, spat_freq = 1, temp_freq = 2, contrast = 3, location = 4
    
    """

    from psychopy import visual, event, clock, gui

    from datetime import datetime
    import socket
    import numpy as np
    import conv

    from init_para_OA import (
        drumgrating_addblank,
        drumgrating_Amp_sinu,
        drumgrating_controlmod,
        drumgrating_dirindex,
        drumgrating_Ori,
        drumgrating_parasize,
        drumgrating_t_triginit,
        GammaFactor,
        AmpFactor,
        drumgrating_contrast,
        drumgrating_MeanLum,
        winWidth,
        winHeight,
        ScrnNum,
        PixelSize,
        winWidthofEachDisp,
        winHeightofEachDisp,
        DisplayFrameWidth,
        DispHeight,
        FR,
        square1,
        square2,
        fontSize,
        fontClr,
        mask,
        directionalGrating_picBreak,
        directionalGrating_convergence,
        directionalGrating_rotate,
        winWidth,
        Local_IP,
        Local_Port,
        Remote_IP,
        Remote_Port,
        win,
        MovSinGrat_addblank,
        MovSinGrat_Amp_sinu,
        MovSinGrat_controlmod,
        MovSinGrat_dirindex,
        MovSinGrat_ori,
        MovSinGrat_t_triginit,
        GammaFactor,
        AmpFactor,
        MovSinGrat_contrast,
        MovSinGrat_MeanLum,
        win,
        MovSinGrat_spat_list,
        winWidth,
        winHeight,
        ScrnNum,
        PixelSize,
        winWidthofEachDisp,
        DisplayFrameWidth,
        FR,
        square1,
        square2,
        MovSinGrat_one_screen,
        mask_L,
        mask_R,
        fontSize,
        fontClr,
        win,
        Local_IP,
        Local_Port,
        Remote_IP,
        Remote_Port,
        ani_distance,
        MovSinGrat_randomseq,
        MovSinGrat_features_dict,
        MovSinGrat_angles_list,
        MovSinGrat_temp_lin_list,
        MovSinGrat_temp_osc_list,
        MovSinGrat_location_list,
        MovSinGrat_contrast_list,
    )

    # factor to scale window wit correct spatial freqency when turning it for different orientations
    fix_spatfreq = 2

    # crating mouse functionality
    mouse = event.Mouse(visible=True, win=win)

    if Synch:

        # creating the socket in which communications will take place
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # binding the local IP address and local port
        sock.bind((Local_IP, Local_Port))

        # creating textbox showing that this VS computer is waiting for UDP signal
        standBy = visual.TextBox(
            window=win,
            text=("Waiting for starting the control computer."),
            font_size=fontSize,
            font_color=fontClr,
            pos=(-2690, 475),
            size=(300, 37),
            units="pix",
            grid_horz_justification="center",
            grid_vert_justification="center",
        )

        standBy.draw()
        square1.draw()
        square2.draw()
        win.flip()

        try:
            # wait for the command 'gammacorrection'
            info = sock.recv(1024)
        except Exception:
            sock.close()
            print("Did not recieve info, connection timeout.")
            return

        # sending 'gammafloatampfloat' to the second PC
        sock.sendto(
            ("gamma" + str(GammaFactor) + "amp" + str(AmpFactor)),
            (Remote_IP, Remote_Port),
        )

        # creating textbox showing that this VS computer is waiting for UDP signal
        standBy = visual.TextBox(
            window=win,
            text=("Control Computer is Ready."),
            font_size=fontSize,
            font_color=fontClr,
            pos=(-2690, 475),
            size=(300, 37),
            units="pix",
            grid_horz_justification="center",
            grid_vert_justification="center",
        )

        standBy.draw()

        try:
            # waiting for the signal autoVs
            drumgrating_controlmod = sock.recv(1024)
        except Exception:
            sock.close()
            print("Did not recieve drumgrating_controlmod, connection timeout.")
            return

        # sending 'Wait for parameters' to the second PC
        sock.sendto("Wait for parameters", (Remote_IP, Remote_Port))

        try:
            drumgrating_parasize = sock.recv(1024)
        except Exception:
            sock.close()
            print("Did not recieve parasize, connection timeout.")
            return

        # sending a completion transcript
        sock.sendto("read parasize", (Remote_IP, Remote_Port))

        # converting the string recieved into int
        drumgrating_parasize = conv.deleteParasize(drumgrating_parasize)

        # making the array in which the parameters will be added to
        paras = np.empty(shape=[drumgrating_parasize, 9])

        # adding the parameters to the array

        # this for loop receives the 9 parameters for all the stimulations and adds them to an array
        for i in range(drumgrating_parasize):  # start from 0 to parasize[0] - 1
            temp = sock.recv(1024)
            temp = conv.convStr2Dig(temp)
            # adding the parameters to the array (temp) at position index
            paras[i, :] = temp

        sock.sendto("Para DONE", (Remote_IP, Remote_Port))

        try:
            # recieving all orientation for stimuli 1 for veritcal, 0 for horizontal
            paratemp = sock.recv(1024)
        except Exception:
            sock.close()
            print("Did not recieve message, connection timeout.")
            return

        paratemp = conv.convStr2Dig(paratemp)

        # setting up the parameters based on what was send in the paras variable
        # drumgrating_Ori = int(paratemp[0])
        Motionmode = int(paratemp[1])
        drumgrating_Amp_sinu = paratemp[2]
        drumgrating_addblank = paratemp[3]

        sock.sendto("Para DONE", (Remote_IP, Remote_Port))
    # if Synch is False, this else condition will make the parameters in the same format as if Synch was True
    else:

        # making the array in which the parameters will be added to
        paras = np.empty(shape=[drumgrating_parasize, 9])

        # adding the parameters to the array
        for i in range(drumgrating_parasize):  # start from 0 to parasize[0] - 1

            # adding the parameters as an array at index i
            paras[i, :] = [
                SpatFreqDeg,
                TempFreq,
                drumgrating_contrast,
                drumgrating_MeanLum,
                drumgrating_dirindex,
                t_before,
                t_During,
                t_after,
                drumgrating_t_triginit,
            ]

        paratemp = [
            drumgrating_Ori,
            Motionmode,
            drumgrating_Amp_sinu,
            drumgrating_addblank,
        ]

        # setting up the parameters based on what was send in the paras variable
        drumgrating_Ori = int(paratemp[0])
        Motionmode = int(paratemp[1])
        drumgrating_Amp_sinu = paratemp[2]
        drumgrating_addblank = paratemp[3]

    # creating generalized sequence of randomely shuffled stimuli for tuning, given a particular feature

    # This firt if loop will create two varialbes:
    # tuning_stim_val and tuning_stim_ind which contains all unique stimulus and corresponding index, respectively, given the tuning feature selected.
    if MovSinGrat_features == 0:  # ori

        tuning_stim_val = map(
            float, MovSinGrat_angles_list
        )  # map applies the float() function to all elements of the list, therefore converting strings to float
        tuning_stim_ind = range(len(tuning_stim_val))

    elif MovSinGrat_features == 1:  # spat_freq

        tuning_stim_val = map(float, MovSinGrat_spat_list)
        tuning_stim_ind = range(len(tuning_stim_val))

    elif MovSinGrat_features == 2:  # temp_freq

        # assign temp freq depending on Motionmode (lin vs osc motion)
        if MovSinGrat_Motionmode == 1:
            tuning_stim_val = map(
                float, MovSinGrat_temp_lin_list
            )  # SHOULD THIS BE DEPENDENT ON MOTIONMODE???
            tuning_stim_ind = range(len(tuning_stim_val))
        else:
            tuning_stim_val = map(
                float, MovSinGrat_temp_osc_list
            )  # SHOULD THIS BE DEPENDENT ON MOTIONMODE???
            tuning_stim_ind = range(len(tuning_stim_val))

    elif MovSinGrat_features == 3:  # contrast
        tuning_stim_val = (
            MovSinGrat_contrast_list  # HAS NOT BEEN CREATED IN INIT_PARA YET;
        )
        tuning_stim_ind = range(len(tuning_stim_val))

    elif MovSinGrat_features == 4:  # location

        tuning_stim_val = map(float, MovSinGrat_location_list)
        tuning_stim_ind = range(len(tuning_stim_val))

    else:
        print(
            "ERROR: MovSinGrat_features outside range. Tuning Feature Value must an integer be between 0 and 4."
        )

    # calculating total number of stimuli that will be presented (based on number of repetitions for each stimulus*ledstate combo)
    tot_num_stim = MovSinGrat_Rep * MovSinGrat_ledstate * len(tuning_stim_ind)

    # defining the variable and array shape in which the parameters will be added to; each column will represent on parameter (spat_freq, temp_freq, stimId etc.) for each presented stimulus (row)
    paras = np.empty(shape=[tot_num_stim, 12])

    # adding the parameters to the array
    # Generating sequence of order of presenting stimID that will ONLY change the TUNING FEATURE PARAMETER of the stimulus:
    for repind in xrange(MovSinGrat_Rep):

        stimId = np.empty(len(tuning_stim_ind) * MovSinGrat_ledstate)
        stimId = map(int, stimId)

        if MovSinGrat_randomseq:

            for iled in xrange(
                0, MovSinGrat_ledstate
            ):  # for each ledstate, one of each angle will be assoign in random order
                np.random.shuffle(tuning_stim_ind)

                for n in xrange(
                    iled, len(stimId), MovSinGrat_ledstate
                ):  # assign tuning_stim_ind elements to stimId by hops of size ledstate (if ledstate = 1), stimId = tuning_stim_ind;
                    stimId[n] = tuning_stim_ind[n / MovSinGrat_ledstate]  #

        else:
            for iled in xrange(0, MovSinGrat_ledstate):

                for n in xrange(iled, len(stimId), MovSinGrat_ledstate):
                    stimId[n] = tuning_stim_ind[n / MovSinGrat_ledstate]

        # adding the parameters as an array at index i
        for localstimid in xrange(0, (len(stimId))):

            if MovSinGrat_features == 0:  # 0 = ori
                paras[repind * (len(stimId)) + localstimid, :] = [
                    MovSinGrat_SpatFreqVal,
                    MovSinGrat_tempFreqVal,
                    MovSinGrat_contrast,
                    MovSinGrat_MeanLum,
                    MovSinGrat_dirindex,
                    MovSinGrat_t_before,
                    MovSinGrat_t_During,
                    MovSinGrat_t_after,
                    MovSinGrat_t_triginit,
                    tuning_stim_val[stimId[localstimid]],
                    MovSinGrat_ledstate,
                    0,
                ]  # ADD LOCATION

            elif MovSinGrat_features == 1:  # 1 = spat
                paras[repind * (len(stimId)) + localstimid, :] = [
                    tuning_stim_val[stimId[localstimid]],
                    MovSinGrat_tempFreqVal,
                    MovSinGrat_contrast,
                    MovSinGrat_MeanLum,
                    MovSinGrat_dirindex,
                    MovSinGrat_t_before,
                    MovSinGrat_t_During,
                    MovSinGrat_t_after,
                    MovSinGrat_t_triginit,
                    MovSinGrat_ori,
                    MovSinGrat_ledstate,
                    0,
                ]  # ADD LOCATION

            elif (
                MovSinGrat_features == 2
            ):  # and movSinGrat_motionMode == 0: #2 = TempFreq
                paras[repind * (len(stimId)) + localstimid, :] = [
                    MovSinGrat_SpatFreqVal,
                    tuning_stim_val[stimId[localstimid]],
                    MovSinGrat_contrast,
                    MovSinGrat_MeanLum,
                    MovSinGrat_dirindex,
                    MovSinGrat_t_before,
                    MovSinGrat_t_During,
                    MovSinGrat_t_after,
                    MovSinGrat_t_triginit,
                    MovSinGrat_ori,
                    MovSinGrat_ledstate,
                    0,
                ]  # ADD LOCATION

            elif MovSinGrat_features == 3:  # 3 = contrast
                paras[repind * (len(stimId)) + localstimid, :] = [
                    MovSinGrat_SpatFreqVal,
                    MovSinGrat_tempFreqVal,
                    tuning_stim_val[stimId[localstimid]],
                    MovSinGrat_MeanLum,
                    MovSinGrat_dirindex,
                    MovSinGrat_t_before,
                    MovSinGrat_t_During,
                    MovSinGrat_t_after,
                    MovSinGrat_t_triginit,
                    MovSinGrat_ori,
                    MovSinGrat_ledstate,
                    0,
                ]  # ADD LOCATION

    if Synch:

        while True:
            try:
                info = sock.recv(1024)
            except:
                pass
            if info.strip():  # strip spaces
                print(info)
                sock.sendto(("nex"), (Remote_IP, Remote_Port))
                break
            if mouse.getPressed()[1]:
                sock.close()
                return

        # waiting for "STR"
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

    # generating the pixel angles relaive to the mouse position based on the orientation of the stimulus
    if drumgrating_Ori == 1:
        # generating matrix that will be the place holder for every pixel

        pixelangle = np.empty(
            shape=[1, winWidth]
        )  # pixel has to be 2D since the image is 2D

        temp = np.array(range(winWidthofEachDisp))

        temp.reshape(1, winWidthofEachDisp)  # the temp must be 2D

        tempPixelAngle = (
            np.degrees(
                np.arctan(
                    (temp - (winWidthofEachDisp / 2.0))
                    * PixelSize
                    * (2.0 / DisplayFrameWidth)
                )
            )
            + 45
        )  # calculating the pixel angle for first monitor

        for i in range(ScrnNum):
            pixelangle[:, i * winWidthofEachDisp : (i + 1) * winWidthofEachDisp] = (
                tempPixelAngle + 90 * i
            )  # taking specific ranges within the full winWidth and replacing the values with the corrusponding angles

        ori = 0
        pos_1 = [0, 0]
        size = [winWidth, winHeight]

    elif drumgrating_Ori == 2:

        pixelangle = np.empty(shape=[1, winHeight])

        temp = np.array(range(winHeightofEachDisp))

        temp.reshape(1, winHeightofEachDisp)

        tempPixelAngle = (
            np.degrees(
                np.arctan(
                    (temp - (winHeightofEachDisp / 2.0))
                    * PixelSize
                    * (2.0 / DispHeight)
                )
            )
            + 45
        )  # calculating the pixel angle for first monitor

        for i in range(ScrnNum):
            pixelangle[:, i * winHeightofEachDisp : (i + 1) * winHeightofEachDisp] = (
                tempPixelAngle + 90 * i
            )  # taking specific ranges within the full winWidth and replacing the values with the corrusponding angles

        ori = 90
        pos_1 = [1 * int(winWidth / 3), 0]
        pos_2 = [-1 * int(winWidth / 3), 0]
        size = [winHeight, int(winWidth / 3)]

    else:
        return

    if drumgrating_controlmod == "maualVS":
        return

    elif drumgrating_controlmod == "autoVS":

        for m in range(drumgrating_parasize):

            if m == 0:
                SpatFreqDeg = paras[m, 0]
                TempFreq = paras[m, 1]
                drumgrating_contrast = paras[m, 2]
                drumgrating_MeanLum = paras[m, 3]
                drumgrating_dirindex = paras[m, 4]
                t_before = paras[m, 5] / 1000.0
                t_During = paras[m, 6] / 1000.0
                t_after = paras[m, 7] / 1000.0
                drumgrating_t_triginit = paras[m, 8] / 1000.0
                pixelformeanlum = (
                    2
                    * (
                        np.exp(np.log(drumgrating_MeanLum / AmpFactor) / GammaFactor)
                        / 255.0
                    )
                    - 1
                )
                drumgrating_gray = drumgrating_MeanLum
                inc = drumgrating_gray * drumgrating_contrast

                # frames to be calculated per period
                frames = round(FR / TempFreq)

                phase = np.array(range(int(frames)))

                if Motionmode == 1:
                    phase = (phase / float(round(frames))) * (2.0 * np.pi)

                elif Motionmode == 0:
                    phase = (
                        drumgrating_Amp_sinu
                        * np.sin((phase / frames) * 2 * np.pi)
                        * SpatFreqDeg
                        * 2
                        * np.pi
                    )

                # generating the pixel values for the stimulus depending on the orientation of the stimulus
                if drumgrating_Ori == 1:

                    # creating the list that will hold all frames
                    texdata1D = []

                    pixelangleTemp = pixelangle
                    # generating the pixel values for vertical stimulus
                    for i in range(int(frames)):

                        if directionalGrating_convergence == 1:

                            pixelangleTemp[
                                :, 0 : int(directionalGrating_picBreak * winWidth)
                            ] = np.exp(
                                np.log(
                                    (
                                        drumgrating_gray
                                        + inc
                                        * np.sin(
                                            pixelangle[
                                                :,
                                                0 : int(
                                                    directionalGrating_picBreak
                                                    * winWidth
                                                ),
                                            ]
                                            * SpatFreqDeg
                                            * 2
                                            * np.pi
                                            - phase[i]
                                        )
                                    )
                                    / AmpFactor
                                )
                                / GammaFactor
                            )
                            pixelangleTemp[
                                :,
                                int(directionalGrating_picBreak * winWidth) : winWidth,
                            ] = np.exp(
                                np.log(
                                    (
                                        drumgrating_gray
                                        + inc
                                        * np.sin(
                                            pixelangle[
                                                :,
                                                int(
                                                    directionalGrating_picBreak
                                                    * winWidth
                                                ) : winWidth,
                                            ]
                                            * SpatFreqDeg
                                            * 2
                                            * np.pi
                                            + phase[i]
                                        )
                                    )
                                    / AmpFactor
                                )
                                / GammaFactor
                            )

                        elif directionalGrating_convergence == 0:
                            pixelangleTemp[
                                :, 0 : int(directionalGrating_picBreak * winWidth)
                            ] = np.exp(
                                np.log(
                                    (
                                        drumgrating_gray
                                        + inc
                                        * np.sin(
                                            pixelangle[
                                                :,
                                                0 : int(
                                                    directionalGrating_picBreak
                                                    * winWidth
                                                ),
                                            ]
                                            * SpatFreqDeg
                                            * 2
                                            * np.pi
                                            + phase[i]
                                        )
                                    )
                                    / AmpFactor
                                )
                                / GammaFactor
                            )
                            pixelangleTemp[
                                :,
                                int(directionalGrating_picBreak * winWidth) : winWidth,
                            ] = np.exp(
                                np.log(
                                    (
                                        drumgrating_gray
                                        + inc
                                        * np.sin(
                                            pixelangle[
                                                :,
                                                int(
                                                    directionalGrating_picBreak
                                                    * winWidth
                                                ) : winWidth,
                                            ]
                                            * SpatFreqDeg
                                            * 2
                                            * np.pi
                                            - phase[i]
                                        )
                                    )
                                    / AmpFactor
                                )
                                / GammaFactor
                            )

                        pixVal = (
                            2 * (pixelangleTemp / 255) - 1
                        )  # converting the pixel values from 0:255 to -1:1
                        texdata1D.append(pixVal)

                        pixelangle = np.empty(shape=[1, winWidth])
                        for i in range(ScrnNum):
                            pixelangle[
                                :, i * winWidthofEachDisp : (i + 1) * winWidthofEachDisp
                            ] = (
                                tempPixelAngle + 90 * i
                            )  # taking specific ranges within the full winWidth and replacing the values with the corrusponding angles

                elif drumgrating_Ori == 2:

                    # creating the list that will hold all frames
                    texdata1D = []

                    pixelangleTemp = pixelangle
                    # generating the pixel values for vertical stimulus
                    for i in range(int(frames)):

                        if directionalGrating_rotate == 0:

                            pixelangleTemp[
                                :, 0 : int(directionalGrating_picBreak * winHeight)
                            ] = np.exp(
                                np.log(
                                    (
                                        drumgrating_gray
                                        + inc
                                        * np.sin(
                                            pixelangle[
                                                :,
                                                0 : int(
                                                    directionalGrating_picBreak
                                                    * winHeight
                                                ),
                                            ]
                                            * SpatFreqDeg
                                            * 2
                                            * np.pi
                                            + phase[i]
                                        )
                                    )
                                    / AmpFactor
                                )
                                / GammaFactor
                            )
                            pixelangleTemp[
                                :,
                                int(
                                    directionalGrating_picBreak * winHeight
                                ) : winHeight,
                            ] = np.exp(
                                np.log(
                                    (
                                        drumgrating_gray
                                        + inc
                                        * np.sin(
                                            pixelangle[
                                                :,
                                                int(
                                                    directionalGrating_picBreak
                                                    * winHeight
                                                ) : winHeight,
                                            ]
                                            * SpatFreqDeg
                                            * 2
                                            * np.pi
                                            - phase[i]
                                        )
                                    )
                                    / drumgrating_AmpFactor
                                )
                                / drumgrating_GammaFactor
                            )

                        elif directionalGrating_rotate == 1:
                            pixelangleTemp[
                                :, 0 : int(directionalGrating_picBreak * winHeight)
                            ] = np.exp(
                                np.log(
                                    (
                                        drumgrating_gray
                                        + inc
                                        * np.sin(
                                            pixelangle[
                                                :,
                                                0 : int(
                                                    directionalGrating_picBreak
                                                    * winHeight
                                                ),
                                            ]
                                            * SpatFreqDeg
                                            * 2
                                            * np.pi
                                            - phase[i]
                                        )
                                    )
                                    / AmpFactor
                                )
                                / GammaFactor
                            )
                            pixelangleTemp[
                                :,
                                int(
                                    directionalGrating_picBreak * winHeight
                                ) : winHeight,
                            ] = np.exp(
                                np.log(
                                    (
                                        drumgrating_gray
                                        + inc
                                        * np.sin(
                                            pixelangle[
                                                :,
                                                int(
                                                    directionalGrating_picBreak
                                                    * winHeight
                                                ) : winHeight,
                                            ]
                                            * SpatFreqDeg
                                            * 2
                                            * np.pi
                                            + phase[i]
                                        )
                                    )
                                    / AmpFactor
                                )
                                / GammaFactor
                            )

                        pixVal = (
                            2 * (pixelangleTemp / 255) - 1
                        )  # converting the pixel values from 0:255 to -1:1
                        texdata1D.append(pixVal)

                        pixelangle = np.empty(shape=[1, winHeight])
                        for i in range(ScrnNum):
                            pixelangle[
                                :,
                                i * winHeightofEachDisp : (i + 1) * winHeightofEachDisp,
                            ] = (
                                tempPixelAngle + 90 * i
                            )  # taking specific ranges within the full winWidth and replacing the values with the corrusponding angles

                    # creating the list that will hold all frames
                    texdata1D_2 = []

                    pixelangleTemp_2 = pixelangle
                    # generating the pixel values for vertical stimulus
                    for i in range(int(frames)):

                        if directionalGrating_rotate == 0:

                            pixelangleTemp_2[
                                :, 0 : int(directionalGrating_picBreak * winHeight)
                            ] = np.exp(
                                np.log(
                                    (
                                        drumgrating_gray
                                        + inc
                                        * np.sin(
                                            pixelangle[
                                                :,
                                                0 : int(
                                                    directionalGrating_picBreak
                                                    * winHeight
                                                ),
                                            ]
                                            * SpatFreqDeg
                                            * 2
                                            * np.pi
                                            - phase[i]
                                        )
                                    )
                                    / AmpFactor
                                )
                                / GammaFactor
                            )
                            pixelangleTemp_2[
                                :,
                                int(
                                    directionalGrating_picBreak * winHeight
                                ) : winHeight,
                            ] = np.exp(
                                np.log(
                                    (
                                        drumgrating_gray
                                        + inc
                                        * np.sin(
                                            pixelangle[
                                                :,
                                                int(
                                                    directionalGrating_picBreak
                                                    * winHeight
                                                ) : winHeight,
                                            ]
                                            * SpatFreqDeg
                                            * 2
                                            * np.pi
                                            + phase[i]
                                        )
                                    )
                                    / drumgrating_AmpFactor
                                )
                                / drumgrating_GammaFactor
                            )

                        elif directionalGrating_rotate == 1:
                            pixelangleTemp_2[
                                :, 0 : int(directionalGrating_picBreak * winHeight)
                            ] = np.exp(
                                np.log(
                                    (
                                        drumgrating_gray
                                        + inc
                                        * np.sin(
                                            pixelangle[
                                                :,
                                                0 : int(
                                                    directionalGrating_picBreak
                                                    * winHeight
                                                ),
                                            ]
                                            * SpatFreqDeg
                                            * 2
                                            * np.pi
                                            + phase[i]
                                        )
                                    )
                                    / AmpFactor
                                )
                                / GammaFactor
                            )
                            pixelangleTemp_2[
                                :,
                                int(
                                    directionalGrating_picBreak * winHeight
                                ) : winHeight,
                            ] = np.exp(
                                np.log(
                                    (
                                        drumgrating_gray
                                        + inc
                                        * np.sin(
                                            pixelangle[
                                                :,
                                                int(
                                                    directionalGrating_picBreak
                                                    * winHeight
                                                ) : winHeight,
                                            ]
                                            * SpatFreqDeg
                                            * 2
                                            * np.pi
                                            - phase[i]
                                        )
                                    )
                                    / AmpFactor
                                )
                                / GammaFactor
                            )

                        pixVal = (
                            2 * (pixelangleTemp_2 / 255) - 1
                        )  # converting the pixel values from 0:255 to -1:1
                        texdata1D_2.append(pixVal)

                        pixelangle = np.empty(shape=[1, winHeight])
                        for i in range(ScrnNum):
                            pixelangle[
                                :,
                                i * winHeightofEachDisp : (i + 1) * winHeightofEachDisp,
                            ] = (
                                tempPixelAngle + 90 * i
                            )  # taking specific ranges within the full winWidth and replacing the values with the corrusponding angles

                else:
                    return

            else:
                if sum(abs(paras[m, :] - paras[m - 1, :])) > 1e-7:
                    # if (not all([v == 0  for v in abs(paras[m, :] - paras[m-1, :])])):

                    SpatFreqDeg = paras[m, 0]
                    TempFreq = paras[m, 1]
                    drumgrating_contrast = paras[m, 2]
                    drumgrating_MeanLum = paras[m, 3]
                    drumgrating_dirindex = paras[m, 4]
                    t_before = paras[m, 5] / 1000.0
                    t_During = paras[m, 6] / 1000.0
                    t_afterVal = paras[m, 7] / 1000.0
                    drumgrating_t_triginit = paras[m, 8] / 1000.0
                    pixelformeanlum = (
                        2
                        * (
                            np.exp(
                                np.log(drumgrating_MeanLum / AmpFactor) / GammaFactor
                            )
                            / 255.0
                        )
                        - 1
                    )
                    drumgrating_gray = drumgrating_MeanLum
                    inc = drumgrating_gray * drumgrating_contrast

                    # frames to be calculated per period
                    frames = round(FR / TempFreq)

                phase = np.array(range(int(frames)))

                if Motionmode == 1:
                    phase = (phase / float(round(frames))) * (2.0 * np.pi)

                elif Motionmode == 0:
                    phase = (
                        drumgrating_Amp_sinu
                        * np.sin((phase / frames) * 2 * np.pi)
                        * SpatFreqDeg
                        * 2
                        * np.pi
                    )

                # generating the pixel values for the stimulus depending on the orientation of the stimulus
                if drumgrating_Ori == 1:

                    # creating the list that will hold all frames
                    texdata1D = []

                    pixelangleTemp = pixelangle
                    # generating the pixel values for vertical stimulus
                    for i in range(int(frames)):
                        print("i")
                        if directionalGrating_convergence == 1:

                            pixelangleTemp[
                                :, 0 : int(directionalGrating_picBreak * winWidth)
                            ] = np.exp(
                                np.log(
                                    (
                                        drumgrating_gray
                                        + inc
                                        * np.sin(
                                            pixelangle[
                                                :,
                                                0 : int(
                                                    directionalGrating_picBreak
                                                    * winWidth
                                                ),
                                            ]
                                            * SpatFreqDeg
                                            * 2
                                            * np.pi
                                            - phase[i]
                                        )
                                    )
                                    / AmpFactor
                                )
                                / GammaFactor
                            )
                            pixelangleTemp[
                                :,
                                int(directionalGrating_picBreak * winWidth) : winWidth,
                            ] = np.exp(
                                np.log(
                                    (
                                        drumgrating_gray
                                        + inc
                                        * np.sin(
                                            pixelangle[
                                                :,
                                                int(
                                                    directionalGrating_picBreak
                                                    * winWidth
                                                ) : winWidth,
                                            ]
                                            * SpatFreqDeg
                                            * 2
                                            * np.pi
                                            + phase[i]
                                        )
                                    )
                                    / AmpFactor
                                )
                                / GammaFactor
                            )

                        elif directionalGrating_convergence == 0:
                            pixelangleTemp[
                                :, 0 : int(directionalGrating_picBreak * winWidth)
                            ] = np.exp(
                                np.log(
                                    (
                                        drumgrating_gray
                                        + inc
                                        * np.sin(
                                            pixelangle[
                                                :,
                                                0 : int(
                                                    directionalGrating_picBreak
                                                    * winWidth
                                                ),
                                            ]
                                            * SpatFreqDeg
                                            * 2
                                            * np.pi
                                            + phase[i]
                                        )
                                    )
                                    / AmpFactor
                                )
                                / GammaFactor
                            )
                            pixelangleTemp[
                                :,
                                int(directionalGrating_picBreak * winWidth) : winWidth,
                            ] = np.exp(
                                np.log(
                                    (
                                        drumgrating_gray
                                        + inc
                                        * np.sin(
                                            pixelangle[
                                                :,
                                                int(
                                                    directionalGrating_picBreak
                                                    * winWidth
                                                ) : winWidth,
                                            ]
                                            * SpatFreqDeg
                                            * 2
                                            * np.pi
                                            + phase[i]
                                        )
                                    )
                                    / dAmpFactor
                                )
                                / GammaFactor
                            )

                        pixVal = (
                            2 * (pixelangleTemp / 255) - 1
                        )  # converting the pixel values from 0:255 to -1:1
                        texdata1D.append(pixVal)

                        pixelangle = np.empty(shape=[1, winWidth])
                        for i in range(ScrnNum):
                            pixelangle[
                                :, i * winWidthofEachDisp : (i + 1) * winWidthofEachDisp
                            ] = (
                                tempPixelAngle + 90 * i
                            )  # taking specific ranges within the full winWidth and replacing the values with the corrusponding angles

                elif drumgrating_Ori == 2:

                    # creating the list that will hold all frames
                    texdata1D = []

                    pixelangleTemp = pixelangle
                    # generating the pixel values for vertical stimulus
                    for i in range(int(frames)):

                        if directionalGrating_rotate == 0:

                            pixelangleTemp[
                                :, 0 : int(directionalGrating_picBreak * winHeight)
                            ] = np.exp(
                                np.log(
                                    (
                                        drumgrating_gray
                                        + inc
                                        * np.sin(
                                            pixelangle[
                                                :,
                                                0 : int(
                                                    directionalGrating_picBreak
                                                    * winHeight
                                                ),
                                            ]
                                            * SpatFreqDeg
                                            * 2
                                            * np.pi
                                            - phase[i]
                                        )
                                    )
                                    / AmpFactor
                                )
                                / GammaFactor
                            )
                            pixelangleTemp[
                                :,
                                int(
                                    directionalGrating_picBreak * winHeight
                                ) : winHeight,
                            ] = np.exp(
                                np.log(
                                    (
                                        drumgrating_gray
                                        + inc
                                        * np.sin(
                                            pixelangle[
                                                :,
                                                int(
                                                    directionalGrating_picBreak
                                                    * winHeight
                                                ) : winHeight,
                                            ]
                                            * SpatFreqDeg
                                            * 2
                                            * np.pi
                                            - phase[i]
                                        )
                                    )
                                    / AmpFactor
                                )
                                / GammaFactor
                            )

                        elif directionalGrating_rotate == 1:
                            pixelangleTemp[
                                :, 0 : int(directionalGrating_picBreak * winHeight)
                            ] = np.exp(
                                np.log(
                                    (
                                        drumgrating_gray
                                        + inc
                                        * np.sin(
                                            pixelangle[
                                                :,
                                                0 : int(
                                                    directionalGrating_picBreak
                                                    * winHeight
                                                ),
                                            ]
                                            * SpatFreqDeg
                                            * 2
                                            * np.pi
                                            - phase[i]
                                        )
                                    )
                                    / AmpFactor
                                )
                                / GammaFactor
                            )
                            pixelangleTemp[
                                :,
                                int(
                                    directionalGrating_picBreak * winHeight
                                ) : winHeight,
                            ] = np.exp(
                                np.log(
                                    (
                                        drumgrating_gray
                                        + inc
                                        * np.sin(
                                            pixelangle[
                                                :,
                                                int(
                                                    directionalGrating_picBreak
                                                    * winHeight
                                                ) : winHeight,
                                            ]
                                            * SpatFreqDeg
                                            * 2
                                            * np.pi
                                            + phase[i]
                                        )
                                    )
                                    / AmpFactor
                                )
                                / GammaFactor
                            )

                        pixVal = (
                            2 * (pixelangleTemp / 255) - 1
                        )  # converting the pixel values from 0:255 to -1:1
                        texdata1D.append(pixVal)

                        pixelangle = np.empty(shape=[1, winHeight])
                        for i in range(ScrnNum):
                            pixelangle[
                                :,
                                i * winHeightofEachDisp : (i + 1) * winHeightofEachDisp,
                            ] = (
                                tempPixelAngle + 90 * i
                            )  # taking specific ranges within the full winWidth and replacing the values with the corrusponding angles

                    # creating the list that will hold all frames
                    texdata1D_2 = []

                    pixelangleTemp_2 = pixelangle
                    # generating the pixel values for vertical stimulus
                    for i in range(int(frames)):

                        if directionalGrating_rotate == 0:

                            pixelangleTemp_2[
                                :, 0 : int(directionalGrating_picBreak * winHeight)
                            ] = np.exp(
                                np.log(
                                    (
                                        drumgrating_gray
                                        + inc
                                        * np.sin(
                                            pixelangle[
                                                :,
                                                0 : int(
                                                    directionalGrating_picBreak
                                                    * winHeight
                                                ),
                                            ]
                                            * SpatFreqDeg
                                            * 2
                                            * np.pi
                                            - phase[i]
                                        )
                                    )
                                    / AmpFactor
                                )
                                / GammaFactor
                            )
                            pixelangleTemp_2[
                                :,
                                int(
                                    directionalGrating_picBreak * winHeight
                                ) : winHeight,
                            ] = np.exp(
                                np.log(
                                    (
                                        drumgrating_gray
                                        + inc
                                        * np.sin(
                                            pixelangle[
                                                :,
                                                int(
                                                    directionalGrating_picBreak
                                                    * winHeight
                                                ) : winHeight,
                                            ]
                                            * SpatFreqDeg
                                            * 2
                                            * np.pi
                                            + phase[i]
                                        )
                                    )
                                    / AmpFactor
                                )
                                / GammaFactor
                            )

                        elif directionalGrating_rotate == 1:
                            pixelangleTemp_2[
                                :, 0 : int(directionalGrating_picBreak * winHeight)
                            ] = np.exp(
                                np.log(
                                    (
                                        drumgrating_gray
                                        + inc
                                        * np.sin(
                                            pixelangle[
                                                :,
                                                0 : int(
                                                    directionalGrating_picBreak
                                                    * winHeight
                                                ),
                                            ]
                                            * SpatFreqDeg
                                            * 2
                                            * np.pi
                                            + phase[i]
                                        )
                                    )
                                    / AmpFactor
                                )
                                / GammaFactor
                            )
                            pixelangleTemp_2[
                                :,
                                int(
                                    directionalGrating_picBreak * winHeight
                                ) : winHeight,
                            ] = np.exp(
                                np.log(
                                    (
                                        drumgrating_gray
                                        + inc
                                        * np.sin(
                                            pixelangle[
                                                :,
                                                int(
                                                    directionalGrating_picBreak
                                                    * winHeight
                                                ) : winHeight,
                                            ]
                                            * SpatFreqDeg
                                            * 2
                                            * np.pi
                                            - phase[i]
                                        )
                                    )
                                    / AmpFactor
                                )
                                / GammaFactor
                            )

                        pixVal = (
                            2 * (pixelangleTemp_2 / 255) - 1
                        )  # converting the pixel values from 0:255 to -1:1
                        texdata1D_2.append(pixVal)

                        pixelangle = np.empty(shape=[1, winHeight])
                        for i in range(ScrnNum):
                            pixelangle[
                                :,
                                i * winHeightofEachDisp : (i + 1) * winHeightofEachDisp,
                            ] = (
                                tempPixelAngle + 90 * i
                            )  # taking specific ranges within the full winWidth and replacing the values with the corrusponding angles

                else:
                    return
            print(mask)
            print(np.shape(mask))
            # setting up the grating
            DrawTexture = visual.GratingStim(
                win=win,
                size=size,
                units="pix",
                tex=texdata1D[0],
                mask=mask,
                ori=ori,
                pos=pos_1,
            )

            if drumgrating_Ori == 2:
                # setting up the grating
                DrawTexture_2 = visual.GratingStim(
                    win=win,
                    size=size,
                    units="pix",
                    tex=texdata1D[0],
                    mask=mask,
                    ori=ori,
                    pos=pos_2,
                )

            if Synch:

                # waiting for "TRLstart", if TRLstart is sent this loop will send "TRLstart m" then break
                sock.settimeout(0.5)
                comm = [""]
                while True:
                    try:
                        comm = sock.recvfrom(1024)
                    except Exception:
                        pass

                    if comm[0] == "TRLstart":
                        sock.sendto(
                            ("TRLstart " + str(m + 1)), (Remote_IP, Remote_Port)
                        )
                        break

                    elif (
                        comm[0] == "ESC1"
                    ):  # if 'ESC1' is in the buffer, return to front
                        sock.close()
                        return

                    if mouse.getPressed()[1]:
                        sock.close()
                        print("Exit at ESC1")
                        return

            # time before the stimulation
            for toc in range(int(t_before * FR)):

                if drumgrating_addblank == 1.0:
                    win.color = pixelformeanlum
                    square1.draw()
                    square2.draw()

                elif drumgrating_addblank == 0.0:
                    DrawTexture.draw()
                    if drumgrating_Ori == 2:
                        DrawTexture_2.draw()
                    square1.draw()
                    square2.draw()
                win.flip()

            # t_triger initial timing for triggerin the camera
            for i in range(int(FR * drumgrating_t_triginit)):
                if i < 3:
                    square1.fillColor = [1, 1, 1]
                    square2.fillColor = [-1, -1, -1]

                else:
                    square1.fillColor = [-1, -1, -1]
                    square2.fillColor = [-1, -1, -1]

                if drumgrating_addblank == 1.0:
                    win.color = pixelformeanlum
                    square1.draw()
                    square2.draw()

                elif drumgrating_addblank == 0.0:
                    DrawTexture.draw()
                    if drumgrating_Ori == 2:
                        DrawTexture_2.draw()

                if mouse.getPressed()[1]:
                    if Synch:
                        sock.close()
                    return

                square1.draw()
                square2.draw()
                win.flip()

            # making the top square white
            square1.fillColor = [-1, -1, -1]
            square2.fillColor = [1, 1, 1]

            # this variable controls the looping and frame that is to be displayed
            m = 0

            # drawing the frames on the window
            for frm in range(int(FR * t_During)):

                # assigning the texture using the corrusponding frame
                DrawTexture.tex = texdata1D[m]
                if drumgrating_Ori == 2:
                    DrawTexture_2.tex = texdata1D_2[m]

                # this if statement is for existing the stimulation
                if mouse.getPressed()[1]:

                    if Synch:
                        sock.close()
                    return

                m = m + 1

                if m >= len(texdata1D):
                    m = 0

                DrawTexture.draw()
                if drumgrating_Ori == 2:
                    DrawTexture_2.draw()
                square1.draw()
                square2.draw()
                win.flip()

            # changing the characteristics of the two squares at the bottom left corner
            square1.fillColor = [-1, -1, -1]
            square2.fillColor = [-1, -1, -1]

            # time after the stimulation
            for toc in range(int(t_after * FR)):

                if drumgrating_addblank == 1.0:
                    win.color = pixelformeanlum
                    square1.draw()
                    square2.draw()

                elif drumgrating_addblank == 0.0:
                    DrawTexture.draw()
                    if drumgrating_Ori == 2:
                        DrawTexture_2.draw()
                    square1.draw()
                    square2.draw()

                win.flip()

            if Synch:

                sock.sendto(("TRLdone " + str(m + 1)), (Remote_IP, Remote_Port))

                # checking for stop button
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
                        print("Exit at ESC2")
                        print("Line 388 UDP:" + str(comm))
                        return

