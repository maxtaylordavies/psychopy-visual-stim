import random
from psychopy import visual, event, core

# Tidy 2: create a window once. Don't close it.
win = visual.Window(
    size=[500, 500],
    units="pix",
    fullscr=False
)

instruction_text = visual.TextStim(win, text = u'Name experiment:', pos=(0, 100))
answer_text = visual.TextStim(win)

instruction_text.draw()
win.flip()

# Solution: a function to collect written responses
#def get_typed_answer():
now = True
answer_text.text = ''
while now:
    key = event.waitKeys()[0]
    # Add a new number
    if key in '1234567890abcdfeghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-':
        answer_text.text += key

    # Delete last character, if there are any chars at all
    elif key == 'backspace' and len(answer_text.text) > 0:
        answer_text.text = answer_text.text[:-1]

    # Stop collecting response and return it
    elif key == 'return':
        fileName = answer_text.text
        now = False

    # Show current answer state
    instruction_text.draw()
    answer_text.draw()
    win.flip()

print (fileName)
#fileName = get_typed_answer()
#print(fileName)

#win.close()