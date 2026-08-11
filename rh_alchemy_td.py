import pgzrun
"""


All images to be imported need to be to a scale of 3x
"""

WIDTH = 960
HEIGHT = 540

TITLE_SCREEN = Actor("menu_background_3x.png")
TITLE_SCREEN.x = 480
TITLE_SCREEN.y = 270


def draw():
    TITLE_SCREEN.draw()
    TITLE_SCREEN.draw()


"""
Positions of buttons are
207, 207
207, 333
207, 459
"""

pgzrun.go()
# This must be at the end of the code for it to run
