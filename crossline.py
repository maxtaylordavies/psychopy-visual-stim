import numpy as np
from psychopy import core, visual, event
import VS
import drumgrating
import movSinGrat_tuning
import EYE_calibration
import socket
from init_para import *
import TestNov
import Rf6x8


def crossline():
    # CREATING TEXTBOXES

    # DRUMGRATING

    Linehorz = psychopy.visual.Line(win, start=(-1, 0), end=(1, 0))
    Linevert1 = psychopy.visual.Line(
        win, start=(0, 1), end=(0, -1)
    )  # vertical line on middle monitor
    Linevert2 = psychopy.visual.Line(
        win, start=(-4 / 6.0, 1), end=(-4 / 6.0, -1)
    )  # vertical line on left monitor
    Linevert3 = psychopy.visual.Line(
        win, start=(4 / 6.0, 1), end=(4 / 6.0, -1)
    )  # vertical line on right monitor
    # drawing the textboxes
    Linehorz.draw()
    Linevert1.draw()
    Linevert2.draw()
    Linevert3.draw()

    win.flip()

    mouse = event.Mouse(visible=True, win=win)

    keep_going = True

    while keep_going:
        psychopy.core.wait(0.1)
        currMouse = mouse.getPressed()

        keys = (
            event.getKeys()
        )  # this will retrieve key presses from the buffer and place them into a list (in the order that they were pressed)

        if keys:
            if keys[0] == "escape":
                break

        # these functions are to draw all the buttons and textboxes
        if sum(currMouse) > 0:
            Linehorz.draw()
            Linevert1.draw()
            Linevert2.draw()
            Linevert3.draw()
            win.flip()

    win.close()


# front()

