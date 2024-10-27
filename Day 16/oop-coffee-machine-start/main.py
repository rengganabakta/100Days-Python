from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee = CoffeeMaker()
menu = Menu()
payment = MoneyMachine()

def main():
    print("Here the menu\n", menu.get_items())
    user_input = input(">> ")
    
    match user_input:
        case "report":
            coffee.report()
            main()
        case "profit":
            payment.report()
            main()
        case "OFF":
            print("Mechine OFF")
            return
        case _ :
            drink = menu.find_drink(user_input)
            if coffee.is_resource_sufficient(drink):
                money = payment.make_payment(drink.cost)
                if money is True:
                    coffee.make_coffee(drink)
                    
            main()
                    
main()
            
    