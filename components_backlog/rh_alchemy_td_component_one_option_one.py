import pgzrun
"""
COMPONENT ONE, OPTION ONE

All images to be imported need to be to a scale of 3x
"""

WIDTH = 1080
HEIGHT = 540

#This lets the screen move
SCREEN_X = [2160, 1080, 0, -1080]

TITLE_SCREEN = Actor("full_menu_3x.png")
TITLE_SCREEN.y = 270

MENU_BUTTON_WIDTH = 360
MENU_BUTTON_HEIGHT = 90
MENU_BUTTON_X = 220
MENU_BUTTON_Y_DIFFERENCE = 130
UI_BUTTON_SIDE = 90
UI_BUTTON_SPACING = 85

PLAY_BUTTON = Actor("menu_play_text_3x.png")
PLAY_BUTTON.x = MENU_BUTTON_X
PLAY_BUTTON.y = 195
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
DEBUG_BUTTON_ON = Actor("menu_debug_text_on_3x.png")
DEBUG_BUTTON_OFF = Actor("menu_debug_text_off_3x.png")
DEBUG_BUTTON_OFF.pos = DEBUG_BUTTON.pos
DEBUG_BUTTON.x = MENU_BUTTON_X
DEBUG_BUTTON_ON.x = DEBUG_BUTTON.x
DEBUG_BUTTON_OFF.x = DEBUG_BUTTON.x
DEBUG_BUTTON.y = CREDITS_BUTTON.y + MENU_BUTTON_Y_DIFFERENCE
DEBUG_BUTTON_ON.y = DEBUG_BUTTON.y
DEBUG_BUTTON_OFF.y = DEBUG_BUTTON.y
DEBUG_BUTTON_AREA = [
    DEBUG_BUTTON.x - (MENU_BUTTON_WIDTH / 2),
    DEBUG_BUTTON.x + (MENU_BUTTON_WIDTH / 2),
    DEBUG_BUTTON.y - (MENU_BUTTON_HEIGHT / 2),
    DEBUG_BUTTON.y + (MENU_BUTTON_HEIGHT / 2)
]

BACK_TO_HOME_BUTTON = Actor("credits_exit_button_3x.png")
BACK_TO_HOME_BUTTON.x = 995
BACK_TO_HOME_BUTTON.y = 85
BACK_TO_HOME_BUTTON_AREA = [
    BACK_TO_HOME_BUTTON.x - (UI_BUTTON_SIDE / 2),
    BACK_TO_HOME_BUTTON.x + (UI_BUTTON_SIDE / 2),
    BACK_TO_HOME_BUTTON.y - (UI_BUTTON_SIDE / 2),
    BACK_TO_HOME_BUTTON.y + (UI_BUTTON_SIDE / 2)
]


# screens being (in order) credits, main menu, difficulty select, and the game
current_screen = 1
debug = False


def update():
    global SCREEN_X
    global TITLE_SCREEN
    global current_screen


def on_mouse_down(pos, button):
    global debug
    global DEBUG_BUTTON
    global current_screen
    if current_screen == 0:
        if (
            pos[0] >= BACK_TO_HOME_BUTTON_AREA[0] and
            pos[0] <= BACK_TO_HOME_BUTTON_AREA[1] and
            pos[1] >= BACK_TO_HOME_BUTTON_AREA[2] and
            pos[1] <= BACK_TO_HOME_BUTTON_AREA[3] and
            mouse.LEFT == button
            ):
            if debug == True:
                print("back to home page")
            current_screen = 1
    if current_screen == 1:
        if (
            pos[0] >= PLAY_BUTTON_AREA[0] and
            pos[0] <= PLAY_BUTTON_AREA[1] and
            pos[1] >= PLAY_BUTTON_AREA[2] and
            pos[1] <= PLAY_BUTTON_AREA[3] and
            mouse.LEFT == button
            ):
            if debug == True:
                print("Congrats, you pressed the PLAY button.")
            current_screen = 2
        if (
            pos[0] >= CREDITS_BUTTON_AREA[0] and
            pos[0] <= CREDITS_BUTTON_AREA[1] and
            pos[1] >= CREDITS_BUTTON_AREA[2] and
            pos[1] <= CREDITS_BUTTON_AREA[3] and
            mouse.LEFT == button
            ):
            if debug == True:
                print("Congrats, you pressed the CREDITS button.")
            current_screen = 0
        if (
            pos[0] >= DEBUG_BUTTON_AREA[0] and
            pos[0] <= DEBUG_BUTTON_AREA[1] and
            pos[1] >= DEBUG_BUTTON_AREA[2] and
            pos[1] <= DEBUG_BUTTON_AREA[3] and
            mouse.LEFT == button
            ):
            if debug == True:
                print("DEBUG is off now.")
                DEBUG_BUTTON = DEBUG_BUTTON_OFF
                debug = False
            elif debug == False:
                print("DEBUG is on now.")
                DEBUG_BUTTON = DEBUG_BUTTON_ON
                debug = True
    if current_screen == 2:
        if (
            pos[0] >= BACK_TO_HOME_BUTTON_AREA[0] and
            pos[0] <= BACK_TO_HOME_BUTTON_AREA[1] and
            pos[1] >= BACK_TO_HOME_BUTTON_AREA[2] and
            pos[1] <= BACK_TO_HOME_BUTTON_AREA[3] and
            mouse.LEFT == button
            ):
            if debug == True:
                print("back to home page")
            current_screen = 1
        


def draw():
    TITLE_SCREEN.x = SCREEN_X[current_screen]
    TITLE_SCREEN.draw()
    if current_screen == 0:
        BACK_TO_HOME_BUTTON.draw()
    if current_screen == 1:
        PLAY_BUTTON.draw()
        CREDITS_BUTTON.draw()
        DEBUG_BUTTON.draw()
    if current_screen == 2:
        BACK_TO_HOME_BUTTON.draw()
    if TITLE_SCREEN.x != SCREEN_X[current_screen]:
        if TITLE_SCREEN.x == SCREEN_X[0]:
            BACK_TO_HOME_BUTTON.clear()
        if TITLE_SCREEN.x == SCREEN_X[1]:
            PLAY_BUTTON.clear()
            CREDITS_BUTTON.clear()
            DEBUG_BUTTON.clear()
        TITLE_SCREEN.x = SCREEN_X[current_screen]
        TITLE_SCREEN.draw()


pgzrun.go() # This must be at the end of the code for it to run
