import csv
import json
import pandas as pd

with open('home_17.json') as f:
    dt = json.load(f)

with open('home_18.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    list_data = ['id', 'name', 'age']
    writer.writerow(list_data)
    for key, value in dt.items():
        writer.writerow([key] + value)

df = pd.read_csv("home_18.csv")
df["phone"] = [1232313, 123123123, 435345345, 35432323, 23354678, 456789765]
df.to_csv("home_18.csv", index=False)

