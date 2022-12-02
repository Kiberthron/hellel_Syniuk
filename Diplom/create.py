import csv

def create():
    with open('db.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        header_data = ['surname', 'name', 'age', 'birth', 'death']
        writer.writerow(header_data)


create()



