import random

# Use a list instead of a set to allow duplicates
card = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

def generate_card():
    """Generate a random card value."""
    return random.choice(card)

def spill_card(comp, user):
    print(f"Bandar: {' and '.join(map(str, comp))} with total {sum(comp)}")
    print(f"You: {' and '.join(map(str, user))} with total {sum(user)}")

def calculate(comp, user):
    total_comp = sum(comp)
    total_user = sum(user)
    
    if total_user == 21:
        return True  # User wins
    elif total_user > 21:
        if 11 in user:  # Check for ace
            user.remove(11)
            user.append(1)
            total_user = sum(user)
            if total_user > 21:
                return False  # User loses
        else:
            return False  # User loses

    return total_user > total_comp and total_user <= 21

def add_card(player):
    player.append(generate_card())
    spill_card(comp, user)
    
def check(U_win):
    if sum(user) > 21:
        print("Comp wins (User bust)")
    elif sum(comp) > 21:
        print("User wins (Comp bust)")
    elif sum(user) > sum(comp):
        print("User wins")
    elif sum(user) < sum(comp):
        print("Comp wins")
    else:
        print("Draw")

def comp_play():
    while sum(comp) < 17:  # Typically, the dealer hits until they reach 17
        add_card(comp)
    spill_card(comp, user)

# Start game
comp = [generate_card(), generate_card()]
user = [generate_card(), generate_card()]

print("Welcome to Blackjack!")
spill_card(comp, user)

U_win = calculate(comp, user)

print("Wanna add more cards? (Y/N)")
input2 = input("==> ")
while input2.lower() == "y":
    add_card(user)
    U_win = calculate(comp, user)  # Update U_win after adding card
    print("Wanna add more cards? (Y/N)")
    input2 = input("==> ")

comp_play()
check(U_win)
