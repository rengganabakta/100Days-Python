#import random
#import data
import random
from data import data
import os

#welcome the user
print("Welcome to Higher or Lower games, please chose the right answer to continue your progress")

#give the Random case A and random case B
def generate_option():
    """Generate the value of the game"""
    a = random.choice(data)
    return a

def play():
    """Generate all the value of the game"""
    a = generate_option()
    b = generate_option()
    print("Which was the most famous ? (A/B)")
    print(f"A: {a['name']}, {a['country']} {a['description']} \n\tor\nB: {b['name']}, {b['country']} {b['description']}")
    return a, b

def compare_option(a, b, inputan):
    """Comparing the value with the input from the user"""
    user_input = inputan.lower()

    op1 = a['follower_count']
    op2 = b['follower_count']
    
    if user_input == "a" and op1 > op2:
        os.system('cls')
        print("Correct answer")
        print("")
        return True
    elif user_input == "b" and op2 > op1:
        os.system('cls')
        print("Correct answer")
        print("")
        return True
    else:
        print("\nWrong Answer")
        return False

lanjut = True
streak = 0
while lanjut is True:
    streak += 1
    print(f"your streak : {streak}")
    a, b = play()
    input_user = input("==> ")
    lanjut = compare_option(a, b, input_user)
    

#aks for the input A or B

# compare the answer Casevalue
#if right repeat If wrong break