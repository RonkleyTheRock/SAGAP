def alive_party(party):
    return [c for c in party if c["hp"] > 0]


def alive_enemies(enemies):
    return [e for e in enemies if e["hp"] > 0]


def choose_enemy(enemies):
    living = alive_enemies(enemies)

    if not living:
        return None

    for i, enemy in enumerate(living, 1):
        print(
            f"{i}. {enemy['name']} "
            f"HP {enemy['hp']}/{enemy['max_hp']}"
        )

    while True:
        choice = input("> ")

        if choice.isdigit() and 1 <= int(choice) <= len(living):
            return living[int(choice) - 1]

        print("Invalid target.")


def choose_character(party, include_dead=False):
    characters = party if include_dead else alive_party(party)

    if not characters:
        return None

    for i, character in enumerate(characters, 1):
        print(
            f"{i}. {character['name']} - "
            f"HP {character['hp']}/{character['max_hp']} "
            f"MP {character['mp']}/{character['max_mp']}"
        )

    while True:
        choice = input("> ")

        if choice.isdigit() and 1 <= int(choice) <= len(characters):
            return characters[int(choice) - 1]

        print("Invalid target.")
