print("Welcome to the tip calculator." + "\n")

total = float(input("What was the totall bill ?" + "\n"))

tip = int(input("How much would you like to tip ?  10%, 12%, 15% ?" + "\n"))

persons = int(input("How many people to split the bill ?" + "\n"))

total_pay = (total + (total * tip / 100))
to_pay = round(total_pay / persons, 2)

print(f"Each person should pay: ${to_pay}")
