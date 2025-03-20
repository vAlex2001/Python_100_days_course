from random import randint

dice_iamges = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(1,6)
print(dice_iamges[dice_num])

# This function will sometimes throw an IndexError.
# Describe the Problem - Write your answers as comments:
# 1. What is the expected output?
# 2. What is the actual output?
# 3. What is the reason for the IndexError?
# 4. What are your assumptions about the value of dice_num so you don't get an error ?

# Answer:
# 1. The expected output is a random number between 1 and 6.
# 2. The actual output is an IndexError, if the random number is 6.
# 3. The reason for the IndexError is that the list index is out of range.
# 4. I assume that the value of dice_num will never be 6.
# 5. List starts from 0, so the last index is 5. So, the value of dice_num should be between 0 and 5.

# Fix the code to avoid the IndexError:
dice_num = randint(0,5)
print(dice_iamges[dice_num]) 