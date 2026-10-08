def xp_needed(level):
    return 10 + (3 * level)

from config import STAT_NAMES
from ui import colorize, GREEN, BOLD


def level_up(character, amount):
    character["xp"] += amount

    while character["xp"] >= xp_needed(character["level"]):
        character["xp"] -= xp_needed(character["level"])
        character["level"] += 1

        automatic = STAT_NAMES[
            (character["level"] - 2) % len(STAT_NAMES)
        ]

        character["stats"][automatic] += 1
        character["max_hp"] += 10
        character["max_mp"] += 5
        character["hp"] = character["max_hp"]
        character["mp"] = character["max_mp"]

        print(
            colorize(
                f"\n*** {character['name']} reached LEVEL "
                f"{character['level']}! ***",
                GREEN + BOLD
            )
        )

        print(f"Automatic stat increase: {automatic} +1")
        print("Choose one additional stat:")

        for i, stat in enumerate(STAT_NAMES, 1):
            print(f"{i}. {stat}")

        while True:
            c = input("> ")

            if c.isdigit() and 1 <= int(c) <= 5:
                stat = STAT_NAMES[int(c) - 1]
                character["stats"][stat] += 1
                break
def unlocked_skills(character):
    skills = [
        skill
        for skill in CLASSES[character["class"]]["skills"]
        if character["level"] >= skill["level"]
    ]

    if character["inherited_skill"]:
        skills.append(character["inherited_skill"])

    for class_name in sorted(character.get("class_mastery", set())):
        if class_name != character["class"]:
            mastered = CLASSES[class_name]["skills"][0].copy()
            mastered["source"] = class_name
            mastered["mastered"] = True
            skills.append(mastered)

    return skills


def check_mastery(character):
    if character["level"] >= 7:
        character.setdefault("class_mastery", set()).add(
            character["class"]
        )
