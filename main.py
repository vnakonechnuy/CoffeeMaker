from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

flag = True

while flag:
    choose = input(f'What would you like? ({menu.get_items()}): ')

    if choose == 'off':
        break
    elif choose == 'report':
        coffeemaker.report()
        moneymachine.report()
        continue
    elif choose == 'fill':
        coffeemaker.fill()
        continue

    drink = menu.find_drink(choose)
    if drink:
        if coffeemaker.is_resource_sufficient(drink):
            if moneymachine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)
