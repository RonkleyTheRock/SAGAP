import random
from config import colorize, RED, GREEN, YELLOW, CYAN, MAGENTA, BOLD, DIM, header

ENEMIES = {
    "Yurei": {"hp": 70, "damage": 15, "defence": 5, "aff": {"Fire": "Weak", "Slash": "Resist"}},
    "Oni": {"hp": 110, "damage": 22, "defence": 10, "aff": {"Pierce": "Weak", "Strike": "Resist"}},
    "Kitsune": {"hp": 100, "damage": 25, "defence": 8, "aff": {"Ice": "Weak", "Fire": "Resist"}},
}

MINI_BOSS = {
    "name": "Onryo of the Lanterns (Mini-Boss)",
    "hp": 280, "damage": 32, "defence": 14,
    "aff": {"Fire": "Weak", "Slash": "Resist"}
}

def alive_party(party):
    return [c for c in party if c["hp"] > 0]

def alive_enemies(enemies):
    return [e for e in enemies if e["hp"] > 0]

def deal_attack(attacker, target, affinity, power):
    result = target["aff"].get(affinity, "Neutral")
    mult = 1.5 if result == "Weak" else (0.5 if result == "Resist" else 1.0)
    
    raw = power + (attacker["stats"]["MA"] * 2 if affinity in ["Fire", "Ice", "Light"] else attacker["stats"]["ST"] * 2)
    damage = max(1, int((raw - target["defence"]) * mult))
    
    target["hp"] = max(0, target["hp"] - damage)
    print(f"{attacker['name']} used {affinity} attack -> {target['name']} took {damage} damage!")
    
    if result != "Neutral":
        color = GREEN if result == "Weak" else RED
        print(colorize(f"Affinity Effect: {result}!", color))
    return result

def combat(party, enemies, items):
    header("COMBAT ENGAGED")
    while alive_party(party) and alive_enemies(enemies):
        # Player Turn
        for member in alive_party(party):
            if not alive_enemies(enemies):
                break
            
            print(f"\n{member['name']} ({member['class']}) - HP: {member['hp']}/{member['max_hp']} | MP: {member['mp']}/{member['max_mp']}")
            print("1. Skill/Attack  2. Medicine  3. Guard")
            c = input("> ")
            
            if c == "1":
                skill = member["skills"][0]
                target = alive_enemies(enemies)[0]
                
                if skill.get("effect") == "heal":
                    print("Choose ally to heal:")
                    for i, ally in enumerate(party, 1):
                        print(f"{i}. {ally['name']} ({ally['hp']}/{ally['max_hp']} HP)")
                    ally_c = input("> ")
                    if ally_c.isdigit() and 1 <= int(ally_c) <= len(party):
                        healed = party[int(ally_c)-1]
                        healed["hp"] = min(healed["max_hp"], healed["hp"] + skill["power"])
                        print(f"{healed['name']} was healed for {skill['power']} HP!")
                else:
                    deal_attack(member, target, skill["affinity"], skill["power"])
                    if target["hp"] == 0:
                        print(colorize(f"{target['name']} was defeated!", RED))
            
            elif c == "2":
                if items.get("Medicine", 0) > 0:
                    items["Medicine"] -= 1
                    member["hp"] = min(member["max_hp"], member["hp"] + 60)
                    print(f"Used Medicine! {member['name']} recovered 60 HP. Remaining Medicine: {items['Medicine']}")
                else:
                    print("No Medicine left!")
            elif c == "3":
                member["guarding"] = True
                print(f"{member['name']} guards!")

        # Enemy Turn
        for enemy in alive_enemies(enemies):
            target = random.choice(alive_party(party))
            damage = max(1, enemy["damage"] - target["stats"]["EN"])
            if target.get("guarding"):
                damage = damage // 2
                target["guarding"] = False
                
            target["hp"] = max(0, target["hp"] - damage)
            print(f"{enemy['name']} attacked {target['name']} for {damage} damage!")
            if target["hp"] == 0:
                print(colorize(f"{target['name']} has fallen!", RED + BOLD))

    return len(alive_party(party)) > 0
