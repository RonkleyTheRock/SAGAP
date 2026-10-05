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
