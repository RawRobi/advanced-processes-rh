import pgzrun
"""
COMPONENT ONE UPDATES ON FEEDBACK

All images to be imported need to be to a scale of 3x
"""

WIDTH = 1080
HEIGHT = 540

#This lets the screen move to designated points of each screen
SCREEN_X = [2160, 1080, 0, -1080]

direction = 0

game_start = False

FULL_MENU = Actor("full_menu.png")
FULL_MENU.y = 270

MENU_BUTTON_WIDTH = 360
MENU_BUTTON_HEIGHT = 90
MENU_BUTTON_X = 220
MENU_BUTTON_Y_DIFFERENCE = 130
UI_BUTTON_SIDE = 90
UI_BUTTON_SPACING = 85

DIFFICULTY_ICON_HEIGHT = 144
DIFFICULTY_ICON_WIDTH = 84

play_button = Actor("menu_play_text.png")
PLAY_BUTTON_DEFAULT = play_button
PLAY_BUTTON_HOVER = Actor("menu_play_text_hover.png")
play_button.x = MENU_BUTTON_X
play_button.y = 195
PLAY_BUTTON_DEFAULT.pos = play_button.pos
PLAY_BUTTON_HOVER.pos = play_button.pos
play_button_area = [
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
credits_button_area = [
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
debug_button_area = [
    debug_button.x - (MENU_BUTTON_WIDTH / 2),
    debug_button.x + (MENU_BUTTON_WIDTH / 2),
    debug_button.y - (MENU_BUTTON_HEIGHT / 2),
    debug_button.y + (MENU_BUTTON_HEIGHT / 2)
]

back_from_credits = Actor("back_from_credits.png")
BACK_FROM_CREDITS_DEFAULT = back_from_credits
BACK_FROM_CREDITS_HOVER = Actor("back_from_credits_hover.png")
back_from_credits.x = -85
back_from_credits.y = 85
back_from_credits_area = [
    back_from_credits.x - (UI_BUTTON_SIDE / 2),
    back_from_credits.x + (UI_BUTTON_SIDE / 2),
    back_from_credits.y - (UI_BUTTON_SIDE / 2),
    back_from_credits.y + (UI_BUTTON_SIDE / 2)
]

back_from_play = Actor("back_from_play.png")
BACK_FROM_PLAY_DEFAULT = back_from_play
BACK_FROM_PLAY_HOVER = Actor("back_from_play_hover.png")
back_from_play.x = 2075
back_from_play.y = 85
back_from_play_area = [
    back_from_play.x - (UI_BUTTON_SIDE / 2),
    back_from_play.x + (UI_BUTTON_SIDE / 2),
    back_from_play.y - (UI_BUTTON_SIDE / 2),
    back_from_play.y + (UI_BUTTON_SIDE / 2)
]

difficulty_display = Actor("difficulty_display.png")
difficulty_display.x = 1360
difficulty_display.y = 495

no_difficulty_display = Actor("difficulty_display_none.png")
easy_difficulty_display = Actor("difficulty_display_easy.png")
medium_difficulty_display = Actor("difficulty_display_medium.png")
hard_difficulty_display = Actor("difficulty_display_hard.png")
current_difficulty_display = no_difficulty_display
current_difficulty_display.x = 1780
current_difficulty_display.y = 495

easy_difficulty_icon_default = Actor("difficulty_easy_icon.png")
easy_difficulty_icon_hover = Actor("difficulty_easy_icon_hover.png")
easy_difficulty_icon_select = Actor("difficulty_easy_icon_select.png")
easy_difficulty_icon = easy_difficulty_icon_default
easy_difficulty_icon.x = 1220
easy_difficulty_icon.y = 320
easy_difficulty_icon_area = [
    easy_difficulty_icon.x - (DIFFICULTY_ICON_HEIGHT / 2),
    easy_difficulty_icon.x + (DIFFICULTY_ICON_HEIGHT / 2),
    easy_difficulty_icon.y - (DIFFICULTY_ICON_WIDTH / 2),
    easy_difficulty_icon.y + (DIFFICULTY_ICON_WIDTH / 2)
    ]

# number values for difficulties being, in order:
# none, easy, medium and hard
difficulty = 0

current_screen = 1
FULL_MENU.x = SCREEN_X[current_screen]
debug = False

def move_all(movement, direction):
    global FULL_MENU
    global back_from_credits
    global play_button, credits_button, debug_button
    global back_from_play, difficulty_display, current_difficulty_display
    global easy_difficulty_icon
    FULL_MENU.x += movement * direction
    back_from_credits.x += movement * direction
    play_button.x += movement * direction
    credits_button.x += + movement * direction
    debug_button.x += movement * direction
    back_from_play.x += movement * direction
    difficulty_display.x += movement * direction
    current_difficulty_display.x += movement * direction
    easy_difficulty_icon.x += movement * direction


def snap(x_of_screen, screen):
    global FULL_MENU
    global back_from_credits
    global play_button, credits_button, debug_button
    global back_from_play, difficulty_display, current_difficulty_display
    global easy_difficulty_icon
    FULL_MENU.x = x_of_screen
    if screen == 0:
        back_from_credits.x = 995
    if screen == 1:
        play_button.x = MENU_BUTTON_X
        credits_button.x = MENU_BUTTON_X
        debug_button.x = MENU_BUTTON_X
    if screen == 2:
        back_from_play.x = 995
        difficulty_display.x = 85
        current_difficulty_display.x = 550
        easy_difficulty_icon.x = 140


def update():
    global back_from_credits_area
    global play_button_area
    global credits_button_area
    global debug_button_area
    global back_from_play_area, current_difficulty_display
    global easy_difficulty_icon_area, easy_difficulty_icon
    if game_start == False:
        if FULL_MENU.x !=- SCREEN_X[current_screen]:
            if FULL_MENU.x >= SCREEN_X[current_screen]:
                direction = -1
            else:
                direction = 1
            distance = FULL_MENU.x - SCREEN_X[current_screen]
            if distance < 0:
                distance *= -1
            if distance >= 800:
                move = 100
            elif distance >= 600:
                move = 80
            elif distance >= 400:
                move = 40
            elif distance >= 200:
                move = 20
            elif distance >= 100:
                move = 10
            elif distance >= 15:
                move = 5
            else:
                move = 1
            if distance < 1:
                snap(SCREEN_X[current_screen], current_screen)
            else:
                move_all(move, direction)
        back_from_credits_area = [
            back_from_credits.x - (UI_BUTTON_SIDE / 2),
            back_from_credits.x + (UI_BUTTON_SIDE / 2),
            back_from_credits.y - (UI_BUTTON_SIDE / 2),
            back_from_credits.y + (UI_BUTTON_SIDE / 2)
        ]
        play_button_area = [
            play_button.x - (MENU_BUTTON_WIDTH / 2),
            play_button.x + (MENU_BUTTON_WIDTH / 2),
            play_button.y - (MENU_BUTTON_HEIGHT / 2),
            play_button.y + (MENU_BUTTON_HEIGHT / 2)
        ]
        credits_button_area = [
            credits_button.x - (MENU_BUTTON_WIDTH / 2),
            credits_button.x + (MENU_BUTTON_WIDTH / 2),
            credits_button.y - (MENU_BUTTON_HEIGHT / 2),
            credits_button.y + (MENU_BUTTON_HEIGHT / 2)
        ]
        debug_button_area = [
            debug_button.x - (MENU_BUTTON_WIDTH / 2),
            debug_button.x + (MENU_BUTTON_WIDTH / 2),
            debug_button.y - (MENU_BUTTON_HEIGHT / 2),
            debug_button.y + (MENU_BUTTON_HEIGHT / 2)
        ]
        back_from_play_area = [
            back_from_play.x - (UI_BUTTON_SIDE / 2),
            back_from_play.x + (UI_BUTTON_SIDE / 2),
            back_from_play.y - (UI_BUTTON_SIDE / 2),
            back_from_play.y + (UI_BUTTON_SIDE / 2)
        ]
        easy_difficulty_icon_area = [
            easy_difficulty_icon.x - (DIFFICULTY_ICON_HEIGHT / 2),
            easy_difficulty_icon.x + (DIFFICULTY_ICON_HEIGHT / 2),
            easy_difficulty_icon.y - (DIFFICULTY_ICON_WIDTH / 2),
            easy_difficulty_icon.y + (DIFFICULTY_ICON_WIDTH / 2)
        ]
        PLAY_BUTTON_DEFAULT.pos = play_button.pos
        PLAY_BUTTON_HOVER.pos = play_button.pos
        BACK_FROM_CREDITS_DEFAULT.pos = back_from_credits.pos
        BACK_FROM_CREDITS_HOVER.pos = back_from_credits.pos
        CREDITS_BUTTON_DEFAULT.pos = credits_button.pos
        CREDITS_BUTTON_HOVER.pos = credits_button.pos
        DEBUG_BUTTON_ON.pos = debug_button.pos
        DEBUG_BUTTON_OFF.pos = debug_button.pos
        DEBUG_BUTTON_ON_HOVER.pos = debug_button.pos
        DEBUG_BUTTON_OFF_HOVER.pos = debug_button.pos
        BACK_FROM_PLAY_DEFAULT.pos = back_from_play.pos
        BACK_FROM_PLAY_HOVER.pos = back_from_play.pos
        no_difficulty_display.pos = current_difficulty_display.pos
        easy_difficulty_display.pos = current_difficulty_display.pos
        medium_difficulty_display.pos = current_difficulty_display.pos
        hard_difficulty_display.pos = current_difficulty_display.pos
        easy_difficulty_icon_hover.pos = easy_difficulty_icon.pos
        easy_difficulty_icon_select.pos = easy_difficulty_icon.pos
        if difficulty == 1:
            current_difficulty_display = easy_difficulty_display
            easy_difficulty_icon = easy_difficulty_icon_select
        


def on_mouse_move(pos):
    global debug
    global back_from_credits, play_button
    global credits_button, debug_button, back_from_play
    global difficulty, easy_difficulty_icon
    if current_screen == 0:
        if (
            pos[0] >= back_from_credits_area[0] and
            pos[0] <= back_from_credits_area[1] and
            pos[1] >= back_from_credits_area[2] and
            pos[1] <= back_from_credits_area[3]
            ):
            if debug:
                print("back to home page")
            back_from_credits = BACK_FROM_CREDITS_HOVER
        else:
            back_from_credits = BACK_FROM_CREDITS_DEFAULT
    if current_screen == 1:
        if (
            pos[0] >= play_button_area[0] and
            pos[0] <= play_button_area[1] and
            pos[1] >= play_button_area[2] and
            pos[1] <= play_button_area[3]
            ):
            if debug:
                print("hover play buton")
            play_button = PLAY_BUTTON_HOVER
        else:
            play_button = PLAY_BUTTON_DEFAULT
        if (
            pos[0] >= credits_button_area[0] and
            pos[0] <= credits_button_area[1] and
            pos[1] >= credits_button_area[2] and
            pos[1] <= credits_button_area[3]
            ):
            if debug:
                print("You are hovering the credits button")
            credits_button = CREDITS_BUTTON_HOVER
        else:
            credits_button = CREDITS_BUTTON_DEFAULT
        if (
            pos[0] >= debug_button_area[0] and
            pos[0] <= debug_button_area[1] and
            pos[1] >= debug_button_area[2] and
            pos[1] <= debug_button_area[3]
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
            pos[0] >= back_from_play_area[0] and
            pos[0] <= back_from_play_area[1] and
            pos[1] >= back_from_play_area[2] and
            pos[1] <= back_from_play_area[3]
            ):
            if debug == True:
                print("Home button")
            back_from_play = BACK_FROM_PLAY_HOVER
        else:
            back_from_play = BACK_FROM_PLAY_DEFAULT
            if (
                pos[0] >= easy_difficulty_icon_area[0] and
                pos[0] <= easy_difficulty_icon_area[1] and
                pos[1] >= easy_difficulty_icon_area[2] and
                pos[1] <= easy_difficulty_icon_area[3] and
                difficulty != 1
                ):
                if debug == True:
                    print("easy difficulty")
                easy_difficulty_icon = easy_difficulty_icon_hover
            elif difficulty != 1:
                easy_difficulty_icon = easy_difficulty_icon_default


def on_mouse_down(pos, button):
    global debug, debug_button
    global current_screen, difficulty
    global easy_difficulty_icon
    if current_screen == 0:
        if (
            pos[0] >= back_from_credits_area[0] and
            pos[0] <= back_from_credits_area[1] and
            pos[1] >= back_from_credits_area[2] and
            pos[1] <= back_from_credits_area[3] and
            mouse.LEFT == button
            ):
            if debug == True:
                print("back to home page")
            current_screen = 1
    if current_screen == 1:
        if (
            pos[0] >= play_button_area[0] and
            pos[0] <= play_button_area[1] and
            pos[1] >= play_button_area[2] and
            pos[1] <= play_button_area[3] and
            mouse.LEFT == button
            ):
            if debug == True:
                print("Congrats, you pressed the PLAY button.")
            current_screen = 2
        if (
            pos[0] >= credits_button_area[0] and
            pos[0] <= credits_button_area[1] and
            pos[1] >= credits_button_area[2] and
            pos[1] <= credits_button_area[3] and
            mouse.LEFT == button
            ):
            if debug == True:
                print("Congrats, you pressed the CREDITS button.")
            current_screen = 0
        if (
            pos[0] >= debug_button_area[0] and
            pos[0] <= debug_button_area[1] and
            pos[1] >= debug_button_area[2] and
            pos[1] <= debug_button_area[3] and
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
            pos[0] >= back_from_play_area[0] and
            pos[0] <= back_from_play_area[1] and
            pos[1] >= back_from_play_area[2] and
            pos[1] <= back_from_play_area[3] and
            mouse.LEFT == button
            ):
            if debug == True:
                print("back to home page")
            current_screen = 1
        if difficulty != 1:
            if (
                pos[0] >= easy_difficulty_icon_area[0] and
                pos[0] <= easy_difficulty_icon_area[1] and
                pos[1] >= easy_difficulty_icon_area[2] and
                pos[1] <= easy_difficulty_icon_area[3]
                ):
                if debug == True:
                    print("easy difficulty pressed")
                easy_difficulty_icon = easy_difficulty_icon_select
                difficulty = 1


def draw():
    FULL_MENU.draw()
    back_from_credits.draw()
    play_button.draw()
    credits_button.draw()
    debug_button.draw()
    back_from_play.draw()
    difficulty_display.draw()
    current_difficulty_display.draw()
    easy_difficulty_icon.draw()


pgzrun.go() # This must be at the end of the code for it to run
