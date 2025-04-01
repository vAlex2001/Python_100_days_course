<<<<<<< HEAD
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
        
    print (temperatures)
    
import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
=======
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
        
    print (temperatures)
    
import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
>>>>>>> 8e6fd66c9ea75f5b66df0705ab2618bd06383890
print(data["temp"])