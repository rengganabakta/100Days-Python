# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height**2)
if bmi > 35:
    con = "are clinically obese."
elif bmi > 30:
    con = "are obese."
elif bmi >= 25:
    con = "are slightly overweight."    
elif bmi > 18.5:
    con = "have a normal weight."
elif bmi < 18.5:
    con = "underweight."


    
print(f"Your BMI is {bmi}, you {con}")