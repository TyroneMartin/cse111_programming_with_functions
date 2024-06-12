import csv 
with open('provinces.csv', 'r') as file:
    # csv_data = csv.reader(file)
    file.pop()
    file.pop(0)
    csv_data = csv.reader(file)

    # next(csv_data)
    for line in csv_data:        
        print(line)