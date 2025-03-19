import Logo

# Define addition
def sum(num1, num2):
    return num1 + num2

# Define subtraction
def subtract(num1, num2):
    return num1 - num2

# Define multiplication
def multiplication(num1, num2):
    return num1 * num2

# Define division
def division(num1, num2):
    return num1 / num2

print (Logo.logo)


math_operations = {
    "+": sum,
    "-": subtract,
    "*": multiplication,
    "/": division
}


def calculator():
    stop = True
    first_number = input("Enter the first number: ")
    print("\n")

    while stop:
        operation = input("Pick an operation {+, -, *, /}: ")
        print("\n")
        second_number = input("Enter the second number: ")
        result = math_operations[operation](float(first_number), float(second_number))
        print(f"{first_number} {operation} {second_number} = {result}")
        
        answer = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or 'exit' to stop: ")
        
        if answer == "y":
            first_number = result
        elif answer == "n":
            stop = False
            print("\033[H\033[J")
            calculator()
        elif answer == "exit":
            stop = False
            print("Goodbye!")
            
calculator()  