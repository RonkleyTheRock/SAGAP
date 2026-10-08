from ui import line, colorize, hp_bar, mp_bar
from ui import CYAN, BOLD

def player_action(character, enemies, party, items, knowledge):
    if character.get("class") == "Lancer":
        character["mp"] = min(
            character["max_mp"],
            character["mp"] + 3
        )
if __name__ == "__main__":
    character = {
        "class": "Lancer",
        "mp": 10,
        "max_mp": 30
    }

    player_action(
        character,
        [],
        [],
        {},
        {}
    )

    print("MP:", character["mp"])
