key = "world"
guess = [False] * len(key)
health = 6

def guess(health):
    user = input("= ").lower()

    for i, word in enumerate(key):
        if word == user:
            guess[i] = True
            show()
            return health

    health -= 1
    print(health)
    return health

def show():
    for i, letter in enumerate(key):
        if guess[i]:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()  # To ensure the output is on a new line after printing all characters

def main():
    global health
    while health > 0 and guess != [True] * len(key):
        health = guess(health)
        print("health =",health)

show()
print("")
main()
show()