def rf6x8(win):

    from psychopy import visual, event, clock, gui

    from datetime import datetime

    from init_para import (
        MovSinGrat_addblank,
        MovSinGrat_Amp_sinu,
        MovSinGrat_controlmod,
        MovSinGrat_dirindex,
        MovSinGrat_ori,
        MovSinGrat_contrast,
        MovSinGrat_MeanLum,
        mask_L,
        mask_R,
        winWidth,
        winHeight,
        ScrnNum,
        PixelSize,
        winWidthofEachDisp,
        DisplayFrameWidth,
        FR,
        square1,
        square2,
        fontSize,
        fontClr,
        win,
        ani_distance,
    )

    import socket
    import numpy as np
    import conv
    import os, sys, time

    # PARAMETERS
    num_row = 6
    num_col = 8
    display_ind = 2  # central screen

    one_screen = 1

    # stim time parameters
    t_before = 0
    t_during = 200
    t_after = 200
    t_triginit = 100

    # contrast (stim colour) parameters
    contrast = 1
    meanLum = 35
    minLum = meanLum - meanLum * contrast
    maxLum = meanLum + meanLum * contrast
    gammaFactor = 2.251
    ampFactor = 0.0007181

    winClr = (
        2 * (np.exp(np.log(meanLum / ampFactor) / gammaFactor) / 255.0) - 1
    )  # colour of background (in pix val)
    white = (
        2 * (np.exp(np.log(maxLum / ampFactor) / gammaFactor) / 255.0) - 1
    )  # convert maxLum into pix value
    black = -1
    win.colour = winClr

    # stim order parameters
    repetition = 25
    num_dif_stim = (
        48 * 2
    )  # number of location the stimulus (6 x 8 = 48) will be displayed in two colours values with 100% contrast => 48*2 = 96
    tot_num_stim = (
        repetition * num_dif_stim
    )  # total number of stiumuli that will be displayed in one experiment

    index = range(
        num_dif_stim
    )  # number 0-95 representing each location in 6 x 8 screen and black or white colour
    x_pos = (
        [0] * 6 + [1] * 6 + [2] * 6 + [3] * 6 + [4] * 6 + [5] * 6 + [6] * 6 + [7] * 6
    ) * 2  # list of all possible x-coordinate for stim
    y_pos = range(6) * 8 * 2  # list of all possible y-coordinate for stim
    Lum_list = [white] * 48 + [black] * 48

    # reshape data into numpy array
    x_pos = np.asarray(x_pos)
    y_pos = np.asarray(y_pos)
    Lum_list = np.asarray(Lum_list)

    # creating a matrix to store all stim ID (index), position and colour information
    stim_order = np.ones((96, 12), dtype=float)

    stim_order[:, 0] = x_pos
    stim_order[:, 1] = y_pos
    stim_order[:, 2] = contrast
    stim_order[:, 3] = meanLum
    stim_order[:, 4] = Lum_list
    stim_order[:, 5] = t_before
    stim_order[:, 6] = t_during
    stim_order[:, 7] = t_after
    stim_order[:, 8] = t_triginit
    stim_order[:, 9] = index
    stim_order[:, 10] = 0
    stim_order[:, 11] = 0

    # create ramdom order for stimuli presentation
    np.random.shuffle(
        index
    )  # this function automatically shuffles the input (no need to assign a new var)

    # stim shape parameters
    top_left = [-1.0 / ScrnNum, 1.0]
    top_right = [top_left[0] + 2.0 / ScrnNum / num_col, top_left[1]]
    bottom_left = [top_left[0], top_left[1] - 2.0 / num_row]
    bottom_right = [top_right[0], bottom_left[1]]

    # top_left = [0,0]
    # top_right = [2.0/ScrnNum/num_col, 0]
    # bottom_left = [0, -2.0/num_row]
    # bottom_right = [top_right[0], bottom_left[1]]

    stim_per_rep = 96
    stim_vertices = np.array(([top_left, top_right, bottom_right, bottom_left]))
    stim_vertices.reshape(4, 2)  # reshape to fit psychopy texture requirements

    # creating visual stimulation display functionality

    # creating mouse functionality
    mouse = event.Mouse(visible=True, win=win)

    # Naming the experiment to create fileName (at the end of this function)
    #    instruction_text = visual.TextStim(win, text = u'Name experiment and press enter to start.', pos=(0, 0.5))
    #    answer_text = visual.TextStim(win)
    #
    #    #show instructions
    #    win.color = winClr
    #    instruction_text.draw()
    square1.draw()  # have to draw trigger squ; otherwise transient white will happen$$$$$$$$$$$$$$$
    square2.draw()
    win.flip()

    # get users input for experiment name
    #    now = True
    #    answer_text.text = ''
    #    while now:
    #        key = event.waitKeys()[0]
    #        # Add a new number
    #        if key in '1234567890abcdfeghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-':
    #            answer_text.text += key
    #
    #        # Delete last character, if there are any chars at all
    #        elif key == 'backspace' and len(answer_text.text) > 0:
    #            answer_text.text = answer_text.text[:-1]
    #
    #        # Stop collecting response and return it
    #        elif key == 'return':
    #            expName = answer_text.text
    #            print ('expName IN here: ', expName)
    #            now = False
    #
    #        # Show current answer state
    #        instruction_text.draw()
    #        answer_text.draw()
    #        square1.draw()  #have to draw trigger squ; otherwise transient white will happen$$$$$$$$$$$$$
    #        square2.draw()
    #        win.flip()
    #
    #        pass #
    #
    #    #setting name of file which will be used to save order of vs stim displayed;
    #    date = datetime.today().strftime('%y%m%d%H') #extract today's date
    #    path = 'Y:/Grade Students/lavoiea2/vs_stim_data/'
    #    fileName = path + expName + '_' + date

    # setting name of file which will be used to save order of vs stim displayed; NAME = MVS (movSinGrat) + type of tuning feature manipulated in experiment + datetime

    eph_pathlist = []
    eph_timelist = []
    eph_dirflaglist = []
    eph_explist = []

    vs_pathlist = []
    vs_timelist = []
    vs_dirflaglist = []

    vs_path = "Y:/Grade Students/lavoiea2/vs paramater/"
    eph_path = "Y:/Grade Students/lavoiea2/ephys_data/"

    # all entries in the directory w/ stats

    for fn in os.listdir(eph_path):
        eph_explist.append(fn)
        temppath = os.path.join(eph_path, fn)
        eph_pathlist.append(temppath)
        eph_timelist.append(os.path.getmtime(temppath))  # find time for each file
        if os.path.isdir(temppath):  # check if directory (do not want any file)
            eph_dirflaglist.append(1)
        else:
            eph_dirflaglist.append(0)

    for fn in os.listdir(vs_path):
        temppath = os.path.join(vs_path, fn)
        vs_pathlist.append(temppath)
        vs_timelist.append(os.path.getmtime(temppath))  # find time for each file
        if os.path.isdir(temppath):  # check if directory (do not want any file)
            vs_dirflaglist.append(1)
        else:
            vs_dirflaglist.append(0)

    latesttime = 0
    latesttimeindex = 0
    if sum(eph_dirflaglist) - sum(vs_dirflaglist) == 1:
        for i in range(len(eph_pathlist)):
            if eph_dirflaglist[i] == 1 and eph_timelist[i] > latesttime:
                latesttime = eph_timelist[i]
                latesttimeindex = i
    else:
        print("ERROR: Ephys folder size does not match vs folder size")
        return

    if not os.path.exists(vs_path + eph_explist[latesttimeindex]):
        os.makedirs(vs_path + eph_explist[latesttimeindex])  # create folder in vs_path
    else:
        print("ERROR: folder already exist in vs_path")
        return

    # date = datetime.today().strftime('%y%m%d') #extract today's date
    fileName = (
        vs_path + eph_explist[latesttimeindex] + "/vsparam"
    )  # exp name defined above either by user (if not synch) or by eye tracking software (if user)

    exit_flag = (
        0  # to make sure finish the current visual stimulation before exiting program;
    )

    # loop over each stim and display it
    for n in range(
        tot_num_stim
    ):  # will loop around for total Repetitions (96*repetition)

        if exit_flag:
            break

        tic = clock.getTime()

        stim_ind = n % len(
            index
        )  # give a number between 0 and 95 which represents each stimuli, allowing to continuouly loop around for total repetitions

        # assign postion of stimulus
        i, j = stim_order[index[stim_ind]][0], stim_order[index[stim_ind]][1]
        # assing colour of stimulus
        colour = stim_order[index[stim_ind]][4]

        # Create stimulus with changing : a single rect with x = screenwdth/8 and y = screenheight/6
        stim = visual.ShapeStim(
            win=win,
            units="norm",
            pos=(
                i * (2.0 / ScrnNum / num_col),
                j * (-2.0 / num_row),
            ),  # moves the stim by 1/9th to the right and 1/4th down (relative to screen size); if (i,j) = (0,0); display middle screen @ top left corner
            fillColor=colour,
            vertices=stim_vertices,
            lineWidth=0,
        )

        # Display stimulation using a series of while loops
        win.color = winClr

        # R and L screen to display stim on front screen only
        if one_screen:
            mask_L.draw()
            mask_R.draw()

        square1.draw()
        square2.draw()
        win.flip()

        # time before the stimulation
        toc = clock.getTime() - tic

        while toc < (t_before / 1000.0):

            toc = clock.getTime() - tic

            # this if statement is for existing the stimulation
            if mouse.getPressed()[1]:
                exit_flag = 1

            # R and L screen to display stim on front screen only
            if one_screen:
                mask_L.draw()
                mask_R.draw()

            # display trigger squares
            square1.draw()
            square2.draw()
            win.flip()

        # t_triger initial timing for triggerin the camera
        for i in range(int(FR * t_triginit / 1000.0)):

            if mouse.getPressed()[1]:
                exit_flag = 1

            if i < 3:
                square1.fillColor = [1, 1, 1]
                square2.fillColor = [-1, -1, -1]

            else:
                square1.fillColor = [-1, -1, -1]
                square2.fillColor = [-1, -1, -1]

            # R and L screen to display stim on front screen only
            if one_screen:
                mask_L.draw()
                mask_R.draw()

            # win.color = winClr
            square1.draw()
            square2.draw()
            win.flip()

        # making the top square white
        square1.fillColor = [-1, -1, -1]
        square2.fillColor = [1, 1, 1]

        # drawing the stimulus on the window
        for frm in range(int(FR * t_during / 1000.0)):

            if mouse.getPressed()[1]:
                exit_flag = 1

            stim.draw()

            # R and L screen to display stim on front screen only
            if one_screen:
                mask_L.draw()
                mask_R.draw()

            square1.draw()
            square2.draw()
            win.flip()

        # changing the characteristics of the two squares at the bottom left corner
        square1.fillColor = [-1, -1, -1]
        square2.fillColor = [-1, -1, -1]

        # time after the stimulation
        for toc in range(int(t_after * FR / 1000.0)):

            if mouse.getPressed()[1]:
                exit_flag = 1

            # win.color = winClr

            # R and L screen to display stim on front screen only
            if one_screen:
                mask_L.draw()
                mask_R.draw()

            square1.draw()
            square2.draw()
            win.flip()

        # save vs data in .csv format
        # create a temp list variable that stores array values that will be appended
        save_row = stim_order[index[stim_ind]].tolist()

        # open and append values to new file
        with open(fileName + ".csv", "a") as f:

            for i in range(len(save_row)):

                f.write(str(save_row[i]) + ",")

            f.write("\n")

