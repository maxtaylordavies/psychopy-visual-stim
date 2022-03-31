import numpy as np
import psychopy.core
import VS
import stimulation
import socket
from psychopy import visual
from psychopy import event



win=visual.Window(
    size = [500, 500], 
    color = 0
    )

#TRY TO MAKE TEXTBOX CLASS AND THEN BUTTON class


def textbox(gray):
    temp = visual.textbox(
        window=win,
        text=(str(gray)),
        font_size=15,
        font_color=[0.5, 0.5, 0.5],
        border_color=[0.5, 0.5, 0.5],
        pos=(1, 1),
        size=(232,37),
        units='pix',
        grid_horz_justification='center',
        grid_vert_justification='center'
        )
    return temp


test = textbox(10)
print 10

test.draw()

win.flip()
print 'win flip'

event.waitKeys()

win.close()
