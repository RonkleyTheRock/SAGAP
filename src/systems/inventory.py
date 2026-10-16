from data.items import ITEMS

def create_inventory():
    return {
        "Medicine": 2,
        "Greater Medicine": 0,
        "Ether": 2,
        "Greater Ether": 0,
        "Panacea": 1,
        "Revival Bead": 0,
        "Smoke Bomb": 1,
        "Amrita": 0,
    }

def use_item(item_name, target):
    #Apply an item and return True only when its effect is valid.
    if item_name not in ITEMS or target is None:
        return False

    hp = target.get("hp", 0)
    max_hp = target.get("max_hp", 0)
    mp = target.get("mp", 0)
    max_mp = target.get("max_mp", 0)

    if item_name == "Medicine":
        if hp <= 0 or hp >= max_hp:
            return False
        target["hp"] = min(max_hp, hp + 60)

    elif item_name == "Greater Medicine":
        if hp <= 0 or hp >= max_hp:
            return False
        target["hp"] = min(max_hp, hp + 140)

    elif item_name == "Ether":
        if hp <= 0 or mp >= max_mp:
            return False
        target["mp"] = min(max_mp, mp + 35)

    elif item_name == "Greater Ether":
        if hp <= 0 or mp >= max_mp:
            return False
        target["mp"] = min(max_mp, mp + 80)

    elif item_name == "Panacea":
        statuses = target.get("statuses", {})
        if not statuses and not target.get("status"):
            return False
        target["status"] = None
        target["statuses"] = {}

    elif item_name == "Revival Bead":
        if hp > 0:
            return False
        target["hp"] = max(1, int(max_hp * 0.35))
        target["status"] = None
        target["statuses"] = {}

    elif item_name == "Amrita":
        if hp <= 0 or (hp >= max_hp and mp >= max_mp):
            return False
        target["hp"] = min(max_hp, hp + 100)
        target["mp"] = min(max_mp, mp + 40)

    else:
        return False

    return True

def add_item(inventory, item_name, amount=1):
    if item_name not in inventory or amount <= 0:
        return False
    inventory[item_name] += amount
    return True

def remove_item(inventory, item_name, amount=1):
    if item_name not in inventory or amount <= 0:
        return False
    if inventory[item_name] < amount:
        return False
    inventory[item_name] -= amount
    return True

def show_inventory(inventory):
    print("\nINVENTORY")
    for item_name, amount in inventory.items():
        print(f"{item_name}: x{amount}")
