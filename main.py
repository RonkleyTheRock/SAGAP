from ui import enable_ansi, header, clear_screen, pause
from characters.character import make_party
from systems.inventory import create_inventory
from systems.dungeon import run_dungeon
from config import DIFFICULTIES

def tutorial():
    pages = [
        ("THE BASICS", [
            "SAGAP is a turn-based RPG about three siblings searching a labyrinth.",
            "Read each room carefully. You will encounter enemies, clues, items,",
            "riddles and story choices. Enter a number when a menu asks for one.",
            "The game clears the screen between scenes; press ENTER when prompted.",
        ]),
        ("COMBAT", [
            "Each living sibling gets a turn. Choose Attack, Skill, Item, Guard,",
            "Analyse or Escape when those options are available.",
            "Analyse records what you learn about an enemy's affinities.",
            "Weakness hits can grant an extra action; resisted hits waste actions.",
            "Guard reduces incoming damage. Boss encounters cannot be escaped.",
        ]),
        ("SKILLS AND ITEMS", [
            "Skills spend MP unless their description says otherwise. Check the",
            "skill's affinity, target and cost before choosing it.",
            "Items are shared by the party. Select an item, then a valid target.",
            "Medicine restores HP; Ether restores MP; Panacea removes statuses;",
            "Revival Bead revives a fallen ally; Smoke Bomb improves escape chances.",
        ]),
        ("CLASSES AND LEVELS", [
            "Irety chooses a starting Class. Iyanu starts as a Caster and Ayonikun",
            "starts as a Lancer. Classes determine stats and available skills.",
            "Victories award XP and gold. When a character levels up, choose a stat",
            "to improve. HP and MP maximums also rise, and new skills unlock by level.",
            "Reaching level 7 can master a Class and preserve its inherited skill.",
        ]),
        ("BONDS AND THE GOAL", [
            "Talk to your siblings during exploration. Your responses affect bond",
            "scores, which are shown in the Social Bonds screen.",
            "Your goal is to reach the tenth floor, learn what happened to your",
            "mother, and confront the truth waiting in the deepest shrine.",
            "There are ten floors and nine floor guardians before the final battle.",
        ]),
    ]
    for title, lines in pages:
        clear_screen()
        header("HOW TO PLAY — " + title)
        for line in lines:
            print(line)
        pause()

def select_difficulty():
    while True:
        clear_screen()
        header("SELECT DIFFICULTY")
        print("1. Easy — more forgiving combat")
        print("2. Normal — intended balance")
        print("3. Hard — dangerous enemies")
        choice = input("> ").strip()
        if choice == "1":
            return DIFFICULTIES["Easy"]
        if choice == "2":
            return DIFFICULTIES["Normal"]
        if choice == "3":
            return DIFFICULTIES["Hard"]
        print("Invalid choice.")
        pause()

def opening_story():
    pages = [
        ("THE DISAPPEARANCE", [
            "Their father died years ago. Their mother never accepted the finality",
            "of that loss. She began searching for a way to reach beyond death.",
            "Then she disappeared, leaving behind one destination: the labyrinth.",
        ]),
        ("", [
            "Irety has made herself the person who keeps everyone standing.",
            "Iyanu hides his sharp mind behind apologies and self-doubt.",
            "Ayonikun learns quickly, but fears the day she finally fails.",
            "They disagree about what their mother was trying to do, but none of",
            "them is willing to leave her to the labyrinth.",
        ]),
        ("THE GOAL", [
            "The labyrinth is built from myths, memories and things people refuse",
            "to let go. Each floor holds clues about their mother's journey.",
            "Find her, discover why she descended, and face whatever remains of",
            "their father. The deeper they go, the less certain the truth becomes.",
        ]),
    ]
    for title, lines in pages:
        clear_screen()
        header(title)
        for line in lines:
            print(line)
        pause()

def start_game():
    difficulty = select_difficulty()
    clear_screen()
    header("PARTY CREATION")
    party = make_party()
    items = create_inventory()
    opening_story()
    run_dungeon(party, difficulty, items)

def main_menu():
    enable_ansi()
    while True:
        clear_screen()
        header("SAGAP — SUPER AWESOME GAME FOR AWESOME PEOPLE")
        print("1. Start Game")
        print("2. Tutorial")
        print("3. Exit")
        choice = input("> ").strip()
        if choice == "1":
            start_game()
        elif choice == "2":
            tutorial()
        elif choice == "3":
            clear_screen()
            print("Thank you for playing SAGAP.")
            break
        else:
            print("Invalid choice.")
            pause()

if __name__ == "__main__":
    main_menu()
