from ui import enable_ansi, header
from data.classes import CLASSES
from characters.character import create_character
from systems.dungeon import run_dungeon
from config import DIFFICULTIES


def pause():
    input("\nPress Enter to continue...")


def tutorial():
    header("TUTORIAL")
    print("You control three siblings in turn-based combat.")
    print("Target enemy weaknesses to gain extra actions.")
    print("Use items to keep your party alive.")
    print("Explore ten floors and defeat their guardians.")
    pause()


def select_difficulty():
    header("SELECT DIFFICULTY")
    print("1. Easy\n2. Normal\n3. Hard")

    while True:
        choice = input("> ")

        if choice == "1":
            return DIFFICULTIES["Easy"]
        elif choice == "2":
            return DIFFICULTIES["Normal"]
        elif choice == "3":
            return DIFFICULTIES["Hard"]

        print("Invalid choice.")


def select_class(name):
    header(f"CHOOSE CLASS: {name}")
    class_names = list(CLASSES.keys())

    for i, class_name in enumerate(class_names, 1):
        print(f"{i}. {class_name}")

    while True:
        choice = input("> ")

        if choice.isdigit() and 1 <= int(choice) <= len(class_names):
            return class_names[int(choice) - 1]

        print("Invalid choice.")


def start_game():
    difficulty = select_difficulty()

    header("PARTY CREATION")
    party = []

    for name in ["Irety", "Iyanu", "Ayonikun"]:
        selected_class = select_class(name)
        party.append(create_character(name, " ", selected_class))

    items = {"Medicine": 3}

    print("\nYour journey begins...")
    pause()

    run_dungeon(party, difficulty, items)


def main_menu():
    enable_ansi()

    while True:
        header("SAGAP")
        print("1. Start Game")
        print("2. Tutorial")
        print("3. Exit")

        choice = input("> ")

        if choice == "1":
            start_game()
        elif choice == "2":
            tutorial()
        elif choice == "3":
            print("Exiting SAGAP...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main_menu()