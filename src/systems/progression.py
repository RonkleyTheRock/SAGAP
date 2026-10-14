from config import STAT_NAMES
from ui import clear_screen, header, pause


def xp_needed(level):
    return 10 + (3 * level)


def level_up(character, amount):
    character["xp"] = character.get("xp", 0) + amount
    while character["xp"] >= xp_needed(character["level"]):
        character["xp"] -= xp_needed(character["level"])
        character["level"] += 1
        character["max_hp"] += 10
        character["max_mp"] += 5
        character["hp"] = character["max_hp"]
        character["mp"] = character["max_mp"]
        from characters.character import check_mastery
        check_mastery(character)

        clear_screen()
        header(f"LEVEL UP — {character['name']}")
        print(f"{character['name']} reached level {character['level']}!")
        print("HP and MP maximums increased, and were restored.")
        print("Choose one stat to increase by 1:")
        for index, stat in enumerate(STAT_NAMES, 1):
            print(f"{index}. {stat} (currently {character['stats'][stat]})")
        while True:
            choice = input("> ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(STAT_NAMES):
                chosen = STAT_NAMES[int(choice) - 1]
                character["stats"][chosen] += 1
                print(f"{chosen} increased by 1.")
                break
            print(f"Choose a number from 1 to {len(STAT_NAMES)}.")
        pause()
        newly_unlocked = [
            skill for skill in unlocked_skills(character)
            if skill.get("level") == character["level"]
        ]
        if newly_unlocked:
            clear_screen()
            header("NEW SKILL UNLOCKED")
            for skill in newly_unlocked:
                print(f"{character['name']} can now use {skill['name']}.")
            pause()


def unlocked_skills(character):
    from data.classes import CLASSES

    skills = [
        skill for skill in CLASSES[character["class"]]["skills"]
        if character["level"] >= skill["level"]
    ]
    inherited = character.get("inherited_skill")
    if inherited and inherited not in skills:
        skills.append(inherited)
    for class_name in sorted(character.get("class_mastery", set())):
        for skill in CLASSES[class_name].get("class_skills", []):
            if not any(existing.get("name") == skill.get("name") for existing in skills):
                mastered_skill = skill.copy()
                mastered_skill["mastered"] = True
                mastered_skill["source"] = class_name
                skills.append(mastered_skill)
    return skills

