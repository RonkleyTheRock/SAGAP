from ui import line, colorize, hp_bar, mp_bar
from ui import CYAN, BOLD

def player_action(character, enemies, party, items, knowledge):
    if character.get("class") == "Lancer":
        character["mp"] = min(
            character["max_mp"],
            character["mp"] + 3
        )
