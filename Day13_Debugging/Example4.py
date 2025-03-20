try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid age.")
    age = int(input("Enter your age: "))
    
if age < 18:
    print("You are a minor.")
elif age >= 18:
    print(f"You can drive at age {age}.")