import random

number = int(random.randint(0, 100))
trying = 0

        
print("Welcome, choose dificulity :")
input1 = input("easy/normal/hard\n")

match input1:
    case "easy":
        trying = 10
    case "normal":
        trying = 8
    case "hard":
        trying = 5
    case _:
        print("Invalid difficulty level. Defaulting to normal.")
        
for i in range(trying):
    guess = (int(input(f"{i + 1} guess is ? =>>  ")))
    if guess == number:
        print("You win")
        break
    elif guess > number:
        print("Lower...")
    elif guess < number:
        print("Higher...")
    
print("you lost the game")