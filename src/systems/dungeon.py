import random

from config import ROOM_COUNT
from data.floors import FLOORS
from data.enemies import ENEMIES, FLOOR_ENEMY_POOL, MINIBOSSES
from combat.combat import combat
from ui import header, colorize, GREEN, RED, BOLD


def make_enemy(name, floor, difficulty):
    enemy = ENEMIES[name].copy()
    enemy["name"] = name
    enemy["max_hp"] = int(enemy["hp"] * difficulty * (1 + 0.10 * (floor - 1)))
    enemy["hp"] = enemy["max_hp"]
    enemy["damage"] = int(enemy["damage"] * difficulty)
    return enemy


def run_dungeon(party, difficulty, items):
    knowledge = {}

    for floor in range(1, 11):
        floor_data = FLOORS[floor]

        header(f"FLOOR {floor}: {floor_data['name']}")
        print(floor_data["description"])
        print(f"Theme: {floor_data['theme']}")

        for room in range(1, ROOM_COUNT + 1):
            print(f"\n--- Room {room}/{ROOM_COUNT} ---")
            event = random.choice(["battle", "battle", "item"])

            if event == "item":
                items["Medicine"] = items.get("Medicine", 0) + 1
                print(colorize("You found 1 Medicine!", GREEN))
                continue

            enemy_name = random.choice(FLOOR_ENEMY_POOL[floor])
            enemy = make_enemy(enemy_name, floor, difficulty)

            won, result = combat(
                party, [enemy], items, knowledge, difficulty
            )

            if not won:
                print(colorize("Your party has been defeated.", RED + BOLD))
                return False

        if floor in MINIBOSSES:
            print(f"\nThe floor's guardian appears: {floor_data['boss']}!")
            boss = MINIBOSSES[floor].copy()
            boss["max_hp"] = int(
                boss["hp"] * difficulty * (1 + 0.10 * (floor - 1))
            )
            boss["hp"] = boss["max_hp"]
            boss["damage"] = int(boss["damage"] * difficulty)

            won, result = combat(
                party, [boss], items, knowledge, difficulty, boss=True
            )

            if not won:
                print(colorize("The guardian defeated your party.", RED + BOLD))
                return False

    boss = ENEMIES.get("The Hollow Father")

    # The final boss is stored separately from regular enemies.
    from data.enemies import FINAL_BOSS

    final_boss = FINAL_BOSS.copy()
    final_boss["max_hp"] = int(
        final_boss["hp"] * difficulty * 1.9
    )
    final_boss["hp"] = final_boss["max_hp"]
    final_boss["damage"] = int(final_boss["damage"] * difficulty)

    header("THE FINAL BATTLE")
    won, result = combat(
        party, [final_boss], items, knowledge, difficulty, boss=True
    )

    if not won:
        print(colorize("The Hollow Father has defeated your party.", RED + BOLD))
        return False

    header("SAGAP: DEMO COMPLETE")
    print(colorize("You have defeated The Hollow Father.", GREEN + BOLD))
    return True