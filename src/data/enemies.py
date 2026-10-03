from config import AFFINITIES

def mk_aff(weak=(), resist=(), strong=()):
    """builds a full affinity table for an enemy. anything not listed is neutral. 'strong' means the enemy hardly felt the attack."""
    aff = {a: "Neutral" for a in AFFINITIES}

    for a in weak:
        aff[a] = "Weak"

    for a in resist:
        aff[a] = "Resist"

    for a in strong:
        aff[a] = "Strong"

    return aff
ENEMIES = {
    #Floor 1: Japanese Folklore
    "Yurei": {"hp": 72, "damage": 18, "defence": 7, "xp": 16, "gold": 10,
              "aff": mk_aff(weak=("Fire", "Light", "Wind"), resist=("Slash", "Lightning", "Dark"))},
    "Kappa": {"hp": 92, "damage": 20, "defence": 9, "xp": 19, "gold": 12,
              "aff": mk_aff(weak=("Strike",), resist=("Ice", "Arcane"))},
    "Oni": {"hp": 125, "damage": 27, "defence": 12, "xp": 25, "gold": 16,
            "aff": mk_aff(weak=("Pierce", "Ice", "Light"), resist=("Strike", "Fire", "Poison"))},
    "Jikininki": {"hp": 105, "damage": 25, "defence": 10, "xp": 23, "gold": 15,
                  "aff": mk_aff(weak=("Strike", "Lightning", "Light"), resist=("Pierce", "Dark", "Poison"))},

    #Floor 2: Greek Mythology
    "Lamia": {"hp": 108, "damage": 27, "defence": 11, "xp": 27, "gold": 18,
              "aff": mk_aff(weak=("Slash", "Ice", "Light"), resist=("Pierce", "Dark", "Poison"))},
    "Stymphalian Harpy": {"hp": 100, "damage": 30, "defence": 9, "xp": 27, "gold": 19,
                          "aff": mk_aff(weak=("Pierce", "Lightning", "Arcane"), resist=("Slash", "Wind"))},
    "Empousa": {"hp": 118, "damage": 29, "defence": 11, "xp": 28, "gold": 20,
                "aff": mk_aff(weak=("Fire", "Light"), resist=("Ice", "Dark", "Poison"))},
    "Chimera Whelp": {"hp": 150, "damage": 32, "defence": 13, "xp": 32, "gold": 22,
                      "aff": mk_aff(weak=("Ice",), resist=("Fire", "Strike", "Poison"))},

    #Floor 3: Norse Mythology
    "Draugr": {"hp": 140, "damage": 32, "defence": 15, "xp": 34, "gold": 24,
               "aff": mk_aff(weak=("Fire", "Light"), resist=("Slash", "Ice", "Dark"))},
    "Huldra": {"hp": 130, "damage": 34, "defence": 12, "xp": 35, "gold": 25,
               "aff": mk_aff(weak=("Fire", "Arcane"), resist=("Wind", "Poison"))},
    "Fenris Whelp": {"hp": 155, "damage": 37, "defence": 14, "xp": 37, "gold": 26,
                     "aff": mk_aff(weak=("Pierce", "Fire"), resist=("Slash", "Ice"))},
    "Frost Wight": {"hp": 145, "damage": 33, "defence": 16, "xp": 36, "gold": 26,
                    "aff": mk_aff(weak=("Fire", "Lightning"), resist=("Ice", "Strike"), strong=("Poison",))},

    #Floor 4: Egyptian Mythology
    "Tomb Wight": {"hp": 160, "damage": 36, "defence": 17, "xp": 40, "gold": 28,
                   "aff": mk_aff(weak=("Light", "Fire"), resist=("Slash", "Dark", "Poison"))},
    "Scarab Swarm": {"hp": 140, "damage": 34, "defence": 13, "xp": 39, "gold": 27,
                     "aff": mk_aff(weak=("Fire", "Wind"), resist=("Pierce", "Poison"))},
    "Serpent of Apep": {"hp": 175, "damage": 40, "defence": 16, "xp": 43, "gold": 30,
                        "aff": mk_aff(weak=("Light", "Ice"), resist=("Dark", "Poison"))},
    "Shabti Guardian": {"hp": 185, "damage": 38, "defence": 20, "xp": 42, "gold": 29,
                        "aff": mk_aff(weak=("Lightning", "Arcane"), resist=("Slash", "Strike", "Pierce"))},

    #Floor 5: West African Folklore
    "Bush Spirit": {"hp": 165, "damage": 39, "defence": 15, "xp": 45, "gold": 32,
                    "aff": mk_aff(weak=("Fire", "Light"), resist=("Wind", "Arcane"))},
    "Iron-Tooth Masquerade": {"hp": 190, "damage": 41, "defence": 18, "xp": 47, "gold": 33,
                              "aff": mk_aff(weak=("Lightning",), resist=("Slash", "Strike", "Pierce"))},
    "Whispering Gourd": {"hp": 150, "damage": 37, "defence": 14, "xp": 44, "gold": 31,
                         "aff": mk_aff(weak=("Strike", "Fire"), resist=("Dark", "Arcane", "Poison"))},
    "Restless Shade": {"hp": 170, "damage": 40, "defence": 16, "xp": 46, "gold": 32,
                       "aff": mk_aff(weak=("Light", "Fire"), resist=("Slash", "Dark"))},

    #Floor 6: Hindu Mythology
"Rakshasa Scout": {"hp": 200, "damage": 44, "defence": 19, "xp": 51, "gold": 36,
                       "aff": mk_aff(weak=("Light", "Fire"), resist=("Slash", "Dark"))},
    "Naga Guardian": {"hp": 210, "damage": 43, "defence": 21, "xp": 52, "gold": 37,
                      "aff": mk_aff(weak=("Lightning", "Ice"), resist=("Poison", "Pierce"))},
    "Preta": {"hp": 175, "damage": 42, "defence": 15, "xp": 50, "gold": 35,
              "aff": mk_aff(weak=("Light", "Fire"), resist=("Dark", "Poison", "Slash"))},
    "Yaksha Sentinel": {"hp": 220, "damage": 45, "defence": 22, "xp": 53, "gold": 38,
                        "aff": mk_aff(weak=("Arcane", "Wind"), resist=("Strike", "Slash"))},

    #Floor 7: Aztec mythology
    "Jaguar Spirit Warrior": {"hp": 215, "damage": 47, "defence": 20, "xp": 56, "gold": 40,
                              "aff": mk_aff(weak=("Fire", "Light"), resist=("Slash", "Strike"))},
    "Obsidian Skeleton": {"hp": 230, "damage": 46, "defence": 24, "xp": 57, "gold": 41,
                          "aff": mk_aff(weak=("Strike", "Lightning"), resist=("Slash", "Pierce"))},
    "Ahuizotl": {"hp": 240, "damage": 49, "defence": 21, "xp": 59, "gold": 43,
                 "aff": mk_aff(weak=("Lightning", "Fire"), resist=("Ice", "Poison"))},
    "Star-Demon Whelp": {"hp": 220, "damage": 48, "defence": 20, "xp": 58, "gold": 42,
                         "aff": mk_aff(weak=("Light",), resist=("Dark", "Arcane"), strong=("Poison",))},

 #Floor 8: Slavic folklore
    "Leshy": {"hp": 235, "damage": 50, "defence": 22, "xp": 62, "gold": 45,
              "aff": mk_aff(weak=("Fire", "Slash"), resist=("Wind", "Arcane"))},
    "Rusalka": {"hp": 220, "damage": 49, "defence": 20, "xp": 61, "gold": 44,
                "aff": mk_aff(weak=("Lightning", "Light"), resist=("Ice", "Dark"))},
    "Feral Domovoi": {"hp": 210, "damage": 47, "defence": 19, "xp": 60, "gold": 43,
                      "aff": mk_aff(weak=("Fire",), resist=("Strike", "Pierce", "Poison"))},
    "Vodyanoy": {"hp": 245, "damage": 51, "defence": 23, "xp": 63, "gold": 46,
                 "aff": mk_aff(weak=("Lightning",), resist=("Ice", "Slash"))},

    #Floor 9: Celtic folklore
    "Bean Sidhe": {"hp": 230, "damage": 52, "defence": 21, "xp": 66, "gold": 48,
                   "aff": mk_aff(weak=("Light", "Fire"), resist=("Dark", "Wind"))},
    "Pooka": {"hp": 245, "damage": 53, "defence": 22, "xp": 67, "gold": 49,
              "aff": mk_aff(weak=("Fire", "Arcane"), resist=("Strike", "Pierce"))},
    "Sluagh": {"hp": 250, "damage": 54, "defence": 23, "xp": 68, "gold": 50,
               "aff": mk_aff(weak=("Light",), resist=("Slash", "Dark", "Poison"))},
    "The Fetch": {"hp": 240, "damage": 55, "defence": 24, "xp": 69, "gold": 51,
                  "aff": mk_aff(weak=("Lightning", "Light"), resist=("Dark", "Arcane"))},

    #Floor 10: final freaking floor
    "Echo of a Memory": {"hp": 260, "damage": 56, "defence": 25, "xp": 74, "gold": 55,
                         "aff": mk_aff(weak=("Light", "Arcane"), resist=("Dark", "Slash"))},
    "Grief Wrought Shade": {"hp": 275, "damage": 58, "defence": 26, "xp": 76, "gold": 56,
                            "aff": mk_aff(weak=("Fire", "Light"), resist=("Ice", "Dark"))},
    "Labyrinth Sentinel": {"hp": 300, "damage": 55, "defence": 30, "xp": 78, "gold": 58,
                           "aff": mk_aff(weak=("Lightning", "Arcane"), resist=("Slash", "Strike", "Pierce"))},
    "Fragment of Someone": {"hp": 265, "damage": 60, "defence": 24, "xp": 77, "gold": 57,
                            "aff": mk_aff(weak=("Light",), resist=("Dark", "Poison"), strong=("Arcane",))},
}

FLOOR_ENEMY_POOL = {
    1: ["Yurei", "Kappa", "Oni", "Jikininki"],
    2: ["Lamia", "Stymphalian Harpy", "Empousa", "Chimera Whelp"],
    3: ["Draugr", "Huldra", "Fenris Whelp", "Frost Wight"],
    4: ["Tomb Wight", "Scarab Swarm", "Serpent of Apep", "Shabti Guardian"],
    5: ["Bush Spirit", "Iron-Tooth Masquerade", "Whispering Gourd", "Restless Shade"],
    6: ["Rakshasa Scout", "Naga Guardian", "Preta", "Yaksha Sentinel"],
    7: ["Jaguar Spirit Warrior", "Obsidian Skeleton", "Ahuizotl", "Star-Demon Whelp"],
    8: ["Leshy", "Rusalka", "Feral Domovoi", "Vodyanoy"],
    9: ["Bean Sidhe", "Pooka", "Sluagh", "The Fetch"],
    10: ["Echo of a Memory", "Grief-Wrought Shade", "Labyrinth Sentinel", "Fragment of Someone"],
}

MINIBOSSES = {
    1: {
        "name": "Onryo of the Lanterns",
        "hp": 360,
        "damage": 39,
        "defence": 17,
        "xp": 100,
        "gold": 120,
        "aff": mk_aff(
            weak=("Pierce", "Fire", "Light"),
            resist=("Slash", "Lightning", "Dark", "Poison")
        )
    },

    2: {
        "name": "Cerberus, Gatekeeper of the Dead",
        "hp": 460,
        "damage": 45,
        "defence": 20,
        "xp": 130,
        "gold": 150,
        "aff": mk_aff(
            weak=("Strike", "Ice", "Light"),
            resist=("Pierce", "Fire", "Dark", "Poison")
        )
    },

    3: {
        "name": "Hrafnkell, Draugr-Jarl of the Frostbound Hall",
        "hp": 560,
        "damage": 51,
        "defence": 23,
        "xp": 165,
        "gold": 185,
        "aff": mk_aff(
            weak=("Fire", "Light"),
            resist=("Slash", "Ice", "Dark")
        )
    },

    4: {
        "name": "Ammit, Devourer of the Unworthy",
        "hp": 650,
        "damage": 57,
        "defence": 26,
        "xp": 200,
        "gold": 225,
        "aff": mk_aff(
            weak=("Light", "Lightning"),
            resist=("Slash", "Dark", "Poison")
        )
    },

    5: {
        "name": "The Many-Faced Herald",
        "hp": 740,
        "damage": 62,
        "defence": 29,
        "xp": 240,
        "gold": 265,
        "aff": mk_aff(
            weak=("Lightning", "Arcane"),
            resist=("Slash", "Strike", "Dark")
        )
    },

    6: {
        "name": "Mahisha, the Buffalo-Demon",
        "hp": 830,
        "damage": 68,
        "defence": 32,
        "xp": 280,
        "gold": 305,
        "aff": mk_aff(
            weak=("Pierce", "Light"),
            resist=("Strike", "Dark", "Poison")
        )
    },

    7: {
        "name": "Tzitzimitl, the Star-Eater",
        "hp": 920,
        "damage": 74,
        "defence": 35,
        "xp": 320,
        "gold": 345,
        "aff": mk_aff(
            weak=("Light",),
            resist=("Dark", "Arcane", "Poison")
        )
    },

    8: {
        "name": "Baba Yaga's Hollow",
        "hp": 1010,
        "damage": 80,
        "defence": 38,
        "xp": 360,
        "gold": 385,
        "aff": mk_aff(
            weak=("Fire", "Lightning"),
            resist=("Ice", "Dark", "Arcane")
        )
    },

    9: {
        "name": "The Dullahan",
        "hp": 1100,
        "damage": 86,
        "defence": 41,
        "xp": 400,
        "gold": 425,
        "aff": mk_aff(
            weak=("Light", "Lightning"),
            resist=("Slash", "Dark")
        )
    },
}

FINAL_BOSS = {
    "name": "The Hollow Father",
    "hp": 1450,
    "damage": 78,
    "defence": 34,
    "xp": 600,
    "gold": 0,
    "aff": mk_aff(
        weak=("Strike", "Light"),
        resist=("Pierce", "Lightning", "Poison"),
        strong=("Dark",)
    ),
}
