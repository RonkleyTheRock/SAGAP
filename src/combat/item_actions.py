from data.items import ITEMS
from ui import header, clear_screen, pause
from systems.inventory import use_item
from combat.targeting import choose_character


def battle_item_menu(character, party, items):
    while True:
        clear_screen()
        usable = [
            name for name, amount in items.items()
            if amount > 0 and name in ITEMS
        ]

        header("ITEMS", 64, "-")

        if not usable:
            print("You have no usable items.")
            pause()
            return False

        for i, name in enumerate(usable, 1):
            print(f"{i}. {name} x{items[name]} - {ITEMS[name]['description']}")

        print("0. Back")
        choice = input("> ").strip()

        if choice == "0":
            return False

        if not choice.isdigit() or not 1 <= int(choice) <= len(usable):
            print("Invalid choice.")
            pause()
            continue

        name = usable[int(choice) - 1]

        if name == "Smoke Bomb":
            character["escape_bonus"] = True
            items[name] -= 1
            print("The Smoke Bomb clouds the battlefield. Your next escape attempt is more likely to succeed.")
            pause()
            return True

        print(f"\nChoose a target for {name}.")
        target = choose_character(party, include_dead=(name == "Revival Bead"))

        if target is None:
            print("There is no valid target.")
            pause()
            continue

        if use_item(name, target):
            items[name] -= 1
            print(f"{target['name']} was affected by {name}.")
            pause()
            return True

        print(f"{name} had no effect on {target['name']}.")
        print("Choose a valid target or select another item.")
        pause()
