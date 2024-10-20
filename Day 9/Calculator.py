def operation(operation, a, b):
    match operation:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b

def ambil_bilangan():
    a = int(input("==>> "))  
    return a

print("welcome to simple calculator \nplease enter your math operation (+, -, /, *)")
operation_input = input("=>> ")

print("Bilangan pertama")
a = ambil_bilangan()
print("Bilangan Kedua")
b = ambil_bilangan()

print(f"hasil ={operation(operation_input, a, b)}")

