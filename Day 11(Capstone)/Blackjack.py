import random

# Use a list instead of a set to allow duplicates
card = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


def generate_card():
    """generate 2 nilai acak yang dikembalikan satu per satu"""
    return random.choice(card)

def spill_card():
    print(f"bandar : {comp[1]} and X ")
    print(f"You : {' and '.join(map(str, user))} with total {sum(user)}")

def calculate(comp, user):
    user_win = False
    total_comp = comp[0] + comp [1]
    total_user = sum(user)
    
    if total_user == 21:
        user_win = True
        return user_win
    elif total_user > 21: # over 21 
        if user[0] == 11 or user[1] == 11: # have ace ?
            if (total_user - 10) > 21: # if the ACE == 1 Are they still above 21 ?
                 user_win = 0 # no == user lose
                 
comp = [generate_card(), generate_card()]
user = [generate_card(), generate_card()]

print("Welcome to black jack")
spill_card()

    

U_win = calculate(comp, user)

print("Wanna Add more Card ? (Y/N)")
input2 = input("==> ")
if input2 == "Y" or input2 == 'y':
    user.append(generate_card())
    spill_card()
    U_win = calculate(comp, user)
    
if U_win == True:
    print("user wins")
else:
    print("comp wins")