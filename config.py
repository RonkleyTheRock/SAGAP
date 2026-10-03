import os

# Terminal Formatting
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"

def enable_ansi():
    if os.name == "nt":
        os.system("")

def colorize(text, color):
    return f"{color}{text}{RESET}"

def header(title, width=64, ch="="):
    print("\n" + ch * width)
    pad = max(0, (width - len(title) - 2) // 2)
    print(f"{ch * pad} {colorize(title, BOLD + YELLOW)} {ch * pad}")
    print(ch * width)

def pause():
    input("\nPress ENTER to continue...")

# Settings & Prototypes Limits
DIFFICULTIES = {
    "Easy": 0.85,
    "Normal": 1.15,
    "Hard": 1.75,
}

STAT_NAMES = ["ST", "EN", "MA", "LK", "AG"]

LEVELS = {
    1: {"name": "Level 1: Entrance Graveyard", "rooms": 3},
    2: {"name": "Level 2: River Bank", "rooms": 3},
    3: {"name": "Level 3: Yokai Trail", "rooms": 4},
    4: {"name": "Level 4: Bronze Hall", "rooms": 4},
    5: {"name": "Level 5: Mini-Boss Chamber", "rooms": 1},
}
