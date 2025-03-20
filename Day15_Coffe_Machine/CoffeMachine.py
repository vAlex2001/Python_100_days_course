# Import the Art logo from Art.py
import Art

profit = 0

def calculate_inserted_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    
    return total
    

def try_prepare_coffee(coffee_type):
    global profit  # Allow modification of the global profit variable

    if coffee_type not in Menu.MENU:
        print("Invalid coffee type.")
        return
    
    ingredients = Menu.MENU[coffee_type]["ingredients"]
    
    # Check if resources are sufficient
    for item, amount in ingredients.items():
        if Menu.Resources.get(item, 0) < amount:
            print(f"Sorry, there is not enough {item}.")
            return
    
    total = calculate_inserted_money()
    
    cost = Menu.MENU[coffee_type]["cost"]
    
    if total >= cost:
        change = round(total - cost, 2)
        print(f"Here is your {coffee_type} ☕️. Enjoy!")
        
        # Deduct ingredients from resources
        for item, amount in ingredients.items():
            Menu.Resources[item] -= amount
        
        # Update money in resources and global profit
        Menu.Resources["money"] += cost
        profit += cost  # Update global profit

        if change > 0:
            print(f"Here is ${change} in change.")
    else:
        print("Sorry, that's not enough money. Money refunded.")

# Print the logo
print(Art.Logo)

# Import the menu resources from Menu.py
import Menu

on = True

while on:
    # Ask the user for input and print the available types of coffe
    user_input = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    
    # If the user input is "off" the machine will turn off
    if user_input == "off":
        on = False
    # If the user input is "report" the machine will print the resources
    elif user_input == "report":
        print(f"Water: {Menu.Resources['water']} ml.")
        print(f"Milk: {Menu.Resources['milk']} ml.")
        print(f"Coffee: {Menu.Resources['coffee']} g.")
        print(f"Money: {Menu.Resources['money']} .$")
        print(f"Profit: {profit} .$")
    
    # If the user input is "espresso" the machine will check if there are enough resources to make the coffee
    elif user_input == "espresso":
        try_prepare_coffee('espresso')
    # If the user input is "latte" the machine will check if there are enough resources to make the coffee
    elif user_input == "latte":
        try_prepare_coffee('latte')
    # If the user input is "cappuccino" the machine will check if there are enough resources to make the coffee
    elif user_input == "cappuccino":
        try_prepare_coffee('cappuccino')
    # If the user input is not valid the machine will print an error message
    else:
        print("Invalid input. Please try again.")