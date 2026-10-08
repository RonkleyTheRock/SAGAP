import random
def alive_party(party):
    return [c for c in party if c["hp"] > 0]

if __name__ == "__main__":
    party = [
        {"name": "Irety", "hp": 100},
        {"name": "Iyanu", "hp": 0},
        {"name": "Ayonikun", "hp": 50},
    ]

    print(alive_party(party))


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
        int(value * difficulty * (1 + 0.10 * (floor - 1)))if __name__ == "__main__":


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


if __name__ == "__main__":
    target = {
        "status": None,
        "statuses": {}
    }

    result = apply_status(target, "Poison", 1.0)

    print("Success:", result)
    print("Target:", target)



def classify(result):
    if result == "Weak":
        return "Weak"

    if result in ("Resist", "Strong"):
        return "Resist"

    return "Neutral"
