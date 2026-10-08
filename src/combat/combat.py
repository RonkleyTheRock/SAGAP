import random

from ui import header, colorize, hp_bar, mp_bar, line
from ui import RED, BOLD, DIM, CYAN


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
        print(f"  HP {hp_bar(e['hp'], e['max_hp'])} {e['hp']}/{e['max_hp']}")

    line()

    for c in party:
        alive = c["hp"] > 0
        tag = colorize(c["name"], DIM if not alive else CYAN + BOLD)
        status = f" [{c['status']}]" if c.get("status") else ""

        print(f"{tag} Lv.{c['level']} {c['class']}{status}")

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
    print("Press-turn combat: weaknesses grant a bonus action, resisted hits cost two.")

    for c in party:
        c["_free_cast_used"] = False

    while alive_party(party) and alive_enemies(enemies):
        tokens = max_tokens

        for c in party:
            c["guarding"] = False

        show_battle_status(enemies, party)


if __name__ == "__main__":
    party = [
        {
            "name": "Irety",
            "hp": 100,
            "max_hp": 100,
            "mp": 25,
            "max_mp": 25,
            "level": 1,
            "class": "Saber",
            "status": None,
            "guarding": False,
            "_free_cast_used": False
        }
    ]

    enemies = [
        {
            "name": "Test Enemy",
            "hp": 80,
            "max_hp": 80
        }
    ]

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


if __name__ == "__main__":
    party = [
        {"name": "Irety", "hp": 0, "stats": {"AG": 15}},
        {"name": "Iyanu", "hp": 100, "stats": {"AG": 10}},
        {"name": "Ayonikun", "hp": 100, "stats": {"AG": 5}}
    ]

    enemies = [
        {"name": "Test Enemy", "hp": 100}
    ]

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

        print(character["name"], "gets a turn.")
