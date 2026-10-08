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
if __name__ == "__main__":
    inventory = create_inventory()
    print(inventory)

def use_item(item_name, target):
    if item_name == "Medicine":
        target["hp"] = min(target["max_hp"], target["hp"] + 60)


    elif item_name == "Greater Medicine":
        target["hp"] = min(target["max_hp"], target["hp"] + 140)


    elif item_name == "Ether":
        target["mp"] = min(target["max_mp"], target["mp"] + 35)

    elif item_name == "Greater Ether":
        target["mp"] = min(target["max_mp"], target["mp"] + 80)

    elif item_name == "Panacea":
        target["status"] = None
        target["statuses"] = {}

    elif item_name == "Revival Bead":
        if target["hp"] > 0:
            return False

        target["hp"] = max(1, int(target["max_hp"] * 0.35))

    elif item_name == "Amrita":
        target["hp"] = min(target["max_hp"], target["hp"] + 100)
        target["mp"] = min(target["max_mp"], target["mp"] + 100)

    else:
        return False

    return True

if __name__ == "__main__":
    character = {
        "hp": 10,
        "max_hp": 100,
        "mp": 20,
        "max_mp": 50,
        "status": "Poison",
        "statuses": {"Poison": 2}
    }

    print("Before:", character)

    use_item("Panacea", character)

    print("After:", character)
def use_item(item_name, target):
    if item_name == "Medicine":
        target["hp"] = min(target["max_hp"], target["hp"] + 60)

    elif item_name == "Greater Medicine":
        target["hp"] = min(target["max_hp"], target["hp"] + 140)

    elif item_name == "Ether":
        target["mp"] = min(target["max_mp"], target["mp"] + 35)

    elif item_name == "Greater Ether":
        target["mp"] = min(target["max_mp"], target["mp"] + 80)

    elif item_name == "Panacea":
        target["status"] = None
        target["statuses"] = {}

    elif item_name == "Revival Bead":
        if target["hp"] > 0:
            return False

        target["hp"] = max(1, int(target["max_hp"] * 0.35))

    elif item_name == "Amrita":
        target["hp"] = min(target["max_hp"], target["hp"] + 100)
        target["mp"] = min(target["max_mp"], target["mp"] + 40)

    else:
        return False


if __name__ == "__main__":
    character = {
        "hp": 50,
        "max_hp": 100,
        "mp": 20,
        "max_mp": 50,
        "status": "Poison",
        "statuses": {"Poison": 2}
    }

    print("Before:", character)

    use_item("Medicine", character)

    print("After:", character)


def add_item(inventory, item_name, amount=1):
    if item_name not in inventory:
        return False

    inventory[item_name] += amount
    return True

def remove_item(inventory, item_name, amount=1):
    if item_name not in inventory:
        return False

    if inventory[item_name] < amount:
        return False

    inventory[item_name] -= amount
    return True
