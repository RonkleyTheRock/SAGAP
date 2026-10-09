def choose_enemy(enemies):
    living = [enemy for enemy in enemies if enemy["hp"] > 0]

    if not living:
        return None

    print("\nChoose an enemy:")

    for i, enemy in enumerate(living, 1):
        print(
            f"{i}. {enemy['name']} "
            f"({enemy['hp']}/{enemy['max_hp']} HP)"
        )

    while True:
        choice = input("> ")

        if choice.isdigit() and 1 <= int(choice) <= len(living):
            return living[int(choice) - 1]

        print("Invalid choice.")
if __name__ == "__main__":
    enemies = [
        {"name": "Yurei", "hp": 20, "max_hp": 20},
        {"name": "Kappa", "hp": 0, "max_hp": 15},
    ]

    target = choose_enemy(enemies)
    print("Selected:", target["name"])
