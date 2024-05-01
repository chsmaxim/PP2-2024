import csv

filename = 'students.csv'

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        name, id, study_year, phone_number = row
       