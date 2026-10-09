def tick_effects(party, enemies):
    """Update active status effects and buffs after a combat round."""

    for target in party + enemies:
        statuses = target.setdefault("statuses", {})
        buffs = target.setdefault("buffs", {})

        for status in list(statuses):
            statuses[status] -= 1

            if statuses[status] <= 0:
                del statuses[status]

        for buff in list(buffs):
            buffs[buff]["turns"] -= 1

            if buffs[buff]["turns"] <= 0:
                del buffs[buff]

        if target.get("status") not in statuses:
            target["status"] = next(iter(statuses), None)
