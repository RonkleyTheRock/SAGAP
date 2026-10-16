from ui import colorize, RED, BOLD


def tick_effects(party, enemies):
    for group in (party, enemies):
        for c in group:
            if c.get("hp", 0) <= 0:
                continue

            for status in list(c.get("statuses", {})):
                if status == "Poison":
                    dmg = max(1, int(c["max_hp"] * 0.06))
                    c["hp"] -= dmg
                    print(f"{c['name']} suffers {dmg} poison damage.")

                elif status == "Burn":
                    dmg = max(1, int(c["max_hp"] * 0.09))
                    c["hp"] -= dmg
                    print(f"{c['name']} is scorched for {dmg} damage.")

                c["statuses"][status] -= 1

                if c["statuses"][status] <= 0:
                    del c["statuses"][status]

                    if c.get("status") == status:
                        c["status"] = None

            for buff in list(c.get("buffs", {})):
                c["buffs"][buff]["turns"] -= 1

                if c["buffs"][buff]["turns"] <= 0:
                    del c["buffs"][buff]

            if c.get("taunt", 0) > 0:
                c["taunt"] -= 1

            if c["hp"] <= 0:
                c["hp"] = 0
                print(
                    colorize(
                        f"{c['name']} succumbs to their wounds!",
                        RED + BOLD
                    )
                )
