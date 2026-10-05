def grade(value):
    if value >= 19:
        return "A+"
    if value >= 16:
        return "A"
    if value >= 13:
        return "B"
    if value >= 10:
        return "C"
    if value >= 7:
        return "D"
    return "E"


def parameter_grades(stats):
    return {
        "Strength": grade(stats["ST"]),
        "Endurance": grade(stats["EN"]),
        "Agility": grade(stats["AG"]),
        "Mana": grade(stats["MA"]),
        "Luck": grade(stats["LK"]),
    }


CLASSES = {
    "Saber": {
        "description": "A balanced, all-around blade. Strong everywhere, weak nowhere, and faintly insulted by the idea that fairness is boring.",
        "stats": {"HP": 135, "MP": 25, "ST": 15, "EN": 15, "MA": 3, "LK": 5, "AG": 6},
        "passive": "After every battle, restore 5% of maximum HP.",
        "class_skills": [
            {
                "name": "Magic Resistance",
                "description": "A standing contempt for spellwork that isn't theirs. Magic-affinity damage taken is reduced.",
                "effect": "magic_resist"
            },
        ],
        "personal_skill": {
            "name": "Unshaken Guard",
            "description": "Draws every eye in the room on purpose, and has never once regretted it."
        },
        "skills": [
            {"name": "Oathbreaker Strike", "level": 1, "power": 24, "affinity": "Strike", "cost": 0, "target": "enemy"},
            {"name": "Vow-Cleaving Arc", "level": 1, "power": 30, "affinity": "Slash", "cost": 4, "target": "enemy"},
            {"name": "Bulwark of Oaths", "level": 4, "power": 0, "affinity": "Guard", "cost": 8, "target": "self",
             "effect": "taunt"},
            {"name": "Shieldbreaker Descent", "level": 7, "power": 60, "affinity": "Strike", "cost": 10,
             "target": "enemy"},
            {"name": "Thunderclap Verdict", "level": 10, "power": 78, "affinity": "Lightning", "cost": 15,
             "target": "enemy"},
        ],
        "noble_phantasm": {
            "name": "Titanomachy",
            "true_name": "ALL THE WEIGHT OF WHAT I REFUSED TO DROP",
            "power": 150,
            "affinity": "Strike",
            "target": "enemy",
            "declaration": "Every shield is a promise shaped like an object. This one's final clause:"
        },
    },

    "Lancer": {
        "description": "Fast, aggressive, and allergic to standing still long enough to be hit back.",
        "stats": {"HP": 105, "MP": 35, "ST": 14, "EN": 8, "MA": 4, "LK": 11, "AG": 17},
        "passive": "After every battle, restore 5% of maximum MP and a small amount of HP.",
        "class_skills": [
            {
                "name": "Independent Action",
                "description": "Needs nobody's permission to keep fighting. Regains a little MP every turn they act.",
                "effect": "mp_regen"
            },
        ],
        "personal_skill": {
            "name": "First Strike",
            "description": "Always wants to go first. Has never once stopped to ask if that's actually a good idea."
        },
        "skills": [
            {"name": "Gale Draw", "level": 1, "power": 23, "affinity": "Slash", "cost": 0, "target": "enemy"},
            {"name": "Crescent Reaping", "level": 1, "power": 28, "affinity": "Slash", "cost": 5, "target": "enemy"},
            {"name": "Thread-Piercer", "level": 4, "power": 43, "affinity": "Pierce", "cost": 8, "target": "enemy"},
            {"name": "Dawnlit Whirl", "level": 7, "power": 58, "affinity": "Light", "cost": 11, "target": "enemy"},
            {"name": "Hundred-Thread Rush", "level": 10, "power": 76, "affinity": "Slash", "cost": 15,
             "target": "enemy"},
        ],
        "noble_phantasm": {
            "name": "Moirae Sever",
            "true_name": "THE THREAD WAS NEVER YOURS TO MEASURE",
            "power": 160,
            "affinity": "Slash",
            "target": "enemy",
            "declaration": "A spear doesn't ask what it's cutting through. That's the whole design flaw. And the whole point."
        },
    },

    "Caster": {
        "description": "A scholar of forces that were never meant to be scholarly about. Exploits elemental weakness with something close to academic glee.",
        "stats": {"HP": 82, "MP": 82, "ST": 3, "EN": 6, "MA": 18, "LK": 9, "AG": 9},
        "passive": "After every battle, restore 5% of maximum MP.",
        "class_skills": [
            {
                "name": "Territory Creation",
                "description": "On the first turn of a fight, the battlefield is briefly theirs. Their first skill that turn costs no MP.",
                "effect": "free_first_cast"
            },
        ],
        "personal_skill": {
            "name": "Workshop Mind",
            "description": "Treats every disaster as a hypothesis. This has gotten them hurt exactly as often as it's saved everyone."
        },
        "skills": [
            {"name": "Kenaz Ignition", "level": 1, "power": 29, "affinity": "Fire", "cost": 5, "target": "enemy"},
            {"name": "Isa Freeze", "level": 1, "power": 29, "affinity": "Ice", "cost": 5, "target": "enemy"},
            {"name": "Thurisaz Bolt", "level": 4, "power": 45, "affinity": "Lightning", "cost": 8, "target": "enemy"},
            {"name": "Ansuz Gale", "level": 7, "power": 57, "affinity": "Wind", "cost": 11, "target": "enemy"},
            {"name": "Nauthiz Eclipse", "level": 10, "power": 75, "affinity": "Dark", "cost": 16, "target": "enemy"},
        ],
        "noble_phantasm": {
            "name": "Amaterasu Cataclysm",
            "true_name": "EVERY EQUATION ENDS WITH SOMETHING BURNING",
            "power": 175,
            "affinity": "Arcane",
            "target": "enemy",
            "declaration": "You wanted to know how it works. This is the part of the lecture where it stops being theoretical."
        },
    },

    "Berserker": {
        "description": "Power purchased with something that isn't money. Hits like consequence finally catching up to someone.",
        "stats": {"HP": 92, "MP": 70, "ST": 5, "EN": 6, "MA": 14, "LK": 10, "AG": 9},
        "passive": "Skills that draw on this character's own life force deal 25% additional damage.",
        "class_skills": [
            {
                "name": "Mad Enhancement",
                "description": "Trades composure for raw output. Deals extra damage, at the cost of a little of their own defence.",
                "effect": "mad_enhancement"
            },
        ],
        "personal_skill": {
            "name": "Borrowed Fury",
            "description": "Doesn't actually enjoy this. Has simply decided that enjoying it isn't a prerequisite for doing it well."
        },
        "skills": [
            {"name": "Maddened Roar", "level": 1, "power": 16, "affinity": "Dark", "cost": 6, "target": "enemy",
             "effect": "debuff_def"},
            {"name": "Hollow Rage", "level": 1, "power": 20, "affinity": "Dark", "cost": 8, "target": "enemy",
             "effect": "debuff_atk"},
            {"name": "Bloodied Rampage", "level": 4, "power": 48, "affinity": "Dark", "cost": 8, "hp_cost": 15,
             "target": "enemy"},
            {"name": "Bane of Reason", "level": 7, "power": 30, "affinity": "Dark", "cost": 14, "target": "enemy",
             "effect": "debuff_def"},
            {"name": "Soul-Eater's Feast", "level": 10, "power": 85, "affinity": "Dark", "cost": 16, "hp_cost": 25,
             "target": "enemy"},
        ],
        "noble_phantasm": {
            "name": "Abyssal Communion",
            "true_name": "I WILL SPEND WHATEVER OF ME IS LEFT",
            "power": 210,
            "affinity": "Dark",
            "target": "enemy",
            "hp_cost": 40,
            "declaration": "There's a version of strength that doesn't cost anything. This isn't that version. It never was."
        },
    },

    "Archer": {
        "description": "Keeps everything at a distance, including - a little too often - the people trying to help.",
        "stats": {"HP": 96, "MP": 62, "ST": 6, "EN": 8, "MA": 13, "LK": 12, "AG": 10},
        "passive": "Status effects inflicted by this character last one turn longer.",
        "class_skills": [
            {
                "name": "Clairvoyance",
                "description": "Sees the gap in a guard before it opens. Critical hit chance is modestly increased.",
                "effect": "crit_up"
            },
        ],
        "personal_skill": {
            "name": "A Thousand Variations",
            "description": "Never throws the same flask the same way twice. Mostly out of boredom, partly out of habit."
        },
        "skills": [
            {"name": "Viper's Draught", "level": 1, "power": 16, "affinity": "Poison", "cost": 6, "target": "enemy",
             "effect": "poison"},
            {"name": "Winter's Philter", "level": 1, "power": 16, "affinity": "Ice", "cost": 6, "target": "enemy",
             "effect": "freeze"},
            {"name": "Elixir of Valor", "level": 4, "power": 0, "affinity": "Support", "cost": 10, "target": "party",
             "effect": "buff_atk"},
            {"name": "Rust-Eater Flask", "level": 7, "power": 34, "affinity": "Poison", "cost": 12, "target": "enemy",
             "effect": "debuff_def"},
            {"name": "Phoenix Ember Vial", "level": 10, "power": 42, "affinity": "Fire", "cost": 15, "target": "enemy",
             "effect": "burn"},
        ],
        "noble_phantasm": {
            "name": "Grand Alchemy",
            "true_name": "EVERYTHING IS FLAMMABLE IF YOU'RE PATIENT ENOUGH",
            "power": 95,
            "affinity": "Fire",
            "target": "all_enemies",
            "effect": "burn",
            "declaration": "One flask was never the point. The point was always what happens once all of them land."
        },
    },

    "Assassin": {
        "description": "Unpredictable, fast, and allergic to being watched closely - including, occasionally, by their own party.",
        "stats": {"HP": 85, "MP": 42, "ST": 11, "EN": 5, "MA": 5, "LK": 18, "AG": 20},
        "passive": "Critical hit chance is doubled, and critical hits deal 75% bonus damage instead of 50%.",
        "class_skills": [
            {
                "name": "Presence Concealment",
                "description": "Harder to pin down than to actually fight. Evasion is modestly increased.",
                "effect": "evasion_up"
            },
        ],
        "personal_skill": {
            "name": "Uncounted Blade",
            "description": "Keeps a tally of every opening nobody else noticed. Won't say the number out loud. It's higher than you'd like."
        },
        "skills": [
            {"name": "Shadow Step Cut", "level": 1, "power": 22, "affinity": "Slash", "cost": 0, "target": "enemy"},
            {"name": "Hollow Needle", "level": 1, "power": 26, "affinity": "Pierce", "cost": 5, "target": "enemy"},
            {"name": "Mist Veil", "level": 4, "power": 0, "affinity": "Support", "cost": 8, "target": "self",
             "effect": "evade_up"},
            {"name": "Fortune's Dagger", "level": 7, "power": 50, "affinity": "Slash", "cost": 12, "target": "enemy"},
            {"name": "Seven Silent Cuts", "level": 10, "power": 18, "affinity": "Slash", "cost": 16, "target": "enemy",
             "effect": "multihit"},
        ],
        "noble_phantasm": {
            "name": "Fatal Gambit",
            "true_name": "YOU ONLY NEEDED TO BE WRONG ABOUT ME ONCE",
            "power": 165,
            "affinity": "Slash",
            "target": "enemy",
            "declaration": "Being underestimated was never an insult. It was just the setup. Here's the rest of the sentence."
        },
    },

    "Rider": {
        "description": "Carries the wounded further than they could've walked alone - sometimes back from somewhere further than that.",
        "stats": {"HP": 94, "MP": 78, "ST": 4, "EN": 7, "MA": 16, "LK": 9, "AG": 8},
        "passive": "After a hard-won battle, there is a chance to ease some of the party's wounds.",
        "class_skills": [
            {
                "name": "Psychopomp's Grace",
                "description": "Has made this exact crossing before, in both directions. Healing output is increased.",
                "effect": "heal_up"
            },
        ],
        "personal_skill": {
            "name": "One More Mile",
            "description": "Has never once said a destination was too far. Has also never once said that was a comfortable policy."
        },
        "skills": [
            {"name": "Ferryman's Mending", "level": 1, "power": 45, "affinity": "Light", "cost": 8, "target": "ally",
             "effect": "heal"},
            {"name": "Lantern Bolt", "level": 1, "power": 20, "affinity": "Light", "cost": 5, "target": "enemy"},
            {"name": "River Cleansing", "level": 4, "power": 0, "affinity": "Support", "cost": 10, "target": "ally",
             "effect": "cure"},
            {"name": "Lantern Tide", "level": 7, "power": 35, "affinity": "Light", "cost": 18, "target": "party",
             "effect": "heal"},
            {"name": "Crossing Blessing", "level": 10, "power": 0, "affinity": "Support", "cost": 14, "target": "party",
             "effect": "buff_def"},
        ],
        "noble_phantasm": {
            "name": "Miracle",
            "true_name": "I HAVE MADE THIS CROSSING BEFORE, AND I WILL MAKE IT AGAIN",
            "power": 140,
            "affinity": "Light",
            "target": "party",
            "effect": "miracle",
            "declaration": "Nobody gets left on the far bank. That was true the first time I said it, and it's still true now."
        },
    },
}
