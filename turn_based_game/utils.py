import sys
import time
import random
from colorama import Fore, Style, init

# Initialize colorama (works on Windows & macOS/Linux)
init(autoreset=True)

def slow_print(text, delay=0.03, color=None):
    """Prints text slowly for dramatic effect."""
    if color:
        sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(Style.RESET_ALL + "\n")

def draw_hp_bar(name, hp, max_hp):
    """Draws a colored HP bar for a player."""
    bar_length = 20
    filled_length = int(bar_length * hp / max_hp)
    empty_length = bar_length - filled_length

    # Color based on % HP
    hp_ratio = hp / max_hp
    if hp_ratio > 0.6:
        color = Fore.GREEN
    elif hp_ratio > 0.3:
        color = Fore.YELLOW
    else:
        color = Fore.RED

    bar = "█" * filled_length + "-" * empty_length
    print(f"{name} HP: {color}[{bar}] {hp}/{max_hp}{Style.RESET_ALL}")

def roll_chance(probability):
    """Returns True with the given probability (0.0 to 1.0)."""
    return random.random() < probability

def print_separator(char="-", length=30):
    """Prints a separator line."""
    print(char * length)
