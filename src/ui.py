import os



RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
ITALIC = '\033[3m'

def enable_ansi():
    """Turns on ANSI escape support in older Windows terminals."""
    if os.name == "nt":
        os.system("")

def colorize(text, color):
    return f"{color}{text}{RESET}"

def bar(current, maximum, width=16, fill_color=GREEN):
    if maximum <= 0:
        maximum = 1

    filled = max(0, min (width, int (width * current / maximum)))

    return f"{fill_color}{'#' * filled}{DIM}{'.' * (width - filled)}{RESET}"

def hp_bar(current, maximum, width=16):
    ratio = current / maximum if maximum else 0
    color = GREEN if ratio > 0.5 else (YELLOW if ratio > 0.25 else RED)

    return bar(current, maximum, width, color)


def mp_bar(current, maximum, width=16):
    return bar(current, maximum, width, CYAN)


def header(title, width=64, ch="="):
    print("\n" + ch * width)

    pad = max(0, (width - len(title) - 2) // 2)

    print(f"{ch * pad} {colorize(title, BOLD + YELLOW)} {ch * pad}")
    print(ch * width)


def line():
    print(colorize("-" * 64, DIM))


def pause():
    input("\nPress ENTER to continue...")
