#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

easy_password = ""

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# for i in range(nr_letters):
#     easy_password += random.choice(letters)
# for i in range(nr_symbols):
#     easy_password += random.choice(numbers)
# for i in range(nr_numbers):
#     easy_password += random.choice(symbols)
    
# print(f"The easy password is {easy_password}")
    
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_password = ""
password_chars = []

for i in range(nr_letters):
    password_chars.append(random.choice(letters))
for i in range(nr_symbols):
    password_chars.append(random.choice(numbers))
for i in range(nr_numbers):
    password_chars.append(random.choice(symbols))
    
random.shuffle(password_chars)

for i in password_chars:
    hard_password+=i

print(f"The hard password is {hard_password}")


