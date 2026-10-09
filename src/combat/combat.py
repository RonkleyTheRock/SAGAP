import random

from config import INCAPACITATING_STATUSES
from ui import header, colorize, hp_bar, mp_bar, line
from ui import RED, GREEN, BOLD, DIM, CYAN
from combat.player_actions import player_action
from combat.enemy_actions import enemy_turn
from combat.effects import tick_effects

def alive_party(party):
    return [c for c in party if c["hp"] > 0]


def alive_enemies(enemies):
    return [e for e in enemies if e["hp"] > 0]


def affinity_multiplier(result):
    return {
        "Weak": 1.5,
        "Neutral": 1.0,
        "Resist": 0.5,
        "Strong": 0.25
    }.get(result, 1.0)


def scaled_stat(value, floor, difficulty):
    return max(
        1,
        int(value * difficulty * (1 + 0.10 * (floor - 1)))
    )


def apply_buff(target, name, value, turns):
    target.setdefault("buffs", {})[name] = {
        "value": value,
        "turns": turns
    }


def apply_status(target, status, chance, duration=2):
    if random.random() < chance:
        target["statuses"][status] = duration
        target["status"] = status
        return True

    return False


def classify(result):
    if result == "Weak":
        return "Weak"

    if result in ("Resist", "Strong"):
        return "Resist"

    return "Neutral"


def show_battle_status(enemies, party):
    header("BATTLE", 64, "=")

    for e in alive_enemies(enemies):
        print(colorize(e["name"], RED + BOLD))
        print(
            f"  HP {hp_bar(e['hp'], e['max_hp'])} "
            f"{e['hp']}/{e['max_hp']}"
        )

    line()

    for c in party:
        alive = c["hp"] > 0

        tag = colorize(
            c["name"],
            DIM if not alive else CYAN + BOLD
        )

        status = f" [{c['status']}]" if c.get("status") else ""

        print(
            f"{tag} Lv.{c['level']} "
            f"{c['class']}{status}"
        )

        if alive:
            print(
                f"  HP {hp_bar(c['hp'], c['max_hp'])} "
                f"{c['hp']}/{c['max_hp']}   "
                f"MP {mp_bar(c['mp'], c['max_mp'])} "
                f"{c['mp']}/{c['max_mp']}"
            )
        else:
            print("  DEFEATED")

    print("=" * 64)


def combat(party, enemies, items, knowledge, difficulty, boss=False):
    max_tokens = len(alive_party(party))

    header("COMBAT START", 64, "=")

    print(
        "Press-turn combat: weaknesses grant a bonus action, "
        "resisted hits cost two."
    )

    for c in party:
        c["_free_cast_used"] = False

    while alive_party(party) and alive_enemies(enemies):

        for c in party:
            c["guarding"] = False

        tokens = max_tokens

        show_battle_status(enemies, party)

        order = sorted(
            alive_party(party),
            key=lambda c: c["stats"]["AG"] + random.randint(0, 8),
            reverse=True
        )

        for character in order:

            if not alive_enemies(enemies) or not alive_party(party):
                break

            if character["hp"] <= 0:
                continue

            if any(
                character["statuses"].get(s, 0) > 0
                for s in INCAPACITATING_STATUSES
            ):
                print(
                    colorize(
                        f"{character['name']} cannot act!",
                        DIM
                    )
                )

                tokens = max(0, tokens - 1)
                continue

            result_tuple = player_action(
                character,
                enemies,
                party,
                items,
                knowledge
            )

            if result_tuple is None:
                continue

            result, cost = result_tuple

            if result == "Escape":
                chance = (
                    0.30
                    + sum(
                        c["stats"]["AG"]
                        for c in alive_party(party)
                    ) / 450
                )

                if random.random() < chance and not boss:
                    print("Escaped successfully!")
                    return True, "escaped"

                print("The escape attempt failed!")
                cost = 1

            if result == "Weak":
                tokens = min(
                    max_tokens + 1,
                    tokens + 1
                )

                print(
                    colorize(
                        "WEAKNESS! An extra action has been gained.",
                        GREEN + BOLD
                    )
                )

            elif result == "Resist":
                tokens = max(0, tokens - 2)

                print(
                    colorize(
                        "The attack was resisted. "
                        "Two actions were consumed.",
                        RED
                    )
                )

            else:
                tokens = max(0, tokens - cost)

            if tokens <= 0:
                break

        if not alive_enemies(enemies):
            break

        print(
            "\n" + colorize(
                "Enemy phase.",
                RED + BOLD
            )
        )

        for enemy in list(alive_enemies(enemies)):

            if enemy["hp"] <= 0:
                continue

            enemy_turn(enemy, party)

            if not alive_party(party):
                return False, "dead"

        tick_effects(party, enemies)

    if not alive_party(party):
        return False, "dead"

    return True, "win"
