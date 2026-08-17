import pgzrun
"""


All images to be imported need to be to a scale of 3x
"""

WIDTH = 960
HEIGHT = 540

TITLE_SCREEN = Actor("menu_background_3x.png")
TITLE_SCREEN.x = 480
TITLE_SCREEN.y = 270

debug = False
paused = False

MENU_BUTTON_WIDTH = 360
MENU_BUTTON_HEIGHT = 90
MENU_BUTTON_X = 200
MENU_BUTTON_Y_DIFFERENCE = 140

PLAY_BUTTON = Actor("menu_play_text_3x.png")
PLAY_BUTTON.x = MENU_BUTTON_X
PLAY_BUTTON.y = 200
PLAY_BUTTON_AREA = [
    PLAY_BUTTON.x - (MENU_BUTTON_WIDTH / 2),
    PLAY_BUTTON.x + (MENU_BUTTON_WIDTH / 2),
    PLAY_BUTTON.y - (MENU_BUTTON_HEIGHT / 2),
    PLAY_BUTTON.y + (MENU_BUTTON_HEIGHT / 2)
]

CREDITS_BUTTON = Actor("menu_credits_text_3x.png")
CREDITS_BUTTON.x = MENU_BUTTON_X
CREDITS_BUTTON.y = PLAY_BUTTON.y + MENU_BUTTON_Y_DIFFERENCE
CREDITS_BUTTON_AREA = [
    CREDITS_BUTTON.x - (MENU_BUTTON_WIDTH / 2),
    CREDITS_BUTTON.x + (MENU_BUTTON_WIDTH / 2),
    CREDITS_BUTTON.y - (MENU_BUTTON_HEIGHT / 2),
    CREDITS_BUTTON.y + (MENU_BUTTON_HEIGHT / 2)
]

DEBUG_BUTTON = Actor("menu_debug_text_off_3x.png")
DEBUG_BUTTON.x = MENU_BUTTON_X
DEBUG_BUTTON.y = CREDITS_BUTTON.y + MENU_BUTTON_Y_DIFFERENCE
DEBUG_BUTTON_AREA = [
    DEBUG_BUTTON.x - (MENU_BUTTON_WIDTH / 2),
    DEBUG_BUTTON.x + (MENU_BUTTON_WIDTH / 2),
    DEBUG_BUTTON.y - (MENU_BUTTON_HEIGHT / 2),
    DEBUG_BUTTON.y + (MENU_BUTTON_HEIGHT / 2)
]

screens = ["main_menu", "credits", "map", ]
current_screen = 0

def on_mouse_down(pos, button):
    if current_screen == 0:
        if debug == True:
            DEBUG_BUTTON = Actor("menu_debug_text_on_3x.png")
        else:
            DEBUG_BUTTON = Actor("menu_debug_text_off_3x.png")
        if (
            pos[0] >= PLAY_BUTTON_AREA[0] and
            pos[0] <= PLAY_BUTTON_AREA[1] and
            pos[1] >= PLAY_BUTTON_AREA[2] and
            pos[1] <= PLAY_BUTTON_AREA[3] and
            mouse.LEFT == button
            ):
            print("Congrats, you pressed the PLAY button.")
        if (
            pos[0] >= CREDITS_BUTTON_AREA[0] and
            pos[0] <= CREDITS_BUTTON_AREA[1] and
            pos[1] >= CREDITS_BUTTON_AREA[2] and
            pos[1] <= CREDITS_BUTTON_AREA[3] and
            mouse.LEFT == button
            ):
            print("Congrats, you pressed the CREDITS button.")
        if (
            pos[0] >= DEBUG_BUTTON_AREA[0] and
            pos[0] <= DEBUG_BUTTON_AREA[1] and
            pos[1] >= DEBUG_BUTTON_AREA[2] and
            pos[1] <= DEBUG_BUTTON_AREA[3] and
            mouse.LEFT == button
            ):
            print("Congrats, you pressed the DEBUG button.")
            debug = True


def draw():
    TITLE_SCREEN.draw()
    PLAY_BUTTON.draw()
    CREDITS_BUTTON.draw()
    DEBUG_BUTTON.draw()

pgzrun.go()
# This must be at the end of the code for it to run
