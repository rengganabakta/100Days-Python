from Menu import MENU

def check_resource(coffee):
    """check apakah bahan bahan cukup untuk membuat kopi yang diinginkan"""
    user = MENU[coffee]["ingredients"]
    dispenser = MENU["dispenser"]["ingredients"]
    
    for ingredient, required_amount in user.items():
        if required_amount > dispenser.get(ingredient, 0):
            print(f"Not enough {ingredient}. Required: {required_amount}, Available: {dispenser.get(ingredient, 0)}\nbalik lagi nanti ya...")
            return False
        else:
            print(f"Enough {ingredient}. Required: {required_amount}, Available: {dispenser.get(ingredient, 0)}")
            
    return True
            
def take_money():
    """Input User Money"""
    print("Please Insert The Coin")
    
    penny = int(input("Penny : "))
    nikel = int(input("Nikel : "))
    dime = int(input(" Dime : "))
    cent = int(input(" Cent : "))
    
    total_money = float(penny*0.01 + dime*0.10 + nikel*0.05 + cent*0.25)
    return round(total_money, 2)

def check_money(coffee):
    """Check the money that user gave"""
    user_money = take_money()
    if MENU[coffee]["cost"] <= user_money:
        print(f"Uang di terima sebanyak {user_money}")
        return True, user_money
    else:
        print(f"Maaf uang anda belum cukup. anda perlu {round(( MENU[coffee]['cost'] - user_money ), 2)}$")
        return False, user_money
    
def make_coffee(money, coffee):
    print("Your Coffee is Served : ☕")
    print(f"Your change : {round(user_money - MENU[coffee]['cost'], 2)}")
    
    user_ingredients = MENU[coffee]["ingredients"]
    dispenser_ingredients = MENU["dispenser"]["ingredients"]

    for ingredient, required_amount in user_ingredients.items():
        if ingredient in dispenser_ingredients:
            dispenser_ingredients[ingredient] -= required_amount  # Deduct from dispenser
            print(f"Updated {ingredient} in dispenser: {dispenser_ingredients[ingredient]}")
        else:
            print(f"Ingredient {ingredient} not available in dispenser.")
         

print("Welcome to our coffee machine, select your coffe please\navalaible today is \nespresso \t: $1.50\nLatte \t\t: $2.50\nCappucino \t: $3.00\n\n")

user_selection = input(">> ")

match user_selection:
    case "espresso":
        coffee = "espresso"
    case "latte":
        coffee = "latte"
    case "cappuccino":
        coffee = "cappuccino"
        
IsEnoughIngredients = check_resource(coffee)
if IsEnoughIngredients == True:
    IsEnoughMoney, user_money = check_money(coffee)
    if IsEnoughMoney == True:
        make_coffee(user_money, coffee)
        