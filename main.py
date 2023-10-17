
def add(a,b):
    result = a + b
    return result

def subtract(a,b):
    result = a - b
    return result

def multiply(a,b):
    result = a * b
    return result

def divide(a,b):
    if b!=0:
        result = a / b
        return result
    else:
        return "Error: Division by zero"    

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

addition_result = add(a, b)
subtraction_result = subtract(a, b)
multiplication_result = multiply(a, b)
division_result = divide(a, b)

print(f"Addition: {addition_result}")
print(f"Subtraction: {subtraction_result}")
print(f"Multiplication: {multiplication_result}")
print(f"Division: {division_result}")