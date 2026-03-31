import csv

employees = [
    {"Name": "Shivani", "BasicSalary": 30000, "Bonus": 5000, "Deduction": 2000},
    {"Name": "Reshmi", "BasicSalary": 25000, "Bonus": 3000, "Deduction": 1500},
    {"Name": "Ramisha", "BasicSalary": 28000, "Bonus": 4000, "Deduction": 1000}
]

for emp in employees:
    emp["NetSalary"] = emp["BasicSalary"] + emp["Bonus"] - emp["Deduction"]

with open("employee1.csv", "w", newline="") as f:
    fieldnames = ["Name", "BasicSalary", "Bonus", "Deduction", "NetSalary"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(employees)

print("Employee data saved")

with open("employee1.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)