import random

from ui import colorize, RED, GREEN, BOLD


def enemy_turn(enemy, party):
    living = [c for c in party if c["hp"] > 0]

    if not living:
        return

    taunting = [c for c in living if c.get("taunt", 0) > 0]

    if taunting:
        target = random.choice(taunting)
    elif random.random() < 0.65:
        target = min(
            living,
            key=lambda c: c["hp"] / c["max_hp"]
        )
    else:
        target = random.choice(living)

    actions = enemy.get("actions", 1)
    enemy_buffs = enemy.get("buffs", {})

    attack_modifier = (
        1.0
        + enemy_buffs.get("ATK_UP", {}).get("value", 0)
        - enemy_buffs.get("ATK_DOWN", {}).get("value", 0)
    )

    for _ in range(actions):
        living = [c for c in party if c["hp"] > 0]

        if not living:
            return

        if target["hp"] <= 0:
            target = random.choice(living)

        damage = max(
            1,
            int(
                enemy["attack"]
                * attack_modifier
                - target["stats"]["EN"]
            )
        )

        if target.get("guarding", False):
            damage = max(1, damage // 2)

        target["hp"] = max(0, target["hp"] - damage)

        print(
            f"{enemy['name']} attacks {target['name']} "
            f"for {damage} damage!"
        )

        if target["hp"] <= 0:
            print(f"{target['name']} has been defeated!")
