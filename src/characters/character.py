from data.classes import CLASSES


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
