# Create empty dictionary
fruits = {}

# Add key-value pairs
fruits["apple"] = "green"

# Print dictionary
print(fruits)

# Print specific value
print(fruits["apple"])

# Create dictionary with key-value pairs
fruits = {
    "apple": "green",
    "banana": "yellow",
    "cherry": "red"
}

# Clear dictioanry
fruits.clear()
print(fruits)

# Loop through dictionary
for key in fruits:
    print(key)
    print(fruits[key])
    
    
# Nested list in dictionry
travel_log = {
    "France": ["Paris", "Lille"],
    "Germany": ["Stuttgart", "Berlin"]
}

# Print the nested dictionary
print(travel_log)

# Print one value
print(travel_log["France"][0])

# Nested dictionary in dictionry
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille"],
        "num_times_visited": 8,  
    },
    "Germany":{
        "cities_visited": ["Stuttgart", "Berlin"],
        "total_visits": 3  
    } 
}

print(travel_log["Germany"]["cities_visited"][1])