import random
from config import LEVELS, header, colorize, GREEN, RED, pause
from combat import combat, ENEMIES, MINI_BOSS
from combat import combat, ENEMIES

def run_dungeon(party, difficulty, items):
    for lvl in range(1, 6):
        level_data = LEVELS[lvl]
        header(f"{level_data['name']}")
        
        # Prototype Level 1-4 standard rooms
        if lvl < 5:
            for room in range(1, level_data["rooms"] + 1):
                print(f"\n--- Room {room}/{level_data['rooms']} ---")
                event = random.choice(["battle", "item"])
                
                if event == "battle":
                    enemy_type = random.choice(list(ENEMIES.keys()))
                    e_stats = ENEMIES[enemy_type].copy()
                    e_stats["hp"] = int(e_stats["hp"] * difficulty)
                    enemy = {"name": enemy_type, **e_stats}
                    
                    win = combat(party, [enemy], items)
                    if not win:
                        print(colorize("\nYour party has been defeated...", RED))
                        return False
                else:
                    items["Medicine"] = items.get("Medicine", 0) + 1
                    print(colorize("You found 1x Medicine on the ground!", GREEN))
                pause()
        
        # Prototype Level 5: Mini-Boss Chamber
        else:
            print("\nYou step into the chamber. A fierce presence blocks the way!")
            boss_stats = MINI_BOSS.copy()
            boss_stats["hp"] = int(boss_stats["hp"] * difficulty)
            boss = {"name": boss_stats["name"], **boss_stats}
            
            win = combat(party, [boss], items)
            if not win:
                print(colorize("\nThe Mini-Boss crushed your party...", RED))
                return False
            else:
                header("PROTOTYPE DEMO COMPLETE!")
                print(colorize("You defeated the Mini-Boss and completed the early prototype!", GREEN))
                return True
    return True
