# List comprehension
numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name  = "Alex"
letter_list = [letter for letter in name]
print(letter_list)

new_list = [i*2 for i in range(1,5)]
print(new_list)

names = ["Alex", "Dorinel"]
short_names = [name for name in names if len(name) < 5]
print(short_names)