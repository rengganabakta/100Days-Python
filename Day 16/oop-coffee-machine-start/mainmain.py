from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Buat instance dari CoffeeMaker
coffee_maker = CoffeeMaker()
menu = Menu()
payment = MoneyMachine()

all_items = menu.get_items()
turn_on = True

while turn_on == True:
    # memanggil menu
    print("Menu:")
    for each in all_items.split('/'):
        if each:  # Pastikan tidak mencetak string kosong
            drink = menu.find_drink(each)  # Mencari objek MenuItem
            if drink:
                print(f"\t{drink.name} for ${drink.cost}")

    #memanggil inputan
    user_input = input(">> ")
    #mencari minuman

    match user_input:
        
        case "report":
            coffee_maker.report()
        case "profit" :
            payment.report()
        case "OFF":
            print("Mesin mati")
            turn_on = False
            break 
        case _:
            drink = menu.find_drink(user_input)
            if drink and coffee_maker.is_resource_sufficient(drink):
                coffee_maker.make_coffee(drink)
            else:
                print("Sorry, that item is not available.")

    # Panggil metode report pada coffee_maker
    if coffee_maker.is_resource_sufficient(drink):
        if payment.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

    