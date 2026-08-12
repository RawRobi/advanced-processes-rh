import pgzrun
"""


All images to be imported need to be to a scale of 3x
"""

WIDTH = 960
HEIGHT = 540

TITLE_SCREEN = Actor("menu_background_3x.png")
TITLE_SCREEN.x = 480
TITLE_SCREEN.y = 270

PLAY = Actor("menu_play_text_3x.png")
PLAY.x = 200
PLAY.y = 200
PLAY_BUTTON_LENGTH = 360
PLAY_BUTTON_WIDTH = 90
PLAY_BUTTON_AREA = [
    PLAY.x - (PLAY_BUTTON_LENGTH / 2),
    PLAY.x + (PLAY_BUTTON_LENGTH / 2),
    PLAY.y - (PLAY_BUTTON_WIDTH / 2),
    PLAY.y + (PLAY_BUTTON_WIDTH / 2)
    ]

screens = ["main_menu", "map"]
current_screen = 0

#Current problem - The button keeps saying it's clicked.

def on_mouse_down(pos, button):
    if current_screen == 0:
        if (
            pos[0] >= PLAY_BUTTON_AREA[0] and
            pos[0] <= PLAY_BUTTON_AREA[1] and
            pos[1] >= PLAY_BUTTON_AREA[2] and
            pos[1] <= PLAY_BUTTON_AREA[3] and
            mouse.LEFT == button
            ):
            print("Congrats, you pressed the PLAY button.")


def draw():
    TITLE_SCREEN.draw()
    PLAY.draw()


"""
Positions of buttons are
207, 207
207, 333
207, 459
"""

pgzrun.go()
# This must be at the end of the code for it to run
