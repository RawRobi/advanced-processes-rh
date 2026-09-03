import pgzrun
"""
COMPONENT TWO

All images to be imported need to be to a scale of 3x
"""

WIDTH = 1080
HEIGHT = 540

#This lets the screen move to designated points
SCREEN_X = [2160, 1080, 0, -1080]
direction = 0

FULL_MENU = Actor("full_menu.png")
FULL_MENU.y = 270

MENU_BUTTON_WIDTH = 360
MENU_BUTTON_HEIGHT = 90
MENU_BUTTON_X = 220
MENU_BUTTON_Y_DIFFERENCE = 130
UI_BUTTON_SIDE = 90
UI_BUTTON_SPACING = 85

play_button = Actor("menu_play_text.png")
PLAY_BUTTON_DEFAULT = play_button
PLAY_BUTTON_HOVER = Actor("menu_play_text_hover.png")
play_button.x = MENU_BUTTON_X
play_button.y = 195
PLAY_BUTTON_DEFAULT.pos = play_button.pos
PLAY_BUTTON_HOVER.pos = play_button.pos
PLAY_BUTTON_AREA = [
    play_button.x - (MENU_BUTTON_WIDTH / 2),
    play_button.x + (MENU_BUTTON_WIDTH / 2),
    play_button.y - (MENU_BUTTON_HEIGHT / 2),
    play_button.y + (MENU_BUTTON_HEIGHT / 2)
]

credits_button = Actor("menu_credits_text.png")
CREDITS_BUTTON_DEFAULT = credits_button
CREDITS_BUTTON_HOVER = Actor("menu_credits_text_hover.png")
credits_button.x = MENU_BUTTON_X
credits_button.y = play_button.y + MENU_BUTTON_Y_DIFFERENCE
CREDITS_BUTTON_DEFAULT.pos = credits_button.pos
CREDITS_BUTTON_HOVER.pos = credits_button.pos
CREDITS_BUTTON_AREA = [
    credits_button.x - (MENU_BUTTON_WIDTH / 2),
    credits_button.x + (MENU_BUTTON_WIDTH / 2),
    credits_button.y - (MENU_BUTTON_HEIGHT / 2),
    credits_button.y + (MENU_BUTTON_HEIGHT / 2)
]

debug_button = Actor("menu_debug_text_off.png")
DEBUG_BUTTON_ON = Actor("menu_debug_text_on.png")
DEBUG_BUTTON_OFF = debug_button
DEBUG_BUTTON_ON_HOVER = Actor("menu_debug_text_on_hover.png")
DEBUG_BUTTON_OFF_HOVER = Actor("menu_debug_text_off_hover.png")
debug_button.x = MENU_BUTTON_X
debug_button.y = credits_button.y + MENU_BUTTON_Y_DIFFERENCE
DEBUG_BUTTON_ON.pos = debug_button.pos
DEBUG_BUTTON_OFF.pos = debug_button.pos
DEBUG_BUTTON_ON_HOVER.pos = debug_button.pos
DEBUG_BUTTON_OFF_HOVER.pos = debug_button.pos
DEBUG_BUTTON_AREA = [
    debug_button.x - (MENU_BUTTON_WIDTH / 2),
    debug_button.x + (MENU_BUTTON_WIDTH / 2),
    debug_button.y - (MENU_BUTTON_HEIGHT / 2),
    debug_button.y + (MENU_BUTTON_HEIGHT / 2)
]

home_button = Actor("home_button.png")
HOME_BUTTON_DEFAULT = home_button
HOME_BUTTON_HOVER = Actor("home_button_hover.png")
home_button.x = 995
home_button.y = 85
HOME_BUTTON_DEFAULT.pos = home_button.pos
HOME_BUTTON_HOVER.pos = home_button.pos
HOME_BUTTON_AREA = [
    home_button.x - (UI_BUTTON_SIDE / 2),
    home_button.x + (UI_BUTTON_SIDE / 2),
    home_button.y - (UI_BUTTON_SIDE / 2),
    home_button.y + (UI_BUTTON_SIDE / 2)
]


# screens being (in order) credits, main menu, difficulty select, and the game
current_screen = 1
FULL_MENU.x = SCREEN_X[current_screen]
debug = False


def update():
    global debug
    global current_screen
    global SCREEN_X

def on_mouse_move(pos):
    global debug
    global play_button
    global credits_button
    global debug_button
    global home_button
    if current_screen == 0:
        if (
            pos[0] >= HOME_BUTTON_AREA[0] and
            pos[0] <= HOME_BUTTON_AREA[1] and
            pos[1] >= HOME_BUTTON_AREA[2] and
            pos[1] <= HOME_BUTTON_AREA[3]
            ):
            if debug:
                print("back to home page")
            home_button = HOME_BUTTON_HOVER
        else:
            home_button = HOME_BUTTON_DEFAULT
    if current_screen == 1:
        if (
            pos[0] >= PLAY_BUTTON_AREA[0] and
            pos[0] <= PLAY_BUTTON_AREA[1] and
            pos[1] >= PLAY_BUTTON_AREA[2] and
            pos[1] <= PLAY_BUTTON_AREA[3]
            ):
            if debug:
                print("hover play buton")
            play_button = PLAY_BUTTON_HOVER
        else:
            play_button = PLAY_BUTTON_DEFAULT
        if (
            pos[0] >= CREDITS_BUTTON_AREA[0] and
            pos[0] <= CREDITS_BUTTON_AREA[1] and
            pos[1] >= CREDITS_BUTTON_AREA[2] and
            pos[1] <= CREDITS_BUTTON_AREA[3]
            ):
            if debug:
                print("You are hovering the credits button")
            credits_button = CREDITS_BUTTON_HOVER
        else:
            credits_button = CREDITS_BUTTON_DEFAULT
        if (
            pos[0] >= DEBUG_BUTTON_AREA[0] and
            pos[0] <= DEBUG_BUTTON_AREA[1] and
            pos[1] >= DEBUG_BUTTON_AREA[2] and
            pos[1] <= DEBUG_BUTTON_AREA[3]
            ):
            if debug == True:
                print("hover credit buton")
                debug_button = DEBUG_BUTTON_ON_HOVER
            if debug == False:
                debug_button = DEBUG_BUTTON_OFF_HOVER
        else:
            if debug:
                debug_button = DEBUG_BUTTON_ON
            else:
                debug_button = DEBUG_BUTTON_OFF
    if current_screen == 2:
        if (
            pos[0] >= HOME_BUTTON_AREA[0] and
            pos[0] <= HOME_BUTTON_AREA[1] and
            pos[1] >= HOME_BUTTON_AREA[2] and
            pos[1] <= HOME_BUTTON_AREA[3]
            ):
            if debug == True:
                print("Home button")
            home_button = HOME_BUTTON_HOVER
        else:
            home_button = HOME_BUTTON_DEFAULT


def on_mouse_down(pos, button):
    
    global debug
    global debug_button
    global current_screen
    if current_screen == 0:
        if (
            pos[0] >= HOME_BUTTON_AREA[0] and
            pos[0] <= HOME_BUTTON_AREA[1] and
            pos[1] >= HOME_BUTTON_AREA[2] and
            pos[1] <= HOME_BUTTON_AREA[3] and
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
                debug_button = DEBUG_BUTTON_OFF
                debug = False
            elif debug == False:
                print("DEBUG is on now.")
                debug_button = DEBUG_BUTTON_ON
                debug = True
    if current_screen == 2:
        if (
            pos[0] >= HOME_BUTTON_AREA[0] and
            pos[0] <= HOME_BUTTON_AREA[1] and
            pos[1] >= HOME_BUTTON_AREA[2] and
            pos[1] <= HOME_BUTTON_AREA[3] and
            mouse.LEFT == button
            ):
            if debug == True:
                print("back to home page")
            current_screen = 1
        


def draw():
    FULL_MENU.draw()
    if FULL_MENU.x != SCREEN_X[current_screen]:
        if FULL_MENU.x > SCREEN_X[current_screen]:
            direction = -1
        else:
            direction = 1
        distance = FULL_MENU.x - SCREEN_X[current_screen]
        if distance < 0:
            distance *= -1
    if current_screen == 0:
        home_button.draw()
    if current_screen == 1:
        play_button.draw()
        credits_button.draw()
        debug_button.draw()
    if current_screen == 2:
        home_button.draw()


pgzrun.go() # This must be at the end of the code for it to run
