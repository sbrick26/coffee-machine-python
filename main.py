from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == 'off':
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        item_chosen = menu.find_drink(choice)
        is_sufficient = coffee_maker.is_resource_sufficient(item_chosen)
        if is_sufficient:
            payment_verify = money_machine.make_payment(item_chosen.cost)
            if payment_verify:
                coffee_maker.make_coffee(item_chosen)
        