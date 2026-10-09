
import random

from data.classes import CLASSES
from config import MAGIC_AFFINITIES
from ui import (
    header, colorize, CYAN, BOLD, YELLOW, GREEN,
    MAGENTA, RED, WHITE, ITALIC
)
from combat.targeting import (
    choose_enemy, choose_character, alive_party, alive_enemies
)
from combat.helpers import (
    affinity_multiplier, apply_status, apply_buff,
    classify, record_knowledge
)
from combat.attacks import deal_attack
from systems.progression import unlocked_skills


def skill_menu(character):
    skills = unlocked_skills(character)
    header(f"{character['name']} - SKILLS", 64, "-")

    for i, s in enumerate(skills, 1):
        if s.get("mastered"):
            tag = f" [Mastered: {s['source']}]"
        elif s is character.get("inherited_skill"):
            tag = " [Inherited]"
        else:
            tag = ""

        hp_note = f" | {s['hp_cost']} HP" if s.get("hp_cost") else ""
        target = s.get("target", "enemy")

        print(
            f"{i}. {colorize(s['name'], YELLOW)}{tag} | "
            f"Lv {s['level']} | {s['affinity']} | "
            f"{s['cost']} MP{hp_note} | Target: {target}"
        )

    np_data = CLASSES[character["class"]]["noble_phantasm"]
    gauge = character.get("np_gauge", 0)
    ready = gauge >= 100
    np_tag = colorize("READY", GREEN + BOLD) if ready else f"{gauge}/100"

    print(
        f"N. {colorize(np_data['name'], MAGENTA + BOLD)} "
        f"[Noble Phantasm - {np_tag}]"
    )
    print("0. Back")

    while True:
        c = input("> ")

        if c == "0":
            return None

        if c.lower() == "n":
            if ready:
                return "NOBLE_PHANTASM"
            print("The Noble Phantasm isn't ready yet. Keep fighting.")
            continue

        if c.isdigit() and 1 <= int(c) <= len(skills):
            return skills[int(c) - 1]

        print("Invalid choice.")


def apply_offensive_effect(character, enemy, effect, knowledge):
    if effect is None:
        return

    bonus_dur = 1 if character["class"] == "Archer" else 0

    if effect == "poison":
        if apply_status(enemy, "Poison", 0.55, 2 + bonus_dur):
            print(colorize(f"{enemy['name']} is poisoned!", GREEN))

    elif effect == "burn":
        if apply_status(enemy, "Burn", 0.55, 2 + bonus_dur):
            print(colorize(f"{enemy['name']} is burning!", RED))

    elif effect == "freeze":
        if apply_status(enemy, "Frozen", 0.40, 1 + bonus_dur):
            print(colorize(f"{enemy['name']} is frozen solid!", CYAN))

    elif effect == "debuff_def":
        apply_buff(enemy, "DEF_DOWN", 0.30, 3)
        print(f"{enemy['name']}'s defence was lowered!")

    elif effect == "debuff_atk":
        apply_buff(enemy, "ATK_DOWN", 0.25, 3)
        print(f"{enemy['name']}'s attack was lowered!")

    elif effect == "multihit":
        hits = random.randint(1, 7)
        print(
            colorize(
                f"The strike lands {hits} additional time(s)!",
                MAGENTA
            )
        )

        for _ in range(hits):
            if enemy["hp"] <= 0:
                break

            deal_attack(
                character, enemy, "Slash", 12,
                knowledge, "Follow-up Strike"
            )


def apply_self_effect(character, skill):
    effect = skill.get("effect")

    if effect == "taunt":
        character["taunt"] = 2
        print(f"{character['name']} draws the enemy's attention!")

    elif effect == "evade_up":
        apply_buff(character, "EVADE_UP", 0.25, 3)
        print(f"{character['name']} becomes much harder to hit!")

    else:
        print(f"{character['name']} braces.")


def apply_support_effect(caster, target, skill, effect):
    if target is None:
        print("There was no valid target.")
        return

    if effect == "heal":
        amount = skill.get("power", 0) + caster["stats"]["MA"] * 2

        if caster.get("class") == "Rider":
            amount = int(amount * 1.20)

        target["hp"] = min(target["max_hp"], target["hp"] + amount)
        print(colorize(f"{target['name']} recovers {amount} HP.", GREEN))

    elif effect == "cure":
        target["status"] = None
        target["statuses"] = {}
        print(f"{target['name']}'s ailments are cured.")

    elif effect == "buff_def":
        apply_buff(target, "DEF_UP", 0.30, 3)
        print(f"{target['name']}'s defence rises.")

    elif effect == "buff_atk":
        apply_buff(target, "ATK_UP", 0.30, 3)
        print(f"{target['name']}'s attack rises.")

    elif effect == "miracle":
        amount = skill.get("power", 0) + caster["stats"]["MA"] * 2
        target["hp"] = min(target["max_hp"], target["hp"] + amount)
        target["status"] = None
        target["statuses"] = {}
        print(
            colorize(
                f"{target['name']} is fully restored and cured.",
                GREEN + BOLD
            )
        )


def process_skill(character, skill, party, enemies, knowledge):
    cost = skill["cost"]
    hp_cost = skill.get("hp_cost", 0)

    if (
        character.get("class") == "Caster"
        and cost > 0
        and not character.get("_free_cast_used", False)
    ):
        cost = 0
        character["_free_cast_used"] = True
        print(
            colorize(
                f"Territory Creation: the ground already belongs to "
                f"{character['name']}. No cost this cast.",
                CYAN
            )
        )

    if character["mp"] < cost:
        print("Not enough MP.")
        return None

    if hp_cost and character["hp"] <= hp_cost:
        print("Not enough HP to pay the life-force cost.")
        return None

    character["mp"] -= cost

    if hp_cost:
        character["hp"] -= hp_cost
        print(
            colorize(
                f"{character['name']} sacrifices {hp_cost} HP "
                f"to fuel {skill['name']}.",
                MAGENTA
            )
        )

    target_type = skill.get("target", "enemy")
    effect = skill.get("effect")

    if target_type == "enemy":
        e = choose_enemy(enemies)
        if e is None:
            return None

        power = skill["power"]

        if hp_cost and character["class"] == "Berserker":
            power = int(power * 1.25)

        result = deal_attack(
            character, e, skill["affinity"], power,
            knowledge, skill["name"]
        )
        apply_offensive_effect(character, e, effect, knowledge)
        return classify(result), 1

    if target_type == "all_enemies":
        worst = "Neutral"

        for e in alive_enemies(enemies):
            r = deal_attack(
                character, e, skill["affinity"],
                int(skill["power"] * 0.55),
                knowledge, skill["name"]
            )
            apply_offensive_effect(character, e, effect, knowledge)

            if r in ("Resist", "Strong"):
                worst = r
            elif r == "Weak" and worst == "Neutral":
                worst = "Weak"

        return classify(worst), 1

    if target_type == "self":
        apply_self_effect(character, skill)
        return "Support", 1

    if target_type == "ally":
        print("Choose a target:")
        target = choose_character(party)
        apply_support_effect(character, target, skill, effect)
        return "Support", 1

    if target_type == "party":
        for member in alive_party(party):
            apply_support_effect(character, member, skill, effect)

        print(f"{skill['name']} washes over the whole party.")
        return "Support", 1

    return "Support", 1


def execute_noble_phantasm(character, party, enemies, knowledge):
    cls = CLASSES[character["class"]]
    np_data = cls["noble_phantasm"]
    character["np_gauge"] = 0

    header("NOBLE PHANTASM", 60, "=")
    print(colorize(np_data["declaration"], ITALIC))
    print(colorize(f"\"{np_data['true_name']}\"", BOLD + YELLOW))
    print(
        f"{colorize(character['name'], CYAN + BOLD)}: "
        f"\"{np_data['name']}!\""
    )

    hp_cost = np_data.get("hp_cost", 0)

    if hp_cost:
        character["hp"] = max(1, character["hp"] - hp_cost)
        print(
            colorize(
                f"{character['name']} pays {hp_cost} HP "
                "to finish the invocation.",
                MAGENTA
            )
        )

    target_type = np_data.get("target", "enemy")
    effect = np_data.get("effect")

    if target_type == "enemy":
        e = choose_enemy(enemies)
        if e is None:
            return "Support", 1

        result = deal_attack(
            character, e, np_data["affinity"],
            np_data["power"], knowledge, np_data["name"]
        )
        apply_offensive_effect(character, e, effect, knowledge)
        return classify(result), 1

    if target_type == "all_enemies":
        worst = "Neutral"

        for e in alive_enemies(enemies):
            r = deal_attack(
                character, e, np_data["affinity"],
                int(np_data["power"] * 0.6),
                knowledge, np_data["name"]
            )
            apply_offensive_effect(character, e, effect, knowledge)

            if r in ("Resist", "Strong"):
                worst = r
            elif r == "Weak" and worst == "Neutral":
                worst = "Weak"

        return classify(worst), 1

    if target_type == "party":
        pseudo_skill = {
            "power": np_data["power"],
            "target": "ally"
        }

        for member in alive_party(party):
            apply_support_effect(
                character, member, pseudo_skill, effect or "heal"
            )

        return "Support", 1

    return "Support", 1
