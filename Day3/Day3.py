print("Welcome to the Python Pizza Deliveries!")

size  = input("What size pizza do you want ? Small, Medium, Large: ")

peperoni = input("Do you want pepperoni on your pizza? Yes or No: ")

extra_cheese = input("Do you want extra cheese ? Yes or No: ")

total_price = 0

size = str.lower(size)
peperoni = str.lower(peperoni)
extra_cheese = str.lower(extra_cheese)

if size == "small":
    total_price = 15
    if peperoni == "yes":
        total_price+=2
    if extra_cheese == "yes":
        total_price+=1
elif size == "medium":
    total_price = 20
    if peperoni == "yes":
        total_price+=3
    if extra_cheese == "yes":
        total_price+=1
elif size == "large":
    total_price = 25
    if peperoni == "yes":
        total_price+=3
    if extra_cheese == "yes":
        total_price+=1
        
        
print(total_price)
    