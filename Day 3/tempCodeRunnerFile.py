print("The Love Calculator is calculating your score...")
name1 = "arengga" # What is your name?
name2 = "anastia" # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

nama = name1 + name2
lower = nama.lower

t = lower.count("t")
r = lower.count("r")
u = lower.count("u")
e = lower.count("e")

first = t + r + u + e

l = lower.count("l")
o = lower.count("o")
v = lower.count("v")
e2 = lower.count("e")

second = l + o + v + e

comb = str(first) + str(second)
final = int(comb)

if final < 10 or final > 90:
    print("Your score is {final}, you go together like coke and mentos")
elif final > 40 and final < 50:
    print("Your score is {final}, you are alright together.")
else:
    print("Your score is {final}.")

