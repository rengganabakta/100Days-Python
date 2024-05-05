print("Welcome to the tip Calculator")
total = float(input("Whats was the total bill ? $"))
tip = float(input("how much tip u gave me ? "))
personne = int(input("For how many people ? "))

print(f"eack personnes should pay : ${round((total + ((tip * total)/100)) / personne, 2)}")

