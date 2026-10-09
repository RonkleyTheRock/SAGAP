
import random

from config import MAGIC_AFFINITIES
from ui import colorize, RED, YELLOW, BOLD, MAGENTA, GREEN, WHITE
from combat.helpers import affinity_multiplier, record_knowledge


def deal_attack(character, target, affinity, power, knowledge, label):
    result = target["aff"].get(affinity, "Neutral")

    if result != "Neutral":
        record_knowledge(
            knowledge, target["name"], affinity, result
        )

    cbuffs = character.get("buffs", {})
    atk_mod = (
        1.0
        + cbuffs.get("ATK_UP", {}).get("value", 0)
        - cbuffs.get("ATK_DOWN", {}).get("value", 0)
    )

    if affinity in MAGIC_AFFINITIES:
        raw = power + character["stats"]["MA"] * 2
    else:
        raw = power + character["stats"]["ST"] * 2

    raw *= atk_mod

    if character.get("class") == "Berserker":
        raw *= 1.20

    raw = max(1, raw - target["defence"])

    tbuffs = target.get("buffs", {})
    def_mod = (
        tbuffs.get("DEF_DOWN", {}).get("value", 0)
        - tbuffs.get("DEF_UP", {}).get("value", 0)
    )

    damage = max(
        1,
        int(raw * affinity_multiplier(result) * (1 + def_mod))
    )

    is_assassin = character.get("class") == "Assassin"
    crit_chance = min(
        0.35,
        0.05 + character["stats"]["LK"] / 300
    )

    if character.get("class") == "Archer":
        crit_chance = min(0.5, crit_chance + 0.05)

    if is_assassin:
        crit_chance = min(0.65, crit_chance * 2)

    crit = random.random() < crit_chance

    if crit:
        damage = int(damage * (1.75 if is_assassin else 1.5))

    target["hp"] -= damage

    print(
        f"{character['name']} used {label}  "
        f"{colorize(target['name'], RED)} took "
        f"{colorize(str(damage), YELLOW + BOLD)} damage."
    )

    if crit:
        print(colorize("CRITICAL HIT!", MAGENTA + BOLD))

    if result != "Neutral":
        aff_color = (
            GREEN if result == "Weak"
            else RED if result in ("Resist", "Strong")
            else WHITE
        )
        print(f"Affinity: {colorize(result, aff_color)}")

    if target["hp"] <= 0:
        target["hp"] = 0
        print(
            colorize(
                f"{target['name']} was defeated!",
                RED + BOLD
            )
        )

    character["np_gauge"] = min(
        100, character.get("np_gauge", 0) + 15
    )

    return result
