students = [
    {"name": "Aayushi", "marks": 85},
    {"name": "Ravi", "marks": 92},
    {"name": "Jassi", "marks": 55},
    {"name": "Lata", "marks": 49},
    {"name": "Karanl", "marks": 34}
]

for i in students:
    status = "Pass"  if i ["marks"] >= 50  else "Fail"

    print(f"Name: {i ["name"]}, Marks: {i ["marks"]} = {status}")