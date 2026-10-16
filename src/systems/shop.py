from data.items import ITEMS
from ui import clear_screen, header, pause

def shop(party, inventory):
    #Let the party buy healing and utility items using shared character gold.
    while True:
        clear_screen()
        header("TRAVELLING MERCHANT")
        gold = min((c.get("gold", 0) for c in party), default=0)
        print(f"Party funds (lowest character balance): {gold} gold")
        print("Items for sale:")
        for index, (name, data) in enumerate(ITEMS.items(), 1):
            print(f"{index}. {name} — {data['price']} gold — {data['description']}")
        print("0. Leave shop")
        choice = input("> ").strip()
        if choice == "0":
            return
        if not choice.isdigit() or not 1 <= int(choice) <= len(ITEMS):
            print("Choose a listed item or 0 to leave.")
            pause()
            continue
        name = list(ITEMS)[int(choice) - 1]
        price = ITEMS[name]["price"]
        amount_text = input("Quantity to buy (1-9, or 0 to cancel): ").strip()
        if not amount_text.isdigit() or not 0 <= int(amount_text) <= 9:
            print("Enter a quantity from 0 to 9.")
            pause()
            continue
        amount = int(amount_text)
        if amount == 0:
            continue
        cost = price * amount
        if any(c.get("gold", 0) < cost for c in party):
            print("Not every sibling has enough gold for this purchase.")
            pause()
            continue
        for character in party:
            character["gold"] = character.get("gold", 0) - cost
        inventory[name] = inventory.get(name, 0) + amount
        print(f"Bought {amount} {name}(s) for {cost} gold.")
        pause()
