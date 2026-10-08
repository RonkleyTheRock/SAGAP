def alive_party(party):
    return [c for c in party if c["hp"] > 0]

if __name__ == "__main__":
    party = [
        {"name": "Irety", "hp": 100},
        {"name": "Iyanu", "hp": 0},
        {"name": "Ayonikun", "hp": 50},
    ]

    print(alive_party(party))
