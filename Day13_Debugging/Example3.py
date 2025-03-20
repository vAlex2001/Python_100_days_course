year = int(input("What's your year of birth? "))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
    
# Describe the Problem - Write your answers as comments:
# 1. What is the expected output?
# 2. What is the actual output?
# 3. What is the reason for the unexpected output?
# 4. What are your assumptions about the value of year ?

# Answer:
# 1. The expected output is "You are a millennial." if the year is between 1981 and 1993.
# 2. The actual output is nothing if the year is 1994.
# 3. The reason for the unexpected output is that the condition is not inclusive.
# 4. I assume that the value of year will never be 1994.

# Fix the code to avoid the unexpected output:
if year >= 1981 and year <= 1993:
    print("You are a millennial.")
elif year > 1993:
    print("You are a Gen Z.")
