
flavor_prices = {
    "Vanilla": 2.0,
    "Chocolate": 2.5,
    "Strawberry": 3.0,
    "Mint": 2.8
}

topping_prices = {
    "Sprinkles": 0.5,
    "Chocolate Chips": 0.7,
    "Cherries": 0.6,
    "Nuts": 0.8
}

cone_prices = {
    "Waffle Cone": 1.0,
    "Sugar Cone": 0.8,
    "Cup": 0.5
}

def display_menu(items, category):
    print(f"\nAvailable {category}:")
    for i, (item, price) in enumerate(items.items(), start=1):
        print(f"{i}. {item} - ${price:.2f}")

def choose_flavor():
    global flavor_prices  # Access global variable
    display_menu(flavor_prices, "Flavors")
    choice = int(input("Choose a flavor (1-4): "))
    flavor = list(flavor_prices.keys())[choice - 1]
    price = flavor_prices[flavor]
    return flavor, price

def choose_toppings():
    global topping_prices  # Access global variable
    display_menu(topping_prices, "Toppings")
    total_topping_cost = 0
    while True:
        choice = int(input("Choose a topping (1-4) or 0 to finish: "))
        if choice == 0:
            break
        topping = list(topping_prices.keys())[choice - 1]
        total_topping_cost += topping_prices[topping]
    return total_topping_cost

def choose_cone():
    global cone_prices  # Access global variable
    display_menu(cone_prices, "Cones")
    choice = int(input("Choose a cone (1-3): "))
    cone = list(cone_prices.keys())[choice - 1]
    price = cone_prices[cone]
    return cone, price

def calculate_total(flavor_price, toppings_cost, cone_price):
    return flavor_price + toppings_cost + cone_price

def main():
    print("Welcome to the Ice Cream Shop!")
    flavor, flavor_price = choose_flavor()
    toppings_cost = choose_toppings()
    cone, cone_price = choose_cone()
    total_cost = calculate_total(flavor_price, toppings_cost, cone_price)
    print("\nYour Ice Cream Order:")
    print(f"Flavor: {flavor}")
    print(f"Toppings cost: ${toppings_cost:.2f}")
    print(f"Cone: {cone}")
    print(f"Total Cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
