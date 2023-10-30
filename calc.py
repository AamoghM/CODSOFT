
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2
while True:
    print("Select Operation:")
    print("'add' for addition")
    print("'subtract' for subtraction")
    print("'multiply' for multiplication")
    print("'divide' for division")

    user_input = input(": ")
    
    if user_input == "exit":
        break   

    elif user_input in ("add", "subtract", "multiply", "divide"):
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        
        if user_input == "add":
            outcome = add(number1, number2)
        elif user_input == "subtract":
            outcome = subtract(number1, number2)
        elif user_input == "multiply":
            outcome = multiply(number1, number2)
        elif user_input == "divide":
            outcome = divide(number1, number2)
        print("Outcome: ", outcome)
    else:
        print("Invalid input.")
    user_input = input("Let's do next calculation? (yes/no): ")
    if user_input == "no":
          break

