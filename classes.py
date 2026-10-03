from config import STAT_NAMES

CLASSES = {
    "Vanguard": {
        "description": "Physically powerful protector.",
        "stats": {"HP": 135, "MP": 25, "ST": 15, "EN": 15, "MA": 3, "LK": 5, "AG": 6},
        "skills": [
            {"name": "Susanoo Break", "affinity": "Slash", "power": 30, "cost": 4, "target": "enemy"}
        ],
    },
    "Duelist": {
        "description": "Fast physical attacker.",
        "stats": {"HP": 105, "MP": 35, "ST": 14, "EN": 8, "MA": 4, "LK": 11, "AG": 17},
        "skills": [
            {"name": "Izanami's Edge", "affinity": "Slash", "power": 28, "cost": 5, "target": "enemy"}
        ],
    },
    "Arcanist": {
        "description": "Elemental magic user.",
        "stats": {"HP": 82, "MP": 82, "ST": 3, "EN": 6, "MA": 18, "LK": 9, "AG": 9},
        "skills": [
            {"name": "Kagutsuchi", "affinity": "Fire", "power": 29, "cost": 5, "target": "enemy"},
            {"name": "Yuki-Onna", "affinity": "Ice", "power": 29, "cost": 5, "target": "enemy"}
        ],
    },
    "Priest": {
        "description": "Party healer.",
        "stats": {"HP": 94, "MP": 78, "ST": 4, "EN": 7, "MA": 16, "LK": 9, "AG": 8},
        "skills": [
            {"name": "Mending Light", "affinity": "Light", "power": 45, "cost": 8, "target": "ally", "effect": "heal"},
            {"name": "Sacred Bolt", "affinity": "Light", "power": 20, "cost": 5, "target": "enemy"}
        ],
    },
}

def choose_class(character_name):
    names = list(CLASSES.keys())
    while True:
        print(f"\nSelect a class for {character_name}:")
        for i, name in enumerate(names, 1):
            print(f"{i}. {name} - {CLASSES[name]['description']}")
        choice = input("> ")
        if choice.isdigit() and 1 <= int(choice) <= len(names):
            return names[int(choice) - 1]
        print("Invalid choice.")

def create_character(name, class_name):
    stats = CLASSES[class_name]["stats"].copy()
    return {
        "name": name,
        "class": class_name,
        "stats": stats,
        "max_hp": stats["HP"],
        "hp": stats["HP"],
        "max_mp": stats["MP"],
        "mp": stats["MP"],
        "skills": CLASSES[class_name]["skills"].copy(),
        "guarding": False
    }
