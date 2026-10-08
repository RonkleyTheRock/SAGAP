import random

from ui import header


def alive_party(party):
    return [c for c in party if c["hp"] > 0]


def alive_enemies(enemies):
    return [e for e in enemies if e["hp"] > 0]


def affinity_multiplier(result):
    return {
        "Weak": 1.5,
        "Neutral": 1.0,
        "Resist": 0.5,
        "Strong": 0.25
    }.get(result, 1.0)


def scaled_stat(value, floor, difficulty):
    return max(
        1,
        int(value * difficulty * (1 + 0.10 * (floor - 1)))
    )


def apply_buff(target, name, value, turns):
    target.setdefault("buffs", {})[name] = {
        "value": value,
        "turns": turns
    }


def apply_status(target, status, chance, duration=2):
    if random.random() < chance:
        target["statuses"][status] = duration
        target["status"] = status
        return True
    return False


def classify(result):
    if result == "Weak":
        return "Weak"

    if result in ("Resist", "Strong"):
        return "Resist"

    return "Neutral"


def combat(party, enemies, items, knowledge, difficulty, boss=False):
    max_tokens = len(alive_party(party))
    header("COMBAT START", 64, "=")
    print("Press-turn combat: weaknesses grant a bonus action, resisted hits cost two.")

    for c in party:
        c["_free_cast_used"] = False

    while alive_party(party) and alive_enemies(enemies):
        tokens = max_tokens

        for c in party:
            c["guarding"] = False

        show_battle_status(enemies, party)


if __name__ == "__main__":
    party = [
        {
            "name": "Irety",
            "hp": 100,
            "guarding": True,
            "_free_cast_used": True
        }
    ]

    enemies = []

    combat(party, enemies, {}, {}, 1.15)

    print(party)
