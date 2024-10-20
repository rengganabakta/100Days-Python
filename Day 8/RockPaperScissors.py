rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user = int(input("1 = gunting, 2 = kertas, 3 = batu : "))
if user == 1:
    print(scissors)
elif user == 2:
    print(paper)
elif user == 3:
    print(rock)
else:
    print("Input eror")
    
comp = random.randint(1, 3)


    
if comp == 1:
    print(scissors)
elif comp == 2:
    print(paper)
elif comp == 3:
    print(rock)
else:
    print("Input eror")
    
if comp == 3 and user == 1:
    comp = -1
if user == 3 and comp == 1:
    user = -1
    
if user < comp:
    print("user won!")
elif user == comp:
    [print("draw")]
else:
    print("user lost")