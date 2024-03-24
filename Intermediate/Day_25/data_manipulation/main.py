#
# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()
#
# print(data)


# import csv
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1].isnumeric():
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

# data = pandas.read_csv('weather_data.csv')
# print(data['temp'].mean())
# print(data['temp'].max())
# print(data.temp)
#
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])
#
# high_temp = data[data.temp == data.temp.max()]
# print(high_temp.condition)
#
# monday = data[data.day == 'Monday']
# print((monday.temp[0] * 9 / 5) + 32)

squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

df = squirrel_data.groupby('Primary Fur Color', as_index=False).size()
df.columns = ['Fur Color', 'Count']
df.to_csv('squirrel_count.csv')
print(df)
print(type(df))
