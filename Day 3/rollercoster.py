print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if (height >= 120):
    if age > 18 :
        print("go ahead, dawg")
        bill = 12
    elif age > 12:
        print("go ahead, men")
        bill = 7
    elif age < 55 and age >45 :
        print("go ahead, gramps")
        bill = 0
    else:
        print("go ahead, kids")
        bill = 5
        
    print("do you what photo ?")
    yes = str(input())
    if yes == "yes":
        print("your bill is $", bill + 3)
    else:
        print("your bill is $")
else:
    print("cant go!")