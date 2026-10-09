
from ui import line, colorize, hp_bar, mp_bar
from ui import CYAN, BOLD
from combat.targeting import choose_enemy
from combat.item_actions import battle_item_menu


def player_action(character, enemies, party, items, knowledge):
    if character.get("class") == "Lancer":
        character["mp"] = min(
            character["max_mp"],
            character["mp"] + 3
        )

    while True:
        line()
        print(
            f"{colorize(character['name'], CYAN + BOLD)}'s turn | "
            f"{character['class']} | "
            f"HP {hp_bar(character['hp'], character['max_hp'], 12)} "
            f"{character['hp']}/{character['max_hp']}  "
            f"MP {mp_bar(character['mp'], character['max_mp'], 12)} "
            f"{character['mp']}/{character['max_mp']}  "
            f"NP {character.get('np_gauge', 0)}/100"
        )

        print("1. Attack  2. Skill  3. Item  4. Guard  5. Analyse  6. Escape")
        choice = input("> ")

        if choice == "1":
            enemy = choose_enemy(enemies)
            if enemy is None:
                continue
            result = deal_attack(
                character, enemy, "Strike", 24,
                knowledge, "Basic Attack"
            )
            return classify(result), 1

        if choice == "2":
            skill = skill_menu(character)

            if skill is None:
                continue

            if skill == "NOBLE_PHANTASM":
                return execute_noble_phantasm(
                    character, party, enemies, knowledge
                )

            outcome = process_skill(
                character, skill, party, enemies, knowledge
            )

            if outcome is None:
                continue

            return outcome

        if choice == "3":
            if battle_item_menu(character, party, items):
                return "Support", 1
            continue

        if choice == "4":
            character["guarding"] = True
            print(f"{character['name']} guards.")
            return "Guard", 1

        if choice == "5":
            enemy = choose_enemy(enemies)
            if enemy is None:
                continue

            print(f"{enemy['name']}: {enemy['hp']}/{enemy['max_hp']} HP")
            known = knowledge.get(enemy["name"], {})

            if known:
                for affinity, result in known.items():
                    print(f"  {affinity}: {result}")
            else:
                print("No useful affinity information has been discovered.")

            continue

        if choice == "6":
            return "Escape", 1

        print("Invalid choice.")
