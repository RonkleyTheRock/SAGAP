
from data.items import ITEMS
from ui import header
from systems.inventory import use_item
from combat.targeting import choose_character


def battle_item_menu(character, party, items):
    usable = [
        name for name, amount in items.items()
        if amount > 0 and name != "Smoke Bomb"
    ]

    header("ITEMS", 64, "-")

    for i, name in enumerate(usable, 1):
        print(
            f"{i}. {name} x{items[name]} - "
            f"{ITEMS[name]['description']}"
        )

    print("0. Back")
    choice = input("> ")

    if choice == "0":
        return False

    if choice.isdigit() and 1 <= int(choice) <= len(usable):
        name = usable[int(choice) - 1]

        print("Choose a target:")
        target = choose_character(
            party,
            include_dead=(name == "Revival Bead")
        )

        if target and use_item(name, target):
            items[name] -= 1
            print(f"Used {name} on {target['name']}.")
            return True

    print("Item could not be used.")
    return False
