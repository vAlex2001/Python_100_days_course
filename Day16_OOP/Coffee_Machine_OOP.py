from menu import Menu
from Coffee_Maker import CoffeeMaker
from Money_Machine import MoneyMachine

coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
machine_menu = Menu()

machine_on = True

while machine_on:
    options = machine_menu.get_items()
    
    choice = input(f"What would you like ({options}): ")
    
    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = machine_menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink.name)