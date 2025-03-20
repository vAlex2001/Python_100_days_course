def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it!")
            
            
my_function()

# Describe the Problem - Write your answers as comments:

# 1. What is the for loop doing ?
# 2. When is the function meant to print "You got it!" ?
# 3. What are your assumptions about the value of i ?

# Answer:
# 1. The for loop is iterating from 1 to 19.
# 2. The function is meant to print "You got it!" when i is equal to 20.
# 3. I assume that the value of i will never be equal to 20.

# Correct function to behave as expected:

def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it!")
            
            
my_function()



