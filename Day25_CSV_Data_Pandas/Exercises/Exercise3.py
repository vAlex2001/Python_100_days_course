import pandas

data = pandas.read_csv("Squirrel.csv")

grey_fur_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_fur_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_fur_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur color": ["Gray", "Black", "Cinnamon"],
    "Count": [grey_fur_squirrels_count, black_fur_squirrels_count, cinnamon_fur_squirrels_count]
}

df = pandas.DataFrame(data_dict)

df.to_csv("Squirrel_Short_Info.csv")