
import random

from ui import colorize, CYAN, MAGENTA, BOLD, RED, YELLOW
from combat.targeting import alive_party
from combat.helpers import apply_status


def enemy_turn(enemy, party):
    living = alive_party(party)

    if not living:
        return

    taunting = [c for c in living if c.get("taunt", 0) > 0]

    target = random.choice(taunting) if taunting else (
        min(living, key=lambda c: c["hp"] / c["max_hp"])
        if random.random() < 0.65
        else random.choice(living)
    )

    actions = enemy.get("actions", 1)
    ebuffs = enemy.get("buffs", {})

    atk_mod = (
        1.0
        + ebuffs.get("ATK_UP", {}).get("value", 0)
        - ebuffs.get("ATK_DOWN", {}).get("value", 0)
    )

    for _ in range(actions):
        living = alive_party(party)

        if not living:
            return

        if target["hp"] <= 0:
            target = random.choice(living)

        special = random.random() < 0.25

        base_damage = (
            enemy["damage"]
            * (1.4 if special else 1.0)
            * atk_mod
        )

        damage = max(
            1,
            int(base_damage)
            + random.randint(-5, 6)
            - target["stats"]["EN"] * 2 // 3
        )

        tbuffs = target.get("buffs", {})

        def_mod = (
            tbuffs.get("DEF_DOWN", {}).get("value", 0)
            - tbuffs.get("DEF_UP", {}).get("value", 0)
        )

        damage = max(1, int(damage * (1 + def_mod)))

        if target.get("guarding", False):
            damage = max(1, int(damage * 0.45))

        if special and target.get("class") == "Saber":
            damage = max(1, int(damage * 0.80))

        if target.get("class") == "Berserker":
            damage = max(1, int(damage * 1.15))

        evade_chance = (
            target["stats"]["AG"] / 300
            + tbuffs.get("EVADE_UP", {}).get("value", 0)
        )

        if target.get("class") == "Assassin":
            evade_chance += 0.10

        if random.random() < evade_chance:
            print(colorize(f"{target['name']} evaded the attack!", CYAN))
            continue

        target["hp"] -= damage

        target["np_gauge"] = min(
            100, target.get("np_gauge", 0) + 12
        )

        tag = (
            colorize(" [SPECIAL]", MAGENTA + BOLD)
            if special else ""
        )

        print(
            f"{colorize(enemy['name'], RED)} attacked "
            f"{target['name']}{tag} for "
            f"{colorize(str(damage), YELLOW)} damage."
        )

        if special and target["hp"] > 0 and random.random() < 0.35:
            status = random.choice(["Stunned", "Poison"])
            apply_status(target, status, 1.0, 2)
            print(
                colorize(
                    f"{target['name']} was afflicted with {status}!",
                    RED
                )
            )

        elif target["hp"] > 0 and random.random() < 0.15:
            apply_status(target, "Stunned", 1.0, 1)
            print(colorize(f"{target['name']} was stunned!", RED))

        if target["hp"] <= 0:
            target["hp"] = 0
            print(
                colorize(
                    f"{target['name']} has fallen!",
                    RED + BOLD
                )
            )
