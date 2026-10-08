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


if __name__ == "__main__":
    print(scaled_stat(100, 3, 1.15))
   
