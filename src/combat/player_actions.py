from ui import line, colorize, hp_bar, mp_bar
from ui import CYAN, BOLD
from combat.targeting import choose_enemy
def player_action(character, enemies, party, items, knowledge):
    if character.get("class") == "Lancer":
        character["mp"] = min(
            character["max_mp"],
            character["mp"] + 3
        )
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
    c = input("> ")
            if c == "1":
            e = choose_enemy(enemies)
            result = deal_attack(
                character, e, "Strike", 24, knowledge, "Basic Attack"
            )
            return classify(result), 1

        if c == "2":
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

        if c == "3":
            if battle_item_menu(character, party, items):
                return "Support", 1
            continue

        if c == "4":
            character["guarding"] = True
            print(f"{character['name']} guards.")
            return "Guard", 1

        if c == "5":
            e = choose_enemy(enemies)
            print(f"{e['name']}: {e['hp']}/{e['max_hp']} HP")

            known = knowledge.get(e["name"], {})

            if known:
                for affinity, result in known.items():
                    print(f"  {affinity}: {result}")
            else:
                print("No useful affinity information has been discovered.")

            continue

        if c == "6":
            return "Escape", 1

        print("Invalid choice.")
