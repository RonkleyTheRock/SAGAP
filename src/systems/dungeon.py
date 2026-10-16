import random

from config import ROOM_COUNT
from data.floors import FLOORS
from data.enemies import ENEMIES, FLOOR_ENEMY_POOL, MINIBOSSES, FINAL_BOSS
from data.narrative import GUIDE_NAME, GUIDE_MOTHER_LINES, GUIDE_SELF_LINES, RIDDLES, LORE_FRAGMENTS
from combat.combat import combat
from systems.inventory import add_item
from systems.progression import level_up
from systems.shop import shop
from characters.character import change_classes
from ui import header, colorize, clear_screen, pause, GREEN, RED, BOLD, YELLOW

SIBLING_SCENES = {
    1: ("Irety", "If we stop now, I'll start thinking about what could happen. Keep moving.", "Iyanu", "You say that like being afraid is a choice we can just refuse to make."),
    2: ("Ayonikun", "The river has no current. It is due to some sort of external force.", "Iyanu", "That is either a very good observation or the beginning of a terrible day."),
    3: ("Iyanu", "I remember this table. Not this room, exactly. The way we used to argue over dinner.", "Irety", "You always took the chair with the loose leg. Your rocking back and forth was the most distracting thing in the world."),
    4: ("Irety", "I thought protecting you meant making every decision first.", "Ayonikun", "It mostly meant we never got to tell you when you were wrong."),
    5: ("Ayonikun", "Every road says it is the right one. Maybe choosing is just agreeing to regret the others.", "Iyanu", "That is a frighteningly grownup thing to say. Please never do it again."),
    6: ("Iyanu", "I keep thinking Mum left because she trusted us to follow.", "Irety", "Or because she thought we would not. Both are hard to forgive."),
    7: ("Ayonikun", "What if I finally get something wrong? What if that's all anyone remembers?", "Irety", "Then we'll remember the thousand times you got it right, too."),
    8: ("Iyanu", "A bargain that hides its price is not a bargain. It is a trap with manners.", "Ayonikun", "I hate when yo say smart sounding things. Really annoys me."),
    9: ("Irety", "When we find her, I don't know whether I'll shout or hug her.", "Iyanu", "You can do both. You've done both to me for less."),
    10: ("Ayonikun", "If that thing looks like Father, I don't know if I can fight it.", "Irety", "You won't have to do it alone. None of us will."),
}

def make_enemy(name, floor, difficulty):
    enemy = ENEMIES[name].copy()
    enemy["name"] = name
    enemy["max_hp"] = int(enemy["hp"] * difficulty * (1 + 0.10 * (floor - 1)))
    enemy["hp"] = enemy["max_hp"]
    enemy["damage"] = int(enemy["damage"] * difficulty)
    return enemy

def show_riddle(floor, solved_riddles):
    riddles = RIDDLES.get(floor, [])
    if not riddles or floor in solved_riddles:
        return False
    question, options, answer_index, success_text, failure_text = riddles[0]
    clear_screen()
    header("A RIDDLE IN THE LABYRINTH")
    print(question)
    for number, option in enumerate(options, 1):
        print(f"{number}. {option}")
    while True:
        choice = input("> ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            break
        print("Choose one of the listed answers.")
    if int(choice) - 1 == answer_index:
        print("\n" + colorize(success_text, GREEN))
        solved_riddles.add(floor)
    else:
        print("\n" + colorize(failure_text, YELLOW))
    pause()
    return True

def show_lore(floor, seen_lore):
    fragments = LORE_FRAGMENTS.get(floor, [])
    unseen = [fragment for fragment in fragments if fragment not in seen_lore]
    if not unseen:
        return False
    clear_screen()
    header("FOUND LORE")
    print(random.choice(unseen))
    seen_lore.add(unseen[0] if len(unseen) == 1 else next(f for f in unseen if f in LORE_FRAGMENTS[floor]))
    pause()
    return True

def show_guide(floor, seen_guide):
    if floor in seen_guide:
        return False
    clear_screen()
    header(GUIDE_NAME)
    print(GUIDE_MOTHER_LINES.get(floor, "The folded paper bird watches the passage ahead."))
    seen_guide.add(floor)
    pause()
    return True

def sibling_interaction(floor, bonds, seen_scenes):
    scene = SIBLING_SCENES.get(floor)
    if not scene or floor in seen_scenes:
        return False
    first_name, first_line, second_name, second_line = scene
    clear_screen()
    header("A MOMENT BETWEEN SIBLINGS")
    print(f"{first_name}: {first_line}")
    pause()
    clear_screen()
    header("A MOMENT BETWEEN SIBLINGS")
    print(f"{second_name}: {second_line}")
    print("\nHow do you respond?")
    print("1. Encourage them to be honest with each other.")
    print("2. Remind everyone to focus on finding Mother.")
    print("3. Let the conversation breathe without interrupting.")
    while True:
        choice = input("> ").strip()
        if choice in {"1", "2", "3"}:
            break
        print("Choose 1, 2 or 3.")
    if choice == "1":
        bonds[first_name] = bonds.get(first_name, 0) + 1
        bonds[second_name] = bonds.get(second_name, 0) + 1
        print("You gave them room to be honest. Both sibling bonds increased.")
    elif choice == "2":
        bonds["Irety"] = bonds.get("Irety", 0) + 1
        print("The group agrees to keep moving. Irety appreciates your resolve.")
    else:
        bonds[second_name] = bonds.get(second_name, 0) + 1
        print(f"{second_name} seems relieved that you listened.")
    seen_scenes.add(floor)
    pause()
    return True

def show_bonds(bonds):
    clear_screen()
    header("SOCIAL BONDS")
    print("Your choices shape how the siblings trust one another.")
    for name in ("Irety", "Iyanu", "Ayonikun"):
        score = bonds.get(name, 0)
        print(f"{name}: Bond {score} / 10")
    pause()

def adventurer_encounter(party, items):
    #A rare meeting with another explorer the player chooses the outcome.
    clear_screen()
    header("ANOTHER PARTY")
    print("Three exhausted adventurers block the passage. Their leader raises a hand.")
    print('"We are not looking for trouble. We are looking for a way out."')
    print("1. Trade supplies (gain 1 Ether, lose 10 gold per sibling)")
    print("2. Share encouragement (gain a small amount of sibling bond)")
    print("3. Challenge them to a sparring match")
    print("4. Leave peacefully")
    while True:
        choice = input("> ").strip()
        if choice in {"1", "2", "3", "4"}:
            break
        print("Choose 1, 2, 3 or 4.")
    if choice == "1":
        if all(c.get("gold", 0) >= 10 for c in party):
            for c in party:
                c["gold"] -= 10
            items["Ether"] = items.get("Ether", 0) + 1
            print("You exchange coins for an Ether.")
        else:
            print("You do not have enough gold to make the trade.")
    elif choice == "2":
        for c in party:
            c["xp"] = c.get("xp", 0) + 3
        print("The conversation steadies everyone's resolve. Each sibling gains 3 XP.")
    elif choice == "3":
        print("The sparring match begins!")
        rival = {"name": "Wayward Adventurer", "hp": 90, "max_hp": 90, "damage": 16,
                 "defence": 8, "xp": 18, "gold": 12, "affinities": {}}
        won, result = combat(party, [rival], items, {}, 1.0)
        if won and result == "win":
            for c in party:
                c["gold"] = c.get("gold", 0) + 12
            print("The adventurers congratulate you and leave 12 gold for each sibling.")
        elif not won:
            print("Your party was defeated during the sparring match.")
            pause()
            return False
    else:
        print("Both groups continue on their separate paths.")
    pause()
    return True

def exploration_services(party, items):
    while True:
        clear_screen()
        header("REST POINT")
        print("1. Visit the travelling merchant")
        print("2. Change a character's Class")
        print("3. View inherited and unlocked skills")
        print("4. Continue exploring")
        choice = input("> ").strip()
        if choice == "1":
            shop(party, items)
        elif choice == "2":
            clear_screen()
            header("CHANGE CLASS")
            for i, character in enumerate(party, 1):
                print(f"{i}. {character['name']} — {character['class']} (Level {character['level']})")
            target = input("Choose a character (1-3, or 0 to cancel): ").strip()
            if target == "0":
                continue
            if target in {"1", "2", "3"}:
                change_classes(party[int(target) - 1])
                pause()
            else:
                print("Invalid character.")
                pause()
        elif choice == "3":
            from systems.progression import unlocked_skills
            clear_screen()
            header("PARTY SKILLS")
            for character in party:
                print(f"\n{character['name']} — {character['class']}, Level {character['level']}")
                skills = unlocked_skills(character)
                if not skills:
                    print("No skills unlocked yet.")
                for skill in skills:
                    source = f" (inherited from {skill.get('source', 'a mastered class')})" if skill.get("mastered") or skill is character.get("inherited_skill") else ""
                    print(f"- {skill['name']}{source}")
            pause()
        elif choice == "4":
            return
        else:
            print("Choose a number from 1 to 4.")
            pause()

def make_boss(source, floor, difficulty):
    boss = source.copy()
    boss["max_hp"] = int(boss["hp"] * difficulty * (1 + 0.10 * (floor - 1)))
    boss["hp"] = boss["max_hp"]
    boss["damage"] = int(boss["damage"] * difficulty)
    return boss

def award_victory(party, enemy):
    xp = int(enemy.get("xp", 10))
    gold = int(enemy.get("gold", 5))
    clear_screen()
    header("VICTORY")
    print(f"Defeated: {enemy['name']}")
    print(f"Party earned {xp} XP and {gold} gold each.")
    for character in party:
        if character["hp"] > 0:
            character["gold"] = character.get("gold", 0) + gold
            level_up(character, xp)
    pause()

def run_dungeon(party, difficulty, items):
    knowledge = {}
    solved_riddles = set()
    seen_lore = set()
    seen_guide = set()
    seen_scenes = set()
    bonds = {"Irety": 0, "Iyanu": 0, "Ayonikun": 0}

    for floor in range(1, 11):
        floor_data = FLOORS[floor]
        clear_screen()
        header(f"FLOOR {floor}: {floor_data['name']}")
        print(floor_data["description"])
        print(f"Theme: {floor_data['theme']}")
        pause()
        show_guide(floor, seen_guide)

        # A single sibling scene on each floor avoids repetitive dialogue.
        sibling_interaction(floor, bonds, seen_scenes)
        clear_screen()
        header("EXPLORATION OPTIONS")
        print("1. Check your siblings' social bonds")
        print("2. Continue exploring")
        choice = input("> ").strip()
        if choice == "1":
            show_bonds(bonds)
        exploration_services(party, items)

        for room in range(1, ROOM_COUNT + 1):
            clear_screen()
            header(f"{floor_data['name']} — ROOM {room}/{ROOM_COUNT}")
            print("The corridor bends onward. You take a moment to inspect the way ahead.")
            pause()

            if room == 2 and floor in RIDDLES and floor not in solved_riddles:
                show_riddle(floor, solved_riddles)
                continue
            if room == 3 and floor in LORE_FRAGMENTS and floor not in seen_lore:
                show_lore(floor, seen_lore)
                continue

            event = random.choice(["battle", "battle", "item", "lore", "adventurer", "shop"])
            if event == "shop":
                shop(party, items)
                continue
            if event == "adventurer":
                if not adventurer_encounter(party, items):
                    clear_screen()
                    header("GAME OVER")
                    print("Your party has been defeated.")
                    pause()
                    return False
                continue
            if event == "item":
                add_item(items, "Medicine", 1)
                clear_screen()
                header("FOUND AN ITEM")
                print(colorize("You found 1 Medicine.", GREEN))
                pause()
                continue
            if event == "lore" and show_lore(floor, seen_lore):
                continue

            enemy_name = random.choice(FLOOR_ENEMY_POOL[floor])
            enemy = make_enemy(enemy_name, floor, difficulty)
            won, result = combat(party, [enemy], items, knowledge, difficulty)
            if not won:
                clear_screen()
                header("GAME OVER")
                print(colorize("Your party has been defeated in the labyrinth.", RED + BOLD))
                pause()
                return False
            if result == "win":
                award_victory(party, enemy)
            elif result == "escaped":
                clear_screen()
                print("You retreat from the encounter and continue exploring.")
                pause()

        if floor in MINIBOSSES:
            clear_screen()
            header("FLOOR GUARDIAN")
            print(f"The floor's guardian appears: {floor_data['boss']}!")
            pause()
            boss = make_boss(MINIBOSSES[floor], floor, difficulty)
            won, result = combat(party, [boss], items, knowledge, difficulty, boss=True)
            if not won:
                clear_screen()
                header("GAME OVER")
                print(colorize("The guardian defeated your party.", RED + BOLD))
                pause()
                return False
            if result == "win":
                award_victory(party, boss)

    final_boss = FINAL_BOSS.copy()
    final_boss["max_hp"] = int(final_boss["hp"] * difficulty * 1.9)
    final_boss["hp"] = final_boss["max_hp"]
    final_boss["damage"] = int(final_boss["damage"] * difficulty)
    clear_screen()
    header("THE FINAL BATTLE")
    print("The labyrinth's memories gather into the shape of your father.")
    print("Your mother came here seeking a way to undo death. Now you must learn what that choice cost.")
    pause()
    won, result = combat(party, [final_boss], items, knowledge, difficulty, boss=True)
    if not won:
        clear_screen()
        header("GAME OVER")
        print(colorize("The Hollow Father has defeated your party.", RED + BOLD))
        pause()
        return False
    if result == "win":
        award_victory(party, final_boss)
    clear_screen()
    header("SAGAP — THE JOURNEY'S END")
    print(colorize("You have defeated The Hollow Father.", GREEN + BOLD))
    print("The labyrinth falls silent. For the first time, it has nothing left to ask.")
    print("The siblings must now decide what to do with the truth they found.")
    pause()
    return True
