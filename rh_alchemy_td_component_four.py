import pgzrun
import random
import math
"""
COMPONENT TWO UPDATING ON FEEDBACK

All images to be imported need to be to a scale of 3x
"""

WIDTH = 1080
HEIGHT = 540
game_started = 0

#This lets the screen move to designated points of each screen
SCREEN_X = [3240.0, 2160.0, 1080.0, -2160.0]

balance = 150000

# any time is done in frames
TOWERS_STATS = [
# Example:
# [tower image, base cost, base cooldown, current cooldown, projectile sprite]
["empty"],
["archer", 100, 75, 75, "archer_projectile"],
["wizard", 250, 45, 25, "wizard_projectile"],
["imp", 400, 25, 15, "imp_projectile"]
    ]

# variables to call for specific stats, which makes the code
# easier to read

EMPTY = 0
ARCHER = 1
WIZARD = 2
IMP = 3

TOWER_IMAGE = 0
TOWER_COST = 1
BASE_COOLDOWN = 2
CURRENT_COOLDOWN = 3
PROJECTILE_SPRITE = 4

MIN_SPAWN_Y = 490
MAX_SPAWN_Y = 520
PROJECTILE_SPEED = -35
ENEMY_SPEED = 15

# enemies

enemy_stats = [
# Example:
# [dropped cost, initial cooldown, base cooldown, sprite]
    [20, 5 * 60, 60, 0, "slime"],
    [60, 20 * 60, 300, 0, "zombie"],
    [45, 45 * 60, 30, 0, "enemy_imp"]
    ]


ENEMY_DROPPED_COST = 0
ENEMY_INITIAL_COOLDOWN = 1
ENEMY_BASE_COOLDOWN = 2
ENEMY_CURRENT_COOLDOWN = 3
ENEMY_SPRITE = 4

SLIME = 0
ZOMBIE = 1
ENEMY_IMP = 2

direction = 0

game_start = False

FULL_MENU = Actor("full_menu")
FULL_MENU.y = 270

spawned_enemies = []

spawned_projectiles = []

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

play_button = Actor("menu_play_text")
PLAY_BUTTON_DEFAULT = play_button
PLAY_BUTTON_HOVER = Actor("menu_play_text_hover")
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

credits_button = Actor("menu_credits_text")
CREDITS_BUTTON_DEFAULT = credits_button
CREDITS_BUTTON_HOVER = Actor("menu_credits_text_hover")
credits_button.x = MENU_BUTTON_X
credits_button.y = play_button.y + MENU_BUTTON_Y_DIFFERENCE
credits_button_area = [
    credits_button.x - (MENU_BUTTON_WIDTH / 2),
    credits_button.x + (MENU_BUTTON_WIDTH / 2),
    credits_button.y - (MENU_BUTTON_HEIGHT / 2),
    credits_button.y + (MENU_BUTTON_HEIGHT / 2)
]

debug_button = Actor("menu_debug_text_off")
DEBUG_BUTTON_ON = Actor("menu_debug_text_on")
DEBUG_BUTTON_OFF = debug_button
DEBUG_BUTTON_ON_HOVER = Actor("menu_debug_text_on_hover")
DEBUG_BUTTON_OFF_HOVER = Actor("menu_debug_text_off_hover")
debug_button.x = MENU_BUTTON_X
debug_button.y = credits_button.y + MENU_BUTTON_Y_DIFFERENCE
debug_button_area = [
    debug_button.x - (MENU_BUTTON_WIDTH / 2),
    debug_button.x + (MENU_BUTTON_WIDTH / 2),
    debug_button.y - (MENU_BUTTON_HEIGHT / 2),
    debug_button.y + (MENU_BUTTON_HEIGHT / 2)
]

back_from_credits = Actor("back_from_credits")
BACK_FROM_CREDITS_DEFAULT = back_from_credits
BACK_FROM_CREDITS_HOVER = Actor("back_from_credits_hover")
back_from_credits.x = -85
back_from_credits.y = 85
back_from_credits_area = [
    back_from_credits.x - (UI_BUTTON_SIDE / 2),
    back_from_credits.x + (UI_BUTTON_SIDE / 2),
    back_from_credits.y - (UI_BUTTON_SIDE / 2),
    back_from_credits.y + (UI_BUTTON_SIDE / 2)
]

back_from_play = Actor("back_from_play")
BACK_FROM_PLAY_DEFAULT = back_from_play
BACK_FROM_PLAY_HOVER = Actor("back_from_play_hover")
back_from_play.x = 2075
back_from_play.y = 85
back_from_play_area = [
    back_from_play.x - (UI_BUTTON_SIDE / 2),
    back_from_play.x + (UI_BUTTON_SIDE / 2),
    back_from_play.y - (UI_BUTTON_SIDE / 2),
    back_from_play.y + (UI_BUTTON_SIDE / 2)
]

difficulty_display = Actor("difficulty_display")
difficulty_display.x = 1360
difficulty_display.y = 495

NO_DIFFICULTY_DISPLAY = Actor("difficulty_display_none")
EASY_DIFFICULTY_DISPLAY = Actor("difficulty_display_easy")
MEDIUM_DIFFICULTY_DISPLAY = Actor("difficulty_display_medium")
HARD_DIFFICULTY_DISPLAY = Actor("difficulty_display_hard")
current_difficulty_display = NO_DIFFICULTY_DISPLAY
current_difficulty_display.x = 1780
current_difficulty_display.y = 495

EASY_DIFFICULTY_ICON_DEFAULT = Actor("difficulty_easy_icon")
EASY_DIFFICULTY_ICON_HOVER = Actor("difficulty_easy_icon_hover")
EASY_DIFFICULTY_ICON_SELECT = Actor("difficulty_easy_icon_select")
easy_difficulty_icon = EASY_DIFFICULTY_ICON_DEFAULT
easy_difficulty_icon.x = 1220
easy_difficulty_icon.y = 360
easy_difficulty_icon_area = [
    easy_difficulty_icon.x - (DIFFICULTY_ICON_WIDTH / 2),
    easy_difficulty_icon.x + (DIFFICULTY_ICON_WIDTH / 2),
    easy_difficulty_icon.y - (DIFFICULTY_ICON_HEIGHT / 2),
    easy_difficulty_icon.y + (DIFFICULTY_ICON_HEIGHT / 2)
    ]

MEDIUM_DIFFICULTY_ICON_DEFAULT = Actor("difficulty_medium_icon")
MEDIUM_DIFFICULTY_ICON_HOVER = Actor("difficulty_medium_icon_hover")
MEDIUM_DIFFICULTY_ICON_SELECT = Actor("difficulty_medium_icon_select")
medium_difficulty_icon = MEDIUM_DIFFICULTY_ICON_DEFAULT
medium_difficulty_icon.x = 1660
medium_difficulty_icon.y = 270
medium_difficulty_icon_area = [
    medium_difficulty_icon.x - (DIFFICULTY_ICON_WIDTH / 2),
    medium_difficulty_icon.x + (DIFFICULTY_ICON_WIDTH / 2),
    medium_difficulty_icon.y - (DIFFICULTY_ICON_HEIGHT / 2),
    medium_difficulty_icon.y + (DIFFICULTY_ICON_HEIGHT / 2)
    ]

HARD_DIFFICULTY_ICON_DEFAULT = Actor("difficulty_hard_icon")
HARD_DIFFICULTY_ICON_HOVER = Actor("difficulty_hard_icon_hover")
HARD_DIFFICULTY_ICON_SELECT = Actor("difficulty_hard_icon_select")
hard_difficulty_icon = HARD_DIFFICULTY_ICON_DEFAULT
hard_difficulty_icon.x = 1950
hard_difficulty_icon.y = 330
hard_difficulty_icon_area = [
    hard_difficulty_icon.x - (DIFFICULTY_ICON_WIDTH / 2),
    hard_difficulty_icon.x + (DIFFICULTY_ICON_WIDTH / 2),
    hard_difficulty_icon.y - (DIFFICULTY_ICON_HEIGHT / 2),
    hard_difficulty_icon.y + (DIFFICULTY_ICON_HEIGHT / 2)
    ]

GAME_START_BUTTON_DEFAULT = Actor("difficulty_start_text")
GAME_START_BUTTON_HOVER = Actor("difficulty_start_text_hover")
GAME_START_BUTTON_UNSELECTABLE = Actor("difficulty_start_text_unselectable")
game_start_button = GAME_START_BUTTON_UNSELECTABLE
game_start_button.x = 1810
game_start_button.y = 85
game_start_button_area = [
    game_start_button.x - (MENU_BUTTON_WIDTH / 2),
    game_start_button.x + (MENU_BUTTON_WIDTH / 2),
    game_start_button.y - (MENU_BUTTON_HEIGHT / 2),
    game_start_button.y + (MENU_BUTTON_HEIGHT / 2)
    ]

drop_down_ui = Actor("drop_down_ui")
DROP_DOWN_STATES = [270, -60]
drop_down_state = 1 # 0 being shown, 1 being hidden
drop_down_ui.x = 4860
drop_down_ui.y = DROP_DOWN_STATES[drop_down_state]

DROP_DOWN_BUTTON_UP_DEFAULT = Actor("button_up")
DROP_DOWN_BUTTON_UP_HOVER = Actor("button_up_selected")
DROP_DOWN_BUTTON_DOWN_DEFAULT = Actor("button_down")
DROP_DOWN_BUTTON_DOWN_HOVER = Actor("button_down_selected")
drop_down_button = DROP_DOWN_BUTTON_UP_DEFAULT
drop_down_button.x = drop_down_ui.x
drop_down_button.y = drop_down_ui.y + 120
drop_down_button_area = [
    drop_down_button.x - 48,
    drop_down_button.x + 48,
    drop_down_button.y - 48,
    drop_down_button.y + 48
    ]

# The unselect tower button can share it's main actor with the
# drop down button

tower_selected_state = 0
# 0 being no tower is selected, 1 being for a tower is selected.

UNSELECT_TOWER_BUTTON_DEFAULT = Actor("unselect_tower")
UNSELECT_TOWER_BUTTON_HOVER = Actor("unselect_tower_hover")

game_bar = Actor("game_bar")
GAME_BAR_STATES = [18, 1068]
game_bar_state = 0
game_bar.x = 4860
game_bar.y = drop_down_ui.y - 120

GAME_BAR_SWITCHER_LEFT = Actor("bar_switcher_left")
GAME_BAR_SWITCHER_RIGHT = Actor("bar_switcher_right")
game_bar_switcher = GAME_BAR_SWITCHER_LEFT
game_bar_switcher.x = 5240
game_bar_switcher.y = -60
game_bar_switcher_area = [
    game_bar_switcher.x - 96,
    game_bar_switcher.x + 96,
    game_bar_switcher.y - 48,
    game_bar_switcher.y + 48
    ]

# tower buttons

TOWER_BUTTON_HEIGHT = 54 * 3
TOWER_BUTTON_WIDTH = 80 * 3

ARCHER_BUTTON_DEFAULT = Actor("archer_tower_button")
ARCHER_BUTTON_HOVER = Actor("archer_tower_button_hover")
ARCHER_BUTTON_UNSELECTABLE = Actor("archer_tower_button_unselectable")
archer_button = ARCHER_BUTTON_DEFAULT
archer_button_area = [
    archer_button.x - (TOWER_BUTTON_WIDTH / 2),
    archer_button.x + (TOWER_BUTTON_WIDTH / 2),
    archer_button.y - (TOWER_BUTTON_HEIGHT / 2),
    archer_button.y + (TOWER_BUTTON_HEIGHT / 2)
    ]

WIZARD_BUTTON_DEFAULT = Actor("wizard_tower_button")
WIZARD_BUTTON_HOVER = Actor("wizard_tower_button_hover")
WIZARD_BUTTON_UNSELECTABLE = Actor("wizard_tower_button_unselectable")
wizard_button = WIZARD_BUTTON_DEFAULT
wizard_button_area = [
    wizard_button.x - (TOWER_BUTTON_WIDTH / 2),
    wizard_button.x + (TOWER_BUTTON_WIDTH / 2),
    wizard_button.y - (TOWER_BUTTON_HEIGHT / 2),
    wizard_button.y + (TOWER_BUTTON_HEIGHT / 2)
    ]

IMP_BUTTON_DEFAULT = Actor("imp_tower_button")
IMP_BUTTON_HOVER = Actor("imp_tower_button_hover")
IMP_BUTTON_UNSELECTABLE = Actor("imp_tower_button_unselectable")
imp_button = IMP_BUTTON_DEFAULT
imp_button_area = [
    imp_button.x - (TOWER_BUTTON_WIDTH / 2),
    imp_button.x + (TOWER_BUTTON_WIDTH / 2),
    imp_button.y - (TOWER_BUTTON_HEIGHT / 2),
    imp_button.y + (TOWER_BUTTON_HEIGHT / 2)
    ]

# towers

TOWER_SLOT_SIDE_LENGTH = 56 * 3

TOWER_SLOT_ONE_EMPTY = Actor("tower_empty")
TOWER_SLOT_ONE_ARCHER_LEFT = Actor("tower_archer_left")
TOWER_SLOT_ONE_WIZARD_LEFT = Actor("tower_wizard_left")
TOWER_SLOT_ONE_IMP_LEFT = Actor("tower_imp_left")
tower_slot_one = TOWER_SLOT_ONE_EMPTY
tower_slot_one.x = 4500
tower_slot_one.y = 390
tower_slot_one_occupied = False
tower_slot_one_area = [
    tower_slot_one.x - (TOWER_SLOT_SIDE_LENGTH / 2),
    tower_slot_one.x + (TOWER_SLOT_SIDE_LENGTH / 2),
    tower_slot_one.y - (TOWER_SLOT_SIDE_LENGTH / 2),
    tower_slot_one.y + (TOWER_SLOT_SIDE_LENGTH / 2)
    ]
tower_slot_one_stats = []

TOWER_SLOT_TWO_EMPTY = Actor("tower_empty")
TOWER_SLOT_TWO_ARCHER_LEFT = Actor("tower_archer_left")
TOWER_SLOT_TWO_WIZARD_LEFT = Actor("tower_wizard_left")
TOWER_SLOT_TWO_IMP_LEFT = Actor("tower_imp_left")
tower_slot_two = TOWER_SLOT_TWO_EMPTY
tower_slot_two.x = 4860
tower_slot_two.y = 320
tower_slot_two_occupied = False
tower_slot_two_area = [
    tower_slot_two.x - (TOWER_SLOT_SIDE_LENGTH / 2),
    tower_slot_two.x + (TOWER_SLOT_SIDE_LENGTH / 2),
    tower_slot_two.y - (TOWER_SLOT_SIDE_LENGTH / 2),
    tower_slot_two.y + (TOWER_SLOT_SIDE_LENGTH / 2)
    ]
tower_slot_two_stats = []

TOWER_SLOT_THREE_EMPTY = Actor("tower_empty")
TOWER_SLOT_THREE_ARCHER_LEFT = Actor("tower_archer_left")
TOWER_SLOT_THREE_WIZARD_LEFT = Actor("tower_wizard_left")
TOWER_SLOT_THREE_IMP_LEFT = Actor("tower_imp_left")
tower_slot_three = TOWER_SLOT_THREE_EMPTY
tower_slot_three.x = 5220
tower_slot_three.y = 360
tower_slot_three_occupied = False
tower_slot_three_area = [
    tower_slot_three.x - (TOWER_SLOT_SIDE_LENGTH / 2),
    tower_slot_three.x + (TOWER_SLOT_SIDE_LENGTH / 2),
    tower_slot_three.y - (TOWER_SLOT_SIDE_LENGTH / 2),
    tower_slot_three.y + (TOWER_SLOT_SIDE_LENGTH / 2)
    ]
tower_slot_three_stats = []

# game ui

CURRENT_TOWERS = [Actor(TOWERS_STATS[EMPTY][TOWER_IMAGE]),
                  Actor(TOWERS_STATS[ARCHER][TOWER_IMAGE]),
                  Actor(TOWERS_STATS[WIZARD][TOWER_IMAGE]),
                  Actor(TOWERS_STATS[IMP][TOWER_IMAGE])]
current_tower_value = 0
current_tower = CURRENT_TOWERS[current_tower_value]

balance_icon = Actor("balance_icon")
balance_icon.x = 5400
balance_icon.y = drop_down_button.y
selected_tower = 0

START_GAME_BUTTON_DEFAULT = Actor("start_game")
START_GAME_BUTTON_HOVER = Actor("start_game_hover")
START_GAME_BUTTON_HIDDEN = Actor("empty")
start_game_button = START_GAME_BUTTON_DEFAULT
start_game_button.x = 4400
start_game_button.y = 230
start_game_button_area = [
    start_game_button.x - (UI_BUTTON_SIDE / 2),
    start_game_button.x + (UI_BUTTON_SIDE / 2),
    start_game_button.y - (UI_BUTTON_SIDE / 2),
    start_game_button.y + (UI_BUTTON_SIDE / 2)
    ]

# ability to select a tower and sell it

SELL_SELECT_DEFAULT = Actor("tower_select")
SELL_SELECT_HIDDEN = Actor("empty")
sell_select = SELL_SELECT_HIDDEN
sell_select.x = 0
sell_select.y = 0
sell_select_area = [
    sell_select.x - (UI_BUTTON_SIDE / 2),
    sell_select.x + (UI_BUTTON_SIDE / 2),
    sell_select.y - (30 * 3) - (UI_BUTTON_SIDE / 2),
    sell_select.y - (30 * 3) + (UI_BUTTON_SIDE / 2),
    ]
cancel_area = [
    sell_select.x - 18,
    sell_select.x + 18,
    sell_select.y - 18,
    sell_select.y + 18
    ]
selling_tower_selected = False
selling_tower_selected_number = 0
# 0 being hidden, 1 being shown

# number values for difficulties being, in order:
# none, easy, medium and hard
difficulty = 0

current_screen = 1
FULL_MENU.x = SCREEN_X[current_screen]
debug = False

#
# Seperate between functions and variables
#

def move_all(movement, direction):
    # To move all the buttons and the screen at the same time
    global FULL_MENU
    global back_from_credits
    global play_button, credits_button, debug_button
    global back_from_play, difficulty_display, current_difficulty_display
    global easy_difficulty_icon, medium_difficulty_icon, hard_difficulty_icon
    global game_start_button, game_bar
    global drop_down_ui, drop_down_button
    global tower_slot_one, tower_slot_two, tower_slot_three
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
    tower_slot_one.x += movement * direction
    tower_slot_two.x += movement * direction
    tower_slot_three.x += movement * direction
    start_game_button.x += movement * direction


def spawn(actor_name, from_player:
    global spawned_enemies, spawned_projectiles
    spawn = Actor(actor_name)
    spawn.y = random.randint(MIN_SPAWN_Y, MAX_SPAWN_Y)
    if from_player:
        spawn.x = 1112
        spawned_projectiles.append(spawn)
    else:
        spawn.x = -32
        spawned_enemies.append(spawn)
    


def tick():
    global enemy_stats
    global TOWERS_TOWERS_STATS
    if tower_slot_one_occupied:
        if tower_slot_one_stats[CURRENT_COOLDOWN] != 0:
            tower_slot_one_stats[CURRENT_COOLDOWN] -= 1
        else:
            spawn(tower_slot_one_stats[PROJECTILE_SPRITE], True)
            tower_slot_one_stats[CURRENT_COOLDOWN] = tower_slot_one_stats[BASE_COOLDOWN]
    if tower_slot_two_occupied:
        if tower_slot_two_stats[CURRENT_COOLDOWN] != 0:
            tower_slot_two_stats[CURRENT_COOLDOWN] -= 1
        else:
            spawn(tower_slot_two_stats[PROJECTILE_SPRITE], True)
            tower_slot_two_stats[CURRENT_COOLDOWN] = tower_slot_two_stats[BASE_COOLDOWN]
    if tower_slot_three_occupied:
        if tower_slot_three_stats[CURRENT_COOLDOWN] != 0:
            tower_slot_three_stats[CURRENT_COOLDOWN] -= 1
        else:
            spawn(tower_slot_three_stats[PROJECTILE_SPRITE], True)
            tower_slot_three_stats[CURRENT_COOLDOWN] = tower_slot_three_stats[BASE_COOLDOWN]
    for enemy_stat in enemy_stats:
        if enemy_stat[ENEMY_INITIAL_COOLDOWN] != 0:
            enemy_stat[ENEMY_INITIAL_COOLDOWN] -= 1
        elif enemy_stat[ENEMY_CURRENT_COOLDOWN] != 0:
            enemy_stat[ENEMY_CURRENT_COOLDOWN] -= 1
        elif enemy_stat[ENEMY_CURRENT_COOLDOWN] == 0:
            enemy_stat[ENEMY_CURRENT_COOLDOWN] = enemy_stat[ENEMY_BASE_COOLDOWN]
            spawn(enemy_stat[ENEMY_SPRITE], False)


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
    global archer_button, wizard_button, imp_button
    global archer_button_area, wizard_button_area, imp_button_area
    global cancel_tower_button, cancel_tower_button_area
    global tower_slot_one_area, tower_slot_two_area, tower_slot_three_area
    global sell_select_area, cancel_area, start_game_button_area
    global start_game_button, spawned_projectiles, spawned_enemies
    # The following three "if" statements make it so the following
    # move smoothly:
    # menu screen, 
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
    # The following redefine the areas, so as the screen moves
    # the hitboxes for the areas move alongside them
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
    archer_button.x = game_bar.x + 160
    archer_button.y = game_bar.y
    wizard_button.x = archer_button.x + 360
    wizard_button.y = game_bar.y
    imp_button.x = wizard_button.x + 360
    imp_button.y = game_bar.y
    archer_button_area = [
        archer_button.x - (TOWER_BUTTON_WIDTH / 2),
        archer_button.x + (TOWER_BUTTON_WIDTH / 2),
        archer_button.y - (TOWER_BUTTON_HEIGHT / 2),
        archer_button.y + (TOWER_BUTTON_HEIGHT / 2)
        ]
    wizard_button_area = [
        wizard_button.x - (TOWER_BUTTON_WIDTH / 2),
        wizard_button.x + (TOWER_BUTTON_WIDTH / 2),
        wizard_button.y - (TOWER_BUTTON_HEIGHT / 2),
        wizard_button.y + (TOWER_BUTTON_HEIGHT / 2)
        ]
    imp_button_area = [
        imp_button.x - (TOWER_BUTTON_WIDTH / 2),
        imp_button.x + (TOWER_BUTTON_WIDTH / 2),
        imp_button.y - (TOWER_BUTTON_HEIGHT / 2),
        imp_button.y + (TOWER_BUTTON_HEIGHT / 2)
        ]
    tower_slot_one_area = [
        tower_slot_one.x - (TOWER_SLOT_SIDE_LENGTH / 2),
        tower_slot_one.x + (TOWER_SLOT_SIDE_LENGTH / 2),
        tower_slot_one.y - (TOWER_SLOT_SIDE_LENGTH / 2),
        tower_slot_one.y + (TOWER_SLOT_SIDE_LENGTH / 2)
    ]
    tower_slot_two_area = [
        tower_slot_two.x - (TOWER_SLOT_SIDE_LENGTH / 2),
        tower_slot_two.x + (TOWER_SLOT_SIDE_LENGTH / 2),
        tower_slot_two.y - (TOWER_SLOT_SIDE_LENGTH / 2),
        tower_slot_two.y + (TOWER_SLOT_SIDE_LENGTH / 2)
    ]
    tower_slot_three_area = [
        tower_slot_three.x - (TOWER_SLOT_SIDE_LENGTH / 2),
        tower_slot_three.x + (TOWER_SLOT_SIDE_LENGTH / 2),
        tower_slot_three.y - (TOWER_SLOT_SIDE_LENGTH / 2),
        tower_slot_three.y + (TOWER_SLOT_SIDE_LENGTH / 2)
    ]
    sell_select_area = [
        sell_select.x - (UI_BUTTON_SIDE / 2),
        sell_select.x + (UI_BUTTON_SIDE / 2),
        sell_select.y - (30 * 3) - (UI_BUTTON_SIDE / 2),
        sell_select.y - (30 * 3) + (UI_BUTTON_SIDE / 2),
    ]
    cancel_area = [
        sell_select.x - 18,
        sell_select.x + 18,
        sell_select.y - 18,
        sell_select.y + 18
    ]
    start_game_button_area = [
        start_game_button.x - (UI_BUTTON_SIDE / 2),
        start_game_button.x + (UI_BUTTON_SIDE / 2),
        start_game_button.y - (UI_BUTTON_SIDE / 2),
        start_game_button.y + (UI_BUTTON_SIDE / 2)
    ]
    # The states share a seperate position as to the main actor
    # they're based off of. The following apply to keep them in the
    # same area.
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
    ARCHER_BUTTON_DEFAULT.pos = archer_button.pos
    ARCHER_BUTTON_HOVER.pos = archer_button.pos
    ARCHER_BUTTON_UNSELECTABLE.pos = archer_button.pos
    WIZARD_BUTTON_DEFAULT.pos = wizard_button.pos
    WIZARD_BUTTON_HOVER.pos = wizard_button.pos
    WIZARD_BUTTON_UNSELECTABLE.pos = wizard_button.pos
    IMP_BUTTON_DEFAULT.pos = imp_button.pos
    IMP_BUTTON_HOVER.pos = imp_button.pos
    IMP_BUTTON_UNSELECTABLE.pos = imp_button.pos
    UNSELECT_TOWER_BUTTON_DEFAULT.pos = drop_down_button.pos
    UNSELECT_TOWER_BUTTON_HOVER.pos = drop_down_button.pos
    TOWER_SLOT_ONE_EMPTY.pos = tower_slot_one.pos
    TOWER_SLOT_ONE_ARCHER_LEFT.pos = tower_slot_one.pos
    TOWER_SLOT_ONE_WIZARD_LEFT.pos = tower_slot_one.pos
    TOWER_SLOT_ONE_IMP_LEFT.pos = tower_slot_one.pos
    TOWER_SLOT_TWO_EMPTY.pos = tower_slot_two.pos
    TOWER_SLOT_TWO_ARCHER_LEFT.pos = tower_slot_two.pos
    TOWER_SLOT_TWO_WIZARD_LEFT.pos = tower_slot_two.pos
    TOWER_SLOT_TWO_IMP_LEFT.pos = tower_slot_two.pos
    TOWER_SLOT_THREE_EMPTY.pos = tower_slot_three.pos
    TOWER_SLOT_THREE_ARCHER_LEFT.pos = tower_slot_three.pos
    TOWER_SLOT_THREE_WIZARD_LEFT.pos = tower_slot_three.pos
    TOWER_SLOT_THREE_IMP_LEFT.pos = tower_slot_three.pos
    START_GAME_BUTTON_DEFAULT.pos = start_game_button.pos
    START_GAME_BUTTON_HOVER.pos = start_game_button.pos
    START_GAME_BUTTON_HIDDEN.pos = start_game_button.pos
    # The following help keep certain actors to the specific sprite
    # they need to be.
    if difficulty == 1:
        current_difficulty_display = EASY_DIFFICULTY_DISPLAY
        easy_difficulty_icon = EASY_DIFFICULTY_ICON_SELECT
    elif difficulty == 2:
        current_difficulty_display = MEDIUM_DIFFICULTY_DISPLAY
        medium_difficulty_icon = MEDIUM_DIFFICULTY_ICON_SELECT
    elif difficulty == 3:
        current_difficulty_display = HARD_DIFFICULTY_DISPLAY
        hard_difficulty_icon = HARD_DIFFICULTY_ICON_SELECT
    if game_bar_state == 0:
        game_bar_switcher = GAME_BAR_SWITCHER_RIGHT
    else:
        game_bar_switcher = GAME_BAR_SWITCHER_LEFT

    # tower firing functions - component four
    
    if game_started == 1:
        if start_game_button != START_GAME_BUTTON_HIDDEN:
            start_game_button = START_GAME_BUTTON_HIDDEN
        tick()
        for projectile in spawned_projectiles:
            projectile.x += PROJECTILE_SPEED
            enemy_index = projectile.collidelist(spawned_enemies)
            if enemy_index != -1:
                del spawned_enemies[enemy_index]
                spawned_projectiles.remove(projectile)
            if projectile.x < -32:
                spawned_projectiles.remove(projectile)

        for enemy in spawned_enemies:
            enemy.x += ENEMY_SPEED
            


def prepare_game():
    global current_screen
    current_screen = 3

def start_game():
    global game_started
    global difficulty
    if difficulty == 1:
        multiplier = 1
    elif difficulty == 2:
        multiplier = 1.4
    else:
        multiplier = 1.8
    for enemy_stat in enemy_stats:
        enemy_stat[ENEMY_DROPPED_COST] * multiplier
        enemy_stat[ENEMY_INITIAL_COOLDOWN] / multiplier
        enemy_stat[ENEMY_BASE_COOLDOWN] / multiplier
    game_started = 1
    

def on_mouse_move(pos):
    global debug
    global back_from_credits, play_button
    global credits_button, debug_button, back_from_play
    global difficulty, easy_difficulty_icon
    global medium_difficulty_icon, hard_difficulty_icon
    global game_start_button, drop_down_button, tower_selected_state
    global archer_button, wizard_button, imp_button, sell_select_area
    global start_game_button
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
            for tower_actor in CURRENT_TOWERS:
                tower_actor.pos = pos
            if (
                pos[0] >= drop_down_button_area[0] and
                pos[0] <= drop_down_button_area[1] and
                pos[1] >= drop_down_button_area[2] and
                pos[1] <= drop_down_button_area[3]
                ):
                if tower_selected_state == 0:
                    if drop_down_state == 1: # hidden, so the button faces down
                        drop_down_button = DROP_DOWN_BUTTON_DOWN_HOVER
                    else:
                        drop_down_button = DROP_DOWN_BUTTON_UP_HOVER
                else:
                    drop_down_button = UNSELECT_TOWER_BUTTON_HOVER
            else:
                if tower_selected_state == 0:
                    if drop_down_state == 1:
                        drop_down_button = DROP_DOWN_BUTTON_DOWN_DEFAULT
                    else:
                        drop_down_button = DROP_DOWN_BUTTON_UP_DEFAULT
                else:
                    drop_down_button = UNSELECT_TOWER_BUTTON_DEFAULT
            if balance >= TOWERS_STATS[ARCHER][TOWER_COST]:
                if (
                    pos[0] >= archer_button_area[0] and
                    pos[0] <= archer_button_area[1] and
                    pos[1] >= archer_button_area[2] and
                    pos[1] <= archer_button_area[3]
                    ):
                    archer_button = ARCHER_BUTTON_HOVER
                else:
                    archer_button = ARCHER_BUTTON_DEFAULT
            else:
                archer_button = ARCHER_BUTTON_UNSELECTABLE
            if balance >= TOWERS_STATS[WIZARD][TOWER_COST]:
                if (
                    pos[0] >= wizard_button_area[0] and
                    pos[0] <= wizard_button_area[1] and
                    pos[1] >= wizard_button_area[2] and
                    pos[1] <= wizard_button_area[3]
                    ):
                    wizard_button = WIZARD_BUTTON_HOVER
                else:
                    wizard_button = WIZARD_BUTTON_DEFAULT
            else:
                wizard_button = WIZARD_BUTTON_UNSELECTABLE
            if balance >= TOWERS_STATS[IMP][TOWER_COST]:
                if (
                    pos[0] >= imp_button_area[0] and
                    pos[0] <= imp_button_area[1] and
                    pos[1] >= imp_button_area[2] and
                    pos[1] <= imp_button_area[3]
                    ):
                    imp_button = IMP_BUTTON_HOVER
                else:
                    imp_button = IMP_BUTTON_DEFAULT
            else:
                imp_button = IMP_BUTTON_UNSELECTABLE
            if (
                pos[0] >= start_game_button_area[0] and
                pos[0] <= start_game_button_area[1] and
                pos[1] >= start_game_button_area[2] and
                pos[1] <= start_game_button_area[3] and
                game_started != 1
                ):
                if debug:
                    print("hovered")
                start_game_button = START_GAME_BUTTON_HOVER
            else:
                if debug:
                    print("normal")
                start_game_button = START_GAME_BUTTON_DEFAULT
            
                
                

def select_tower(tower):
    global tower_selected_state, current_tower, drop_down_state
    global selected_tower
    current_tower = CURRENT_TOWERS[tower]
    drop_down_state = 1 #hidden
    tower_selected_state = 1
    selected_tower = tower


def place_tower(tower, slot):
    global tower_slot_one, tower_slot_two, tower_slot_three
    global tower_slot_one_stats, tower_slot_two_stats
    global tower_slot_three_stats, tower_selected_state
    global selected_tower, current_tower
    global tower_slot_one_occupied, tower_slot_two_occupied
    global tower_slot_three_occupied, selected_tower
    global balance
    for stat in TOWERS_STATS[tower]:
        if slot == 1:
            tower_slot_one_stats.append(stat)
            tower_slot_one_occupied = True
        elif slot == 2:
            tower_slot_two_stats.append(stat)
            tower_slot_two_occupied = True
        else:
            tower_slot_three_stats.append(stat)
            tower_slot_three_occupied = True
    if slot == 1:
        if selected_tower == 1:
            tower_slot_one = TOWER_SLOT_ONE_ARCHER_LEFT
        elif selected_tower == 2:
            tower_slot_one = TOWER_SLOT_ONE_WIZARD_LEFT
        else:
            tower_slot_one = TOWER_SLOT_ONE_IMP_LEFT
    elif slot == 2:
        if selected_tower == 1:
            tower_slot_two = TOWER_SLOT_TWO_ARCHER_LEFT
        elif selected_tower == 2:
            tower_slot_two = TOWER_SLOT_TWO_WIZARD_LEFT
        else:
            tower_slot_two = TOWER_SLOT_TWO_IMP_LEFT	
    else:
        if selected_tower == 1:
            tower_slot_three = TOWER_SLOT_THREE_ARCHER_LEFT
        elif selected_tower == 2:
            tower_slot_three = TOWER_SLOT_THREE_WIZARD_LEFT
        else:
            tower_slot_three = TOWER_SLOT_THREE_IMP_LEFT
    tower_selected_state = 0
    balance -= TOWERS_STATS[tower][TOWER_COST]
    selected_tower = 0
    current_tower = CURRENT_TOWERS[EMPTY]


def select_tower_to_sell(tower_actor, tower_slot):
    global tower_slot_one, tower_slot_two, tower_slot_three
    global tower_slot_one_stats, tower_slot_two_stats
    global tower_slot_three_stats, selling_tower_selected_number
    global sell_select, selling_tower_selected
    sell_select.pos = tower_actor.pos
    SELL_SELECT_DEFAULT.pos = tower_actor.pos
    sell_select = SELL_SELECT_DEFAULT
    selling_tower_selected = True
    selling_tower_selected_number = tower_slot
    

def cancel_sell():
    global tower_slot_one, tower_slot_two, tower_slot_three
    global tower_slot_one_stats, tower_slot_two_stats
    global tower_slot_three_stats, selling_tower_selected_number
    global sell_select, selling_tower_selected
    selling_tower_selected = False
    sell_select = SELL_SELECT_HIDDEN


def sell_tower(tower_slot):
    global tower_slot_one, tower_slot_two, tower_slot_three
    global tower_slot_one_stats, tower_slot_two_stats
    global tower_slot_three_stats, selling_tower_selected_number
    global sell_select, selling_tower_selected
    global balance
    global tower_slot_one_occupied, tower_slot_two_occupied
    global tower_slot_three_occupied
    cancel_sell()
    print(tower_slot)
    if tower_slot == 1:
        tower_slot_one = TOWER_SLOT_ONE_EMPTY
        tower_slot_one_occupied = False
        balance += tower_slot_one_stats[TOWER_COST]
        tower_slot_one_stats = []
    if tower_slot == 2:
        tower_slot_two = TOWER_SLOT_TWO_EMPTY
        tower_slot_two_occupied = False
        balance += tower_slot_two_stats[TOWER_COST]
        tower_slot_two_stats = []
    if tower_slot == 3:
        tower_slot_three = TOWER_SLOT_THREE_EMPTY
        tower_slot_three_occupied = False
        balance += tower_slot_three_stats[TOWER_COST]
        tower_slot_three_stats = []

    
def on_mouse_down(pos, button):
    global debug, debug_button
    global current_screen, difficulty
    global easy_difficulty_icon, medium_difficulty_icon
    global hard_difficulty_icon, drop_down_state, game_bar_state
    global current_tower, tower_selected_state
    global selling_tower_selected_number, start_game_button
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
                print(pos)
                if (
                    pos[0] >= drop_down_button_area[0] and
                    pos[0] <= drop_down_button_area[1] and
                    pos[1] >= drop_down_button_area[2] and
                    pos[1] <= drop_down_button_area[3]
                    ):
                    if tower_selected_state == 0:
                        if drop_down_state == 0:
                            drop_down_state = 1
                        else:
                            drop_down_state = 0
                    else:
                        current_tower = CURRENT_TOWERS[EMPTY]
                        tower_selected_state = 0
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
                if balance >= TOWERS_STATS[ARCHER][TOWER_COST]:
                    if (
                        pos[0] >= archer_button_area[0] and
                        pos[0] <= archer_button_area[1] and
                        pos[1] >= archer_button_area[2] and
                        pos[1] <= archer_button_area[3]
                        ):
                        select_tower(ARCHER)
                if balance >= TOWERS_STATS[WIZARD][TOWER_COST]:
                    if (
                        pos[0] >= wizard_button_area[0] and
                        pos[0] <= wizard_button_area[1] and
                        pos[1] >= wizard_button_area[2] and
                        pos[1] <= wizard_button_area[3]
                       ):
                        select_tower(WIZARD)
                if balance >= TOWERS_STATS[IMP][TOWER_COST]:
                    if (
                        pos[0] >= imp_button_area[0] and
                        pos[0] <= imp_button_area[1] and
                        pos[1] >= imp_button_area[2] and
                        pos[1] <= imp_button_area[3]
                        ):
                        select_tower(IMP)
                if tower_selected_state == 1:
                    if (
                        pos[0] >= tower_slot_one_area[0] and
                        pos[0] <= tower_slot_one_area[1] and
                        pos[1] >= tower_slot_one_area[2] and
                        pos[1] <= tower_slot_one_area[3] and
                        tower_slot_one_occupied == False
                        ):
                        place_tower(selected_tower, 1)
                    if (
                        pos[0] >= tower_slot_two_area[0] and
                        pos[0] <= tower_slot_two_area[1] and
                        pos[1] >= tower_slot_two_area[2] and
                        pos[1] <= tower_slot_two_area[3] and
                        tower_slot_two_occupied == False
                        ):
                        place_tower(selected_tower, 2)
                    if (
                        pos[0] >= tower_slot_three_area[0] and
                        pos[0] <= tower_slot_three_area[1] and
                        pos[1] >= tower_slot_three_area[2] and
                        pos[1] <= tower_slot_three_area[3] and
                        tower_slot_three_occupied == False
                        ):
                        place_tower(selected_tower, 3)
                if selling_tower_selected == False:
                    if (
                        pos[0] >= tower_slot_one_area[0] and
                        pos[0] <= tower_slot_one_area[1] and
                        pos[1] >= tower_slot_one_area[2] and
                        pos[1] <= tower_slot_one_area[3] and
                        tower_slot_one_occupied == True
                        ):
                        select_tower_to_sell(tower_slot_one, 1)
                    if (
                        pos[0] >= tower_slot_two_area[0] and
                        pos[0] <= tower_slot_two_area[1] and
                        pos[1] >= tower_slot_two_area[2] and
                        pos[1] <= tower_slot_two_area[3] and
                        tower_slot_two_occupied == True
                        ):
                        select_tower_to_sell(tower_slot_two, 2)
                    if (
                        pos[0] >= tower_slot_three_area[0] and
                        pos[0] <= tower_slot_three_area[1] and
                        pos[1] >= tower_slot_three_area[2] and
                        pos[1] <= tower_slot_three_area[3] and
                        tower_slot_three_occupied == True
                        ):
                        select_tower_to_sell(tower_slot_three, 3)
                else:
                    if (
                        pos[0] >= sell_select_area[0] and
                        pos[0] <= sell_select_area[1] and
                        pos[1] >= sell_select_area[2] and
                        pos[1] <= sell_select_area[3]
                        ):
                        sell_tower(selling_tower_selected_number)
                    if (
                        pos[0] >= cancel_area[0] and
                        pos[0] <= cancel_area[1] and
                        pos[1] >= cancel_area[2] and
                        pos[1] <= cancel_area[3]
                        ):
                        cancel_sell()
                if (
                    pos[0] >= start_game_button_area[0] and
                    pos[0] <= start_game_button_area[1] and
                    pos[1] >= start_game_button_area[2] and
                    pos[1] <= start_game_button_area[3] and
                    game_started != 1
                    ):
                    start_game()


def draw(): # Draw all the buttons/actors
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
    tower_slot_one.draw()
    tower_slot_two.draw()
    tower_slot_three.draw()
    start_game_button.draw()
    sell_select.draw()
    start_game_button.draw()
    game_bar.draw()
    archer_button.draw()
    wizard_button.draw()
    imp_button.draw()
    drop_down_ui.draw()
    game_bar_switcher.draw()
    drop_down_button.draw()
    current_tower.draw()
    for enemy in spawned_enemies:
        enemy.draw()
    for projectile in spawned_projectiles:
        projectile.draw()
    
    

pgzrun.go() # This must be at the end of the code for it to run
