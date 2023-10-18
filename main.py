
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

def exponentiation(a,b):
    result = a**b
    return result

def modulus(a, b):
    if a > 0 and b > 0:
        result = ((a/100)* b)
        return result
    else:
        return "Error: Both numbers should be positive for modulus operation"


def get_number(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a number.")
          
def get_user_input():              
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    return a, b

def display_results(a, b):
    print(f"Addition: {add(a, b)}")
    print(f"Subtraction: {subtract(a, b)}")
    print(f"Multiplication: {multiply(a, b)}")
    print(f"Division: {divide(a, b)}")
    print(f"Exponentiation: {exponentiation(a, b)}")
    print(f"Modulus: {modulus(a, b)}")

if __name__ == "__main__":
    a, b = get_user_input()
    display_results(a, b)