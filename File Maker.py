import csv

array = [["Assignment for: Mike", "Unit: Unit 20", "Due: 30/11/2018", "----------------"]]

with open("assignments.csv", "w") as db:
    writer = csv.writer(db, lineterminator = "\n")
    writer.writerows(array)
