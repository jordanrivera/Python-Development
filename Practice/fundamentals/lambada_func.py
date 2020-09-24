# lambda function in python
def divide(x, y):
    return x/ y

# same function with lambda
divide = lambda x, y: x / y

print(divide(15, 3))

# example for lambda function
average = lambda sequence: sum(sequence) / len(sequence)

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95,100)},
]
for student in students:
    print(average(student["grades"]))
