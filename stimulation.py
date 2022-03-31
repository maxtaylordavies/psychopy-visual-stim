def stimulation(SpatFreqDeg, TempFreq, t_before, t_During, t_after, Synch, Motionmode):

    from psychopy import visual
    from psychopy import event

    from init_para import (
        drumgrating_addblank,
        drumgrating_Amp_sinu,
        drumgrating_controlmod,
        drumgrating_dirindex,
        drumgrating_Ori,
        drumgrating_parasize,
        drumgrating_t_triginit,
        drumgrating_GammaFactor,
        drumgrating_AmpFactor,
        drumgrating_contrast,
        drumgrating_MeanLum,
        drumgrating_gray,
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
    )

    import socket
    import numpy as np
    import conv

    print(ScrnNum)
    # crating mouse functionality
    mouse = event.Mouse(visible=True, win=win)
    if Synch:

        # creating the socket in which communications will take place
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # binding the local IP address and local port
        sock.bind((Local_IP, Local_Port))

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
            (
                "gamma"
                + str(drumgrating_GammaFactor)
                + "amp"
                + str(drumgrating_AmpFactor)
            ),
            (Remote_IP, Remote_Port),
        )

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
        drumgrating_Ori = int(paratemp[0])
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

    if Synch:

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
        pixelangle = np.empty(shape=[1, winWidth])

        # generating the corrusponding angle of every pixel
        for i in range(winWidthofEachDisp):
            angle = (
                np.degrees(
                    np.arctan(
                        (i - (winWidthofEachDisp / 2.0))
                        * PixelSize
                        * (2.0 / DisplayFrameWidth)
                    )
                )
                + 45
            )  # finding the pixle angle of each pixle in degrees (left monitor)

            if ScrnNum >= 1:
                pixelangle[:, i] = angle

                if ScrnNum >= 2:
                    pixelangle[:, i + winWidthofEachDisp] = angle + 90

                    if ScrnNum >= 3:
                        pixelangle[:, i + 2 * winWidthofEachDisp] = angle + 180

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
                        np.exp(
                            np.log(drumgrating_MeanLum / drumgrating_AmpFactor)
                            / drumgrating_GammaFactor
                        )
                        / 255.0
                    )
                    - 1
                )
                drumgrating_gray = drumgrating_MeanLum
                inc = drumgrating_gray * drumgrating_contrast

                # frames to be calculated per period
                frames = round(FR / TempFreq)

                if Motionmode == 1:
                    phase = []
                    for i in range(int(frames)):
                        x = (i / frames) * (2.0 * np.pi)
                        phase.append(x)

                elif Motionmode == 0:
                    phase = []
                    for i in range(int(frames)):
                        x = (
                            drumgrating_Amp_sinu
                            * np.sin((i / frames) * 2 * np.pi)
                            * SpatFreqDeg
                            * 2
                            * np.pi
                        )
                        phase.append(x)

                # generating the pixel values for the stimulus depending on the orientation of the stimulus
                if drumgrating_Ori == 1:

                    # creating the list that will hold all frames
                    textdata1D = []

                    # generating the pixel values for vertical stimulus
                    for i in range(int(frames)):
                        textdata1DTmp = np.exp(
                            np.log(
                                (
                                    drumgrating_gray
                                    + inc
                                    * np.sin(
                                        pixelangle * SpatFreqDeg * 2 * np.pi + phase[i]
                                    )
                                )
                                / drumgrating_AmpFactor
                            )
                            / drumgrating_GammaFactor
                        )
                        pixVal = (
                            2 * (textdata1DTmp / 255) - 1
                        )  # converting the pixel values from 0:255 to -1:1
                        textdata1D.append(pixVal)

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
                                np.log(drumgrating_MeanLum / drumgrating_AmpFactor)
                                / drumgrating_GammaFactor
                            )
                            / 255.0
                        )
                        - 1
                    )
                    drumgrating_gray = drumgrating_MeanLum
                    inc = drumgrating_gray * drumgrating_contrast

                    # frames to be calculated per period
                    frames = int(np.ceil(FR / TempFreq))

                if Motionmode == 1:
                    phase = []
                    for i in range(int(frames)):
                        x = (i / frames) * (2.0 * np.pi)
                        phase.append(x)

                elif Motionmode == 0:
                    phase = []
                    for i in range(int(frames)):
                        x = (
                            drumgrating_Amp_sinu
                            * np.sin((i / frames) * 2 * np.pi)
                            * SpatFreqDeg
                            * 2
                            * np.pi
                        )
                        phase.append(x)

                # generating the pixel values for the stimulus depending on the orientation of the stimulus
                if drumgrating_Ori == 1:

                    # creating the list that will hold all frames
                    textdata1D = []

                    # generating the pixel values for vertical stimulus
                    for i in range(int(frames)):
                        textdata1DTmp = np.exp(
                            np.log(
                                (
                                    drumgrating_gray
                                    + inc
                                    * np.sin(
                                        pixelangle * SpatFreqDeg * 2 * np.pi + phase[i]
                                    )
                                )
                                / drumgrating_AmpFactor
                            )
                            / drumgrating_GammaFactor
                        )
                        pixVal = (
                            2 * (textdata1DTmp / 255) - 1
                        )  # converting the pixel values from 0:255 to -1:1
                        textdata1D.append(pixVal)

                else:
                    return

            # setting up the grating
            DrawTexture = visual.GratingStim(
                win=win, size=[winWidth, winHeight], units="pix", tex=pixVal
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
                        print("Line 275 UDP:" + str(comm))
                        return

            # time before the stimulation
            for toc in range(int(t_before * FR)):

                if drumgrating_addblank == 1.0:
                    win.color = pixelformeanlum
                    square1.draw()
                    square2.draw()

                elif drumgrating_addblank == 0.0:
                    DrawTexture.draw()
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
                DrawTexture.tex = textdata1D[m]

                # this if statement is for existing the stimulation
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

