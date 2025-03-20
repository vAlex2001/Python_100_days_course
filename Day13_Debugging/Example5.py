import random

def add(num1, num2):
    return num1 + num2

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1,3)
        new_item = add(new_item, item)
    b_list.append(new_item)
    print(b_list)
    
mutate([1,2,3,5,8,13])
    
    
# Questions:
# 1. What is the expected output ?
# 2. Is the code behaving as expected ?

# Answer:
# 1. A list with 6 elements.
# 2. No, just on item is in the final list.

# Fix : move the "append" instruction inside the for Loop.

def correct_mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1,3)
        new_item = add(new_item, item)
        b_list.append(new_item)
    print(b_list)
    
correct_mutate([1,2,3,5,8,13])
    