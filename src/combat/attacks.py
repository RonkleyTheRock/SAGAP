from combat.combat import affinity_multiplier, classify
from ui import colorize, RED, GREEN, BOLD


def deal_attack(character, target, affinity, power, knowledge, skill_name):
    attack = character["stats"]["ST"]
    defence = target.get("defence", 0)

    damage = max(1, int(power + attack - defence))

    target["hp"] = max(0, target["hp"] - damage)

    print(
        f"{character['name']} uses {skill_name} "
        f"against {target['name']} for {damage} damage!"
    )

    result = target.get("affinities", {}).get(affinity, "Neutral")

    if result == "Weak":
        knowledge.setdefault(target["name"], {})[affinity] = result
    elif result in ("Resist", "Strong"):
        knowledge.setdefault(target["name"], {})[affinity] = result

    return result
