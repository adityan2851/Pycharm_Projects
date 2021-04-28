# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(row[1])
#
#     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # temp_list = data["temp"].to_list()
# # print(sum(temp_list)/len(temp_list))
#
# # print(data[data.temp == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# print((monday.temp * 9/5) + 32)

squirrels = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
Gray_count = len(squirrels[squirrels["Primary Fur Color"] == "Gray"])
Cinnamon_count = len(squirrels[squirrels["Primary Fur Color"] == "Cinnamon"])
Black_count = len(squirrels[squirrels["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color":["Gray", "Cinnamon", "Black"],
    "Count":[Gray_count, Cinnamon_count, Black_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_Count.csv")
