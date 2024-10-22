from Menu import MENU

def check_resource(coffee):
    """Check if there are enough ingredients to make the desired coffee."""
    user = MENU[coffee]["ingredients"]
    dispenser = MENU["dispenser"]["ingredients"]
    
    for ingredient, required_amount in user.items():
        if required_amount > dispenser.get(ingredient, 0):
            print(f"Not enough {ingredient}. Required: {required_amount}, Available: {dispenser.get(ingredient, 0)}\nCome back later...")
            return False
        else:
            print(f"Enough {ingredient}. Required: {required_amount}, Available: {dispenser.get(ingredient, 0)}")
            
    return True
            
def take_money():
    """Input user money."""
    print("Please Insert The Coin")
    
    penny = int(input("Penny : "))
    nikel = int(input("Nikel : "))
    dime = int(input("Dime : "))
    cent = int(input("Cent : "))
    
    total_money = float(penny * 0.01 + dime * 0.10 + nikel * 0.05 + cent * 0.25)
    return round(total_money, 2)

def check_money(coffee):
    """Check the money that user gave."""
    user_money = take_money()
    if MENU[coffee]["cost"] <= user_money:
        print(f"Money received: ${user_money}")
        return True, user_money
    else:
        print(f"Sorry, you need ${round((MENU[coffee]['cost'] - user_money), 2)} more.")
        return False, user_money
    
def make_coffee(money, coffee):
    print("Your Coffee is Served: ☕")
    print(f"Your change: ${round(money - MENU[coffee]['cost'], 2)}")
    
    user_ingredients = MENU[coffee]["ingredients"]
    dispenser_ingredients = MENU["dispenser"]["ingredients"]

    for ingredient, required_amount in user_ingredients.items():
        if ingredient in dispenser_ingredients:
            dispenser_ingredients[ingredient] -= required_amount  # Deduct from dispenser
            print(f"Updated {ingredient} in dispenser: {dispenser_ingredients[ingredient]}")
        else:
            print(f"Ingredient {ingredient} not available in dispenser.")
         
def report():
    """Generate a report of the ingredients in the dispenser."""
    print("Current ingredient levels in the dispenser:")
    for ingredient, amount in MENU["dispenser"]["ingredients"].items():
        print(f"{ingredient.capitalize()}: {amount}")

def main():
    print("Welcome to our coffee machine! Please select your coffee:\nAvailable today:\nEspresso: $1.50\nLatte: $2.50\nCappuccino: $3.00\n\n")

    user_selection = input(">> ").lower()

    coffee = None  # Initialize coffee variable
    match user_selection:
        case "espresso":
            coffee = "espresso"
        case "latte":
            coffee = "latte"
        case "cappuccino":
            coffee = "cappuccino"
        case "report":
            report()
            print()
            main()  # Restart the main function
            return  # Exit current call to avoid further execution
        case "off":
            print("Turning off the coffee machine.")
            return  # Exit the program
        case _:
            print("Invalid selection. Please try again.")
            main()  # Restart the main function
            return  # Exit current call

    if coffee:  # Check if coffee has been assigned a valid value
        is_enough_ingredients = check_resource(coffee)
        if is_enough_ingredients:
            is_enough_money, user_money = check_money(coffee)
            if is_enough_money:
                make_coffee(user_money, coffee)
    
    main()
    
main()
