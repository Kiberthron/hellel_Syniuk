import csv

def new_data():
   en_name = input("Name: ")
   name = en_name.split()
   en_surname = input("Surname: ")
   surname = en_surname.split()
   en_age = input("Age: ")
   age = en_age.split()
   en_birth = input("Brith: ")
   birth = en_birth.split()
   en_death = input("Death: ")

   death = en_death.split()
   list_data = surname + name + age + birth + death
   with open('db.csv', 'a') as csvfile:
       writer = csv.writer(csvfile)
       writer.writerow(list_data)















new_data()
