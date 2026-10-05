from data.classes import CLASSES
from config import STAT_NAMES
from ui import header, colorize, YELLOW


def create_character(name, personality, class_name):
    stats = CLASSES[class_name]["stats"].copy()

    return {
        "name": name,
        "personality": personality,
        "class": class_name,
        "level": 1,
        "xp": 0,
        "stats": stats,
        "max_hp": stats["HP"],
        "hp": stats["HP"],
        "max_mp": stats["MP"],
        "mp": stats["MP"],
        "gold": 60,
        "inherited_skill": None,
        "guarding": False,
        "status": None,
        "statuses": {},
        "buffs": {},
        "taunt": 0,
        "np_gauge": 0,
        "class_mastery": set(),
        "_free_cast_used": False,
    }


def check_mastery(character):
    """Reaching level 7 while holding a Class means that Class's contract is
    permanent - its basic skill stays with this character even after they
    move on to another Class."""

    if character["level"] >= 7:
        character.setdefault("class_mastery", set()).add(character["class"])


def make_party():
    print("\nIrety forms her first contract. Choose the Class that answers her call.")

    class_name = choose_class()

    party = [
        create_character(
            "Irety",
            "Calls herself the strong one so often it stopped being a compliment "
            "and started being a job description. Doesn't always believe it. "
            "Says it anyway.",
            class_name
        ),
        create_character(
            "Iyanu",
            "Apologizes before sentences that don't need one. Sharper than he lets "
            "on, and getting tired of being surprised when people notice.",
            "Caster"
        ),
        create_character(
            "Ayonikun",
            "Learns everything on the first try and has never once figured out "
            "what to do with the version of herself that doesn't.",
            "Lancer"
        ),
    ]

    return party


def choose_class():
    names = list(CLASSES.keys())

    while True:
        header("SELECT CLASS", 64, "-")

        for i, name in enumerate(names, 1):
            print(
                f"{i}. {colorize(name, YELLOW)} - "
                f"{CLASSES[name]['description']}"
            )

        choice = input("> ")

        if choice.isdigit() and 1 <= int(choice) <= len(names):
            return names[int(choice) - 1]

        print("Invalid choice.")


def sync_class_stats(character, old_class, new_class):
    new = CLASSES[new_class]["stats"]

    ratio_hp = character["hp"] / max(1, character["max_hp"])
    ratio_mp = character["mp"] / max(1, character["max_mp"])

    for stat in STAT_NAMES:
        character["stats"][stat] = new[stat] + (character["level"] - 1) // 2

    character["max_hp"] = new["HP"] + (character["level"] - 1) * 10
    character["max_mp"] = new["MP"] + (character["level"] - 1) * 5

    character["hp"] = max(
        1,
        min(
            character["max_hp"],
            int(character["max_hp"] * ratio_hp)
        )
    )

    character["mp"] = max(
        0,
        min(
            character["max_mp"],
            int(character["max_mp"] * ratio_mp)
        )
    )

    check_mastery(character)


if __name__ == "__main__":
    test_character = create_character(
        "Irety",
        "Strong and protective",
        "Saber"
    )

    print("Before:", test_character["class"])
    print("Stats:", test_character["stats"])

    test_character["level"] = 5

    sync_class_stats(test_character, "Saber", "Caster")

    print("After:", test_character["class"])
    print("Stats:", test_character["stats"])
    print("HP:", test_character["hp"], "/", test_character["max_hp"])
    print("MP:", test_character["mp"], "/", test_character["max_mp"])
