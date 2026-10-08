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


if __name__ == "__main__":
    enemies = [
        {"name": "Oni", "hp": 100},
        {"name": "Kappa", "hp": 0},
        {"name": "Yurei", "hp": 50},
    ]

    print(alive_enemies(enemies))


def affinity_multiplier(result):
    return {
        "Weak": 1.5,
        "Neutral": 1.0,
        "Resist": 0.5,
        "Strong": 0.25
    }.get(result, 1.0)


if __name__ == "__main__":
    print(affinity_multiplier("Weak"))
    print(affinity_multiplier("Neutral"))
    print(affinity_multiplier("Resist"))
    print(affinity_multiplier("Strong"))
