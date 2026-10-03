from config import enable_ansi, header, pause, DIFFICULTIES
from classes import create_character, choose_class
from dungeon import run_dungeon

def tutorial():
    header("TUTORIAL")
    print("Welcome to the SAGAP!")
    print("- You control 3 party members.")
    print("- Combat uses Turn Actions. Target enemy weaknesses to deal massive damage.")
    print("- There are NO shops, gold, or gear in this demo.")
    print("- Keep your party alive using 'Medicine' found in rooms.")
    print("- Progress through 4 levels to face the Level 5 Mini-Boss!")
    pause()

def select_difficulty():
    header("SELECT DIFFICULTY")
    print("1. Easy\n2. Normal\n3. Hard")
    while True:
        c = input("> ")
        if c == "1": return DIFFICULTIES["Easy"]
        if c == "2": return DIFFICULTIES["Normal"]
        if c == "3": return DIFFICULTIES["Hard"]
        print("Invalid choice.")

def start_prototype():
    diff = select_difficulty()
    
    header("PARTY CREATION")
    party = []
    siblings = ["Irety", "Iyanu", "Ayonikun"]
    
    for name in siblings:
        selected_class = choose_class(name)
        party.append(create_character(name, selected_class))
    
    # Prototype Inventory: Restricted strictly to Medicine
    items = {"Medicine": 3}
    
    print("\nStarting prototype dungeon run...")
    pause()
    
    run_dungeon(party, diff, items)

def main_menu():
    enable_ansi()
    while True:
        header("SAGAP - PROTOTYPE v0.1")
        print("1. Play Prototype\n2. Tutorial\n3. Exit")
        c = input("> ")
        if c == "1":
            start_prototype()
        elif c == "2":
            tutorial()
        elif c == "3":
            print("Exiting...")
            break

if __name__ == "__main__":
    main_menu()
