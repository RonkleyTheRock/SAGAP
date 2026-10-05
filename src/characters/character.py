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
def change_classes(character):
    old_class = character["class"]

    print(f"\n{character['name']} is currently a {old_class}.")

    new_class = choose_class()

    if new_class == old_class:
        print("The character is already this Class.")
        return False

    character["class"] = new_class

    sync_class_stats(character, old_class, new_class)

    print(f"{character['name']} changed Class from {old_class} to {new_class}.")

    return True
def choose_inherited_skill(character, old_class):
    mastered = character.get("class_mastery", set())

    if old_class not in mastered:
        return

    skills = CLASSES[old_class]["class_skills"]

    if not skills:
        return

    print(f"\nChoose a skill to inherit from {old_class}:")

    for i, skill in enumerate(skills, 1):
        print(f"{i}. {skill['name']} - {skill['description']}")

    while True:
        choice = input("> ")

        if choice.isdigit() and 1 <= int(choice) <= len(skills):
            character["inherited_skill"] = skills[int(choice) - 1]
            print(f"Inherited skill: {skills[int(choice) - 1]['name']}")
            return

        print("Invalid choice.")
def unlocked_skills(character):
    skills = CLASSES[character["class"]]["skills"]
    return [
        skill
        for skill in skills
        if character["level"] >= skill["level"]
    ]
def xp_needed(level):
    return 10 + (3 * level)

if __name__ == "__main__":
    print("Level 1 XP:", xp_needed(1))
    print("Level 5 XP:", xp_needed(5))
    print("Level 10 XP:", xp_needed(10))

def level_up(character):
    while character["xp"] >= xp_needed(character["level"]):
        required = xp_needed(character["level"])
        character["xp"] -= required
        character["level"] += 1

        character["max_hp"] += 10
        character["hp"] = character["max_hp"]

        character["max_mp"] += 5
        character["mp"] = character["max_mp"]

        print(
            f"{character['name']} reached Level "
            f"{character['level']}!"
        )

        check_mastery(character)

        unlocked = [
            skill
            for skill in CLASSES[character["class"]]["skills"]
            if skill["level"] == character["level"]
        ]

        if unlocked:
            print("New skill unlocked:")
            for skill in unlocked:
                print(f"- {skill['name']}")

def show_party(party):
    header("PARTY", 64, "-")

    for character in party:
        print(
            f"{character['name']} | "
            f"{character['class']} | "
            f"Level {character['level']} | "
            f"HP {character['hp']}/{character['max_hp']} | "
            f"MP {character['mp']}/{character['max_mp']}"
        )
