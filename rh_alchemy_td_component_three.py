import pgzrun
import random
"""
COMPONENT TWO UPDATING ON FEEDBACK

All images to be imported need to be to a scale of 3x
"""

WIDTH = 1080
HEIGHT = 540

#This lets the screen move to designated points of each screen
SCREEN_X = [3240.0, 2160.0, 1080.0, -2160.0]

TOWERS_STATS_DICT = {
    "": []
    }

direction = 0

game_start = False

FULL_MENU = Actor("full_menu.png")
FULL_MENU.y = 270


# All of the buttons are set up as the following way
# The states it can be (e.g. hovered, selected and default) are made
# The coordinates of the button are put in.
# Then the area (based off of the coordinates and the buttons dimensions)


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

NO_DIFFICULTY_DISPLAY = Actor("difficulty_display_none.png")
EASY_DIFFICULTY_DISPLAY = Actor("difficulty_display_easy.png")
MEDIUM_DIFFICULTY_DISPLAY = Actor("difficulty_display_medium.png")
HARD_DIFFICULTY_DISPLAY = Actor("difficulty_display_hard.png")
current_difficulty_display = NO_DIFFICULTY_DISPLAY
current_difficulty_display.x = 1780
current_difficulty_display.y = 495

EASY_DIFFICULTY_ICON_DEFAULT = Actor("difficulty_easy_icon.png")
EASY_DIFFICULTY_ICON_HOVER = Actor("difficulty_easy_icon_hover.png")
EASY_DIFFICULTY_ICON_SELECT = Actor("difficulty_easy_icon_select.png")
easy_difficulty_icon = EASY_DIFFICULTY_ICON_DEFAULT
easy_difficulty_icon.x = 1220
easy_difficulty_icon.y = 320
easy_difficulty_icon_area = [
    easy_difficulty_icon.x - (DIFFICULTY_ICON_WIDTH / 2),
    easy_difficulty_icon.x + (DIFFICULTY_ICON_WIDTH / 2),
    easy_difficulty_icon.y - (DIFFICULTY_ICON_HEIGHT / 2),
    easy_difficulty_icon.y + (DIFFICULTY_ICON_HEIGHT / 2)
    ]

MEDIUM_DIFFICULTY_ICON_DEFAULT = Actor("difficulty_medium_icon.png")
MEDIUM_DIFFICULTY_ICON_HOVER = Actor("difficulty_medium_icon_hover.png")
MEDIUM_DIFFICULTY_ICON_SELECT = Actor("difficulty_medium_icon_select.png")
medium_difficulty_icon = MEDIUM_DIFFICULTY_ICON_DEFAULT
medium_difficulty_icon.x = 1520
medium_difficulty_icon.y = 280
medium_difficulty_icon_area = [
    medium_difficulty_icon.x - (DIFFICULTY_ICON_WIDTH / 2),
    medium_difficulty_icon.x + (DIFFICULTY_ICON_WIDTH / 2),
    medium_difficulty_icon.y - (DIFFICULTY_ICON_HEIGHT / 2),
    medium_difficulty_icon.y + (DIFFICULTY_ICON_HEIGHT / 2)
    ]

HARD_DIFFICULTY_ICON_DEFAULT = Actor("difficulty_hard_icon.png")
HARD_DIFFICULTY_ICON_HOVER = Actor("difficulty_hard_icon_hover.png")
HARD_DIFFICULTY_ICON_SELECT = Actor("difficulty_hard_icon_select.png")
hard_difficulty_icon = HARD_DIFFICULTY_ICON_DEFAULT
hard_difficulty_icon.x = 1950
hard_difficulty_icon.y = 310
hard_difficulty_icon_area = [
    hard_difficulty_icon.x - (DIFFICULTY_ICON_WIDTH / 2),
    hard_difficulty_icon.x + (DIFFICULTY_ICON_WIDTH / 2),
    hard_difficulty_icon.y - (DIFFICULTY_ICON_HEIGHT / 2),
    hard_difficulty_icon.y + (DIFFICULTY_ICON_HEIGHT / 2)
    ]

GAME_START_BUTTON_DEFAULT = Actor("difficulty_start_text.png")
GAME_START_BUTTON_HOVER = Actor("difficulty_start_text_hover.png")
GAME_START_BUTTON_UNSELECTABLE = Actor("difficulty_start_text_unselectable.png")
game_start_button = GAME_START_BUTTON_UNSELECTABLE
game_start_button.x = 1810
game_start_button.y = 85
game_start_button_area = [
    game_start_button.x - (MENU_BUTTON_WIDTH / 2),
    game_start_button.x + (MENU_BUTTON_WIDTH / 2),
    game_start_button.y - (MENU_BUTTON_HEIGHT / 2),
    game_start_button.y + (MENU_BUTTON_HEIGHT / 2)
    ]

drop_down_ui = Actor("drop_down_ui.png")
DROP_DOWN_STATES = [270, -60]
drop_down_state = 1 # 0 being shown, 1 being hidden
drop_down_ui.x = 4860
drop_down_ui.y = DROP_DOWN_STATES[drop_down_state]

DROP_DOWN_BUTTON_UP_DEFAULT = Actor("button_up.png")
DROP_DOWN_BUTTON_UP_HOVER = Actor("button_up_selected.png")
DROP_DOWN_BUTTON_DOWN_DEFAULT = Actor("button_down.png")
DROP_DOWN_BUTTON_DOWN_HOVER = Actor("button_down_selected.png")
drop_down_button = DROP_DOWN_BUTTON_UP_DEFAULT
drop_down_button.x = drop_down_ui.x
drop_down_button.y = drop_down_ui.y + 120
drop_down_button_area = [
    drop_down_button.x - 48,
    drop_down_button.x + 48,
    drop_down_button.y - 48,
    drop_down_button.y + 48
    ]

game_bar = Actor("game_bar.png")
GAME_BAR_STATES = [18, 1068]
game_bar_state = 0
game_bar.x = 4860
game_bar.y = drop_down_ui.y - 120

GAME_BAR_SWITCHER_LEFT = Actor("bar_switcher_left.png")
GAME_BAR_SWITCHER_RIGHT = Actor("bar_switcher_right.png")
game_bar_switcher = GAME_BAR_SWITCHER_LEFT
game_bar_switcher.x = 5240
game_bar_switcher.y = -60
game_bar_switcher_area = [
    game_bar_switcher.x - 96,
    game_bar_switcher.x + 96,
    game_bar_switcher.y - 48,
    game_bar_switcher.y + 48
    ]

# number values for difficulties being, in order:
# none, easy, medium and hard
difficulty = 0

current_screen = 1
FULL_MENU.x = SCREEN_X[current_screen]
debug = False

def move_all(movement, direction):
    # To move all the buttons and the screen at the same time
    global FULL_MENU
    global back_from_credits
    global play_button, credits_button, debug_button
    global back_from_play, difficulty_display, current_difficulty_display
    global easy_difficulty_icon, medium_difficulty_icon, hard_difficulty_icon
    global game_start_button, game_bar
    global drop_down_ui, drop_down_button
    back_from_credits.x += movement * direction
    play_button.x += movement * direction
    credits_button.x += + movement * direction
    debug_button.x += movement * direction
    back_from_play.x += movement * direction
    difficulty_display.x += movement * direction
    current_difficulty_display.x += movement * direction
    easy_difficulty_icon.x += movement * direction
    medium_difficulty_icon.x += movement * direction
    hard_difficulty_icon.x += movement * direction
    game_start_button.x += movement * direction
    FULL_MENU.x += movement * direction
    drop_down_ui.x += movement * direction
    drop_down_button.x += movement * direction
    game_bar.x += movement * direction
    game_bar_switcher.x += movement * direction
    



def update():
    global back_from_credits_area
    global play_button_area
    global credits_button_area
    global debug_button_area
    global back_from_play_area, current_difficulty_display
    global easy_difficulty_icon_area, easy_difficulty_icon
    global medium_difficulty_icon_area, medium_difficulty_icon
    global hard_difficulty_icon_area, hard_difficulty_icon
    global game_start_button_area
    global drop_down_ui, drop_down_button_area, game_bar
    global game_bar_switcher_area, game_bar_switcher
    if FULL_MENU.x != SCREEN_X[current_screen]:
        if FULL_MENU.x >= SCREEN_X[current_screen]:
            direction = -1 # To the right
        else:
            direction = 1 # To the left
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
        elif distance >= 9:
            move = 5
        else:
            move = 1
        if distance != 0:
            move_all(move, direction)
    # comment to seperate the moving functions
    if (
        current_screen == 3 and
        FULL_MENU.x == SCREEN_X[current_screen] and
        drop_down_ui.y != DROP_DOWN_STATES[drop_down_state]
        ):
        if drop_down_ui.y >= DROP_DOWN_STATES[drop_down_state]:
            direction = -1 # To the right
        else:
            direction = 1 # To the left            
        distance = drop_down_ui.y - DROP_DOWN_STATES[drop_down_state]
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
        elif distance >= 9:
            move = 5
        else:
            move = 1
        if distance != 0:
            drop_down_ui.y += move * direction
            drop_down_button.y += move * direction
            game_bar_switcher.y += move * direction
            game_bar.y += move * direction
    # comment to seperate the functions
    if (
        current_screen == 3 and
        FULL_MENU.x == SCREEN_X[current_screen] and
        game_bar.x != GAME_BAR_STATES[game_bar_state]
        ):
        if game_bar.x >= GAME_BAR_STATES[game_bar_state]:
            direction = -1 # To the right
        else:
            direction = 1 # To the left            
        distance = game_bar.x - GAME_BAR_STATES[game_bar_state]
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
        elif distance >= 9:
            move = 5
        else:
            move = 1
        if distance != 0:
            game_bar.x += move * direction
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
        easy_difficulty_icon.x - (DIFFICULTY_ICON_WIDTH / 2),
        easy_difficulty_icon.x + (DIFFICULTY_ICON_WIDTH / 2),
        easy_difficulty_icon.y - (DIFFICULTY_ICON_HEIGHT / 2),
        easy_difficulty_icon.y + (DIFFICULTY_ICON_HEIGHT / 2)
    ]
    medium_difficulty_icon_area = [
        medium_difficulty_icon.x - (DIFFICULTY_ICON_WIDTH / 2),
        medium_difficulty_icon.x + (DIFFICULTY_ICON_WIDTH / 2),
        medium_difficulty_icon.y - (DIFFICULTY_ICON_HEIGHT / 2),
        medium_difficulty_icon.y + (DIFFICULTY_ICON_HEIGHT / 2)
    ]
    hard_difficulty_icon_area = [
        hard_difficulty_icon.x - (DIFFICULTY_ICON_WIDTH / 2),
        hard_difficulty_icon.x + (DIFFICULTY_ICON_WIDTH / 2),
        hard_difficulty_icon.y - (DIFFICULTY_ICON_HEIGHT / 2),
        hard_difficulty_icon.y + (DIFFICULTY_ICON_HEIGHT / 2)
    ]
    game_start_button_area = [
        game_start_button.x - (MENU_BUTTON_WIDTH / 2),
        game_start_button.x + (MENU_BUTTON_WIDTH / 2),
        game_start_button.y - (MENU_BUTTON_HEIGHT / 2),
        game_start_button.y + (MENU_BUTTON_HEIGHT / 2)
    ]
    drop_down_button_area = [
        drop_down_button.x - 48,
        drop_down_button.x + 48,
        drop_down_button.y - 48,
        drop_down_button.y + 48
    ]
    game_bar_switcher_area = [
        game_bar_switcher.x - 96,
        game_bar_switcher.x + 96,
        game_bar_switcher.y - 48,
        game_bar_switcher.y + 48
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
    NO_DIFFICULTY_DISPLAY.pos = current_difficulty_display.pos
    EASY_DIFFICULTY_DISPLAY.pos = current_difficulty_display.pos
    MEDIUM_DIFFICULTY_DISPLAY.pos = current_difficulty_display.pos
    HARD_DIFFICULTY_DISPLAY.pos = current_difficulty_display.pos
    EASY_DIFFICULTY_ICON_HOVER.pos = easy_difficulty_icon.pos
    EASY_DIFFICULTY_ICON_SELECT.pos = easy_difficulty_icon.pos
    EASY_DIFFICULTY_ICON_DEFAULT.pos = easy_difficulty_icon.pos
    MEDIUM_DIFFICULTY_ICON_HOVER.pos = medium_difficulty_icon.pos
    MEDIUM_DIFFICULTY_ICON_SELECT.pos = medium_difficulty_icon.pos
    MEDIUM_DIFFICULTY_ICON_DEFAULT.pos = medium_difficulty_icon.pos
    HARD_DIFFICULTY_ICON_HOVER.pos = hard_difficulty_icon.pos
    HARD_DIFFICULTY_ICON_SELECT.pos = hard_difficulty_icon.pos
    HARD_DIFFICULTY_ICON_DEFAULT.pos = hard_difficulty_icon.pos
    GAME_START_BUTTON_DEFAULT.pos = game_start_button.pos
    GAME_START_BUTTON_HOVER.pos = game_start_button.pos
    GAME_START_BUTTON_UNSELECTABLE.pos = game_start_button.pos
    DROP_DOWN_BUTTON_UP_DEFAULT.pos = drop_down_button.pos
    DROP_DOWN_BUTTON_UP_HOVER.pos = drop_down_button.pos 
    DROP_DOWN_BUTTON_DOWN_DEFAULT.pos = drop_down_button.pos
    DROP_DOWN_BUTTON_DOWN_HOVER.pos = drop_down_button.pos
    GAME_BAR_SWITCHER_LEFT.pos = game_bar_switcher.pos
    GAME_BAR_SWITCHER_RIGHT.pos = game_bar_switcher.pos
    if difficulty == 1:
        current_difficulty_display = EASY_DIFFICULTY_DISPLAY
        easy_difficulty_icon = EASY_DIFFICULTY_ICON_SELECT
    elif difficulty == 2:
        current_difficulty_display = MEDIUM_DIFFICULTY_DISPLAY
        medium_difficulty_icon = MEDIUM_DIFFICULTY_ICON_SELECT
    elif difficulty == 3:
        current_difficulty_display = HARD_DIFFICULTY_DISPLAY
        hard_difficulty_icon = HARD_DIFFICULTY_ICON_SELECT
    if game_bar_state == 1:
        game_bar_switcher = GAME_BAR_SWITCHER_RIGHT
    else:
        game_bar_switcher = GAME_BAR_SWITCHER_LEFT


def prepare_game():
    global FULL_MENU
    global game_start, current_screen, SCREEN_X
    current_screen = 3
    
    

def on_mouse_move(pos):
    global debug
    global back_from_credits, play_button
    global credits_button, debug_button, back_from_play
    global difficulty, easy_difficulty_icon
    global medium_difficulty_icon, hard_difficulty_icon
    global game_start_button, drop_down_button
    if game_start == False:
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
                    print("hover debug buton")
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
                easy_difficulty_icon = EASY_DIFFICULTY_ICON_HOVER
            elif difficulty != 1:
                easy_difficulty_icon = EASY_DIFFICULTY_ICON_DEFAULT
            if (
                pos[0] >= medium_difficulty_icon_area[0] and
                pos[0] <= medium_difficulty_icon_area[1] and
                pos[1] >= medium_difficulty_icon_area[2] and
                pos[1] <= medium_difficulty_icon_area[3] and
                difficulty != 2
                ):
                if debug == True:
                    print("medium difficulty")
                medium_difficulty_icon = MEDIUM_DIFFICULTY_ICON_HOVER
            elif difficulty != 2:
                medium_difficulty_icon = MEDIUM_DIFFICULTY_ICON_DEFAULT
            if (
                pos[0] >= hard_difficulty_icon_area[0] and
                pos[0] <= hard_difficulty_icon_area[1] and
                pos[1] >= hard_difficulty_icon_area[2] and
                pos[1] <= hard_difficulty_icon_area[3] and
                difficulty != 3
                ):
                if debug == True:
                    print("hard difficulty")
                hard_difficulty_icon = HARD_DIFFICULTY_ICON_HOVER
            elif difficulty != 3:
                hard_difficulty_icon = HARD_DIFFICULTY_ICON_DEFAULT
            if difficulty != 0:
                if (
                    pos[0] >= game_start_button_area[0] and
                    pos[0] <= game_start_button_area[1] and
                    pos[1] >= game_start_button_area[2] and
                    pos[1] <= game_start_button_area[3]
                    ):
                    if debug:
                        print("Hovering start button")
                    game_start_button = GAME_START_BUTTON_HOVER
                else:
                    game_start_button = GAME_START_BUTTON_DEFAULT
        if current_screen == 3:
            if (
                    pos[0] >= drop_down_button_area[0] and
                    pos[0] <= drop_down_button_area[1] and
                    pos[1] >= drop_down_button_area[2] and
                    pos[1] <= drop_down_button_area[3]
                    ):
                if drop_down_state == 1: # hidden, so the button faces down
                    drop_down_button = DROP_DOWN_BUTTON_DOWN_HOVER
                else:
                    drop_down_button = DROP_DOWN_BUTTON_UP_HOVER
            else:
                if drop_down_state == 1:
                    drop_down_button = DROP_DOWN_BUTTON_DOWN_DEFAULT
                else:
                    drop_down_button = DROP_DOWN_BUTTON_UP_DEFAULT


def on_mouse_down(pos, button):
    global debug, debug_button
    global current_screen, difficulty
    global easy_difficulty_icon, medium_difficulty_icon
    global hard_difficulty_icon, drop_down_state, game_bar_state
    if game_start == False:
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
                    pos[1] <= easy_difficulty_icon_area[3] and
                    mouse.LEFT == button
                    ):
                    if debug == True:
                        print("easy difficulty pressed")
                    easy_difficulty_icon = EASY_DIFFICULTY_ICON_SELECT
                    difficulty = 1
            if difficulty != 2:
                if (
                    pos[0] >= medium_difficulty_icon_area[0] and
                    pos[0] <= medium_difficulty_icon_area[1] and
                    pos[1] >= medium_difficulty_icon_area[2] and
                    pos[1] <= medium_difficulty_icon_area[3] and
                    mouse.LEFT == button
                    ):
                    if debug == True:
                        print("medium difficulty pressed")
                    medium_difficulty_icon = MEDIUM_DIFFICULTY_ICON_SELECT
                    difficulty = 2
            if difficulty != 3:
                if (
                    pos[0] >= hard_difficulty_icon_area[0] and
                    pos[0] <= hard_difficulty_icon_area[1] and
                    pos[1] >= hard_difficulty_icon_area[2] and
                    pos[1] <= hard_difficulty_icon_area[3] and
                    mouse.LEFT == button
                    ):
                    if debug == True:
                        print("hard difficulty pressed")
                    hard_difficulty_icon = HARD_DIFFICULTY_ICON_SELECT
                    difficulty = 3
            if difficulty != 0:
                if (
                    pos[0] >= game_start_button_area[0] and
                    pos[0] <= game_start_button_area[1] and
                    pos[1] >= game_start_button_area[2] and
                    pos[1] <= game_start_button_area[3] and
                    mouse.LEFT == button
                    ):
                    if debug:
                        print("starting game")
                    prepare_game()
        if current_screen == 3:
            if button == mouse.LEFT:
                if (
                    pos[0] >= drop_down_button_area[0] and
                    pos[0] <= drop_down_button_area[1] and
                    pos[1] >= drop_down_button_area[2] and
                    pos[1] <= drop_down_button_area[3]
                    ):
                    if drop_down_state == 0:
                        drop_down_state = 1
                    else:
                        drop_down_state = 0
                if (
                    pos[0] >= game_bar_switcher_area[0] and
                    pos[0] <= game_bar_switcher_area[1] and
                    pos[1] >= game_bar_switcher_area[2] and
                    pos[1] <= game_bar_switcher_area[3]
                    ):
                    if game_bar_state == 0:
                        game_bar_state = 1
                    else:
                        game_bar_state = 0


def draw(): # Draw all the
    FULL_MENU.draw()
    back_from_credits.draw()
    play_button.draw()
    credits_button.draw()
    debug_button.draw()
    back_from_play.draw()
    difficulty_display.draw()
    current_difficulty_display.draw()
    easy_difficulty_icon.draw()
    medium_difficulty_icon.draw()
    hard_difficulty_icon.draw()
    game_start_button.draw()
    game_bar.draw()
    drop_down_ui.draw()
    game_bar_switcher.draw()
    drop_down_button.draw()
    

pgzrun.go() # This must be at the end of the code for it to run
