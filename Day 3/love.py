print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

nama1 = str(len(name1))
nama2 = str(len(name2))

nama = int(nama1+nama2)

if nama < 10 or nama > 90 :
    print("Your score is {nama}, you go together like coke and mentos")
elif nama > 40 and nama < 50:
    print("Your score is *y*, you are alright together.")
