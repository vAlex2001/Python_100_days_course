import pandas
import statistics

data = pandas.read_csv("weather_data.csv")
#print(data)

# Transform the series into a dictionary
data_dict = data.to_dict()
#print(data_dict)

# Transform one entry from the dictionary into a list
temp_list = data["temp"].to_list()
#print(temp_list)

# Calculate the average temperature
avg_tmp = statistics.mean(temp_list)
#print(avg_tmp)

#print(data["temp"].mean())
#print(data["temp"].max())

#print(data.condition)

# Print certain row
#print(data[data.day == "Monday"])

# Print row with max temperature
#print(data[data.temp == data["temp"].max()])

# Get monday temp
# Print row with max temperature
monday = data[data.day == "Monday"]
#print(monday)

monday_temp = monday.temp[0]
print(monday_temp * 1.8 + 32)

# Create data frame from scratch
data_dict = {
    "students": ["A", "B", "C"],
    "scores": [1, 2, 3]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")