
import random


def affinity_multiplier(result):
    return {
        "Weak": 1.5,
        "Neutral": 1.0,
        "Resist": 0.5,
        "Strong": 0.25,
    }.get(result, 1.0)


def apply_buff(target, name, value, turns):
    target.setdefault("buffs", {})[name] = {
        "value": value,
        "turns": turns,
    }


def apply_status(target, status, chance, duration=2):
    if random.random() < chance:
        target.setdefault("statuses", {})[status] = duration
        target["status"] = status
        return True
    return False


def classify(result):
    if result == "Weak":
        return "Weak"
    if result in ("Resist", "Strong"):
        return "Resist"
    return "Neutral"


def record_knowledge(knowledge, enemy, affinity, result):
    knowledge.setdefault(enemy, {})[affinity] = result

