import random

# Use a list instead of a set to allow duplicates
card = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


def generate_card():
    """generate 2 nilai acak yang dikembalikan satu per satu"""
    return random.choice(card)

def spill_card():
    print(f"bandar : {comp[0]} and X with total XX")
    print(f"You : {' and '.join(map(str, user))} with total {sum(user)}")

def calculate(comp, user):
    user_win = False
    total_comp = comp[0] + comp [1]
    total_user = sum(user)
    
    if total_user == 21:
        user_win = True
        return user_win
    elif total_user > 21: # over 21 
        if 11 in user: # have ace ?
            if (total_user - 10) > 21: # if the ACE == 1 Are they still above 21 ?
                 user_win = 0 # no == user lose
        else:
            return
    elif total_comp < total_user and total_user <= 21:
        return user_win == 0
    
    return user_win

def add_card(player):
    player.append(generate_card())
    spill_card()
    U_win = calculate(comp, user)
    
def check(U_win):
    if sum(user) == sum(comp):
        print("Draw")
    if U_win == True:
        print("user wins")
    else:
        print("comp wins")
        
def comp_play():
    while sum(comp) < sum(user):
        add_card(comp)
        calculate(comp, user)
    print(f"bandar : {' and '.join(map(str, comp))} with total {sum(comp)}")
    print(f"You : {' and '.join(map(str, user))} with total {sum(user)}")
        
comp = [generate_card(), generate_card()]
user = [generate_card(), generate_card()]

print("Welcome to black jack")
spill_card()

    

U_win = calculate(comp, user)

print("Wanna Add more Card ? (Y/N)")
input2 = input("==> ")
while input2 == "Y" or input2 == 'y':
    add_card(user)
    print("Wanna Add more Card ? (Y/N)")
    input2 = input("==> ")

comp_play()
check(U_win)