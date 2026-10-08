from ui import line, colorize, hp_bar, mp_bar
from ui import CYAN, BOLD

def player_action(character, enemies, party, items, knowledge):
    if character.get("class") == "Lancer":
        character["mp"] = min(
            character["max_mp"],
            character["mp"] + 3
        )
def player_action(character, enemies, party, items, knowledge):
    if character.get("class") == "Lancer":
        character["mp"] = min(
            character["max_mp"],
            character["mp"] + 3
        )

    while True:
        line()

        print(
            f"{colorize(character['name'], CYAN + BOLD)}'s turn | "
            f"{character['class']} | "
            f"HP {hp_bar(character['hp'], character['max_hp'], 12)} "
            f"{character['hp']}/{character['max_hp']}  "
            f"MP {mp_bar(character['mp'], character['max_mp'], 12)} "
            f"{character['mp']}/{character['max_mp']}  "
            f"NP {character.get('np_gauge', 0)}/100"
        )
