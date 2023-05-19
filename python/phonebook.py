import csv

with open("phonebook.csv", "a") as file:
    name = input("Enter name: ")
    number = input("Enter number: ")

    writer = csv.DictWriter(file, fieldnames=["name", "number"])
    writer.writerow({"name": name, "number": number})