# iterate in to a dictionary

friends_ages = {"Rolf": 25, "Anne": 37, "Charlie": 31, "Bob": 22}

for name, age in friends_ages.items():
    print(f"{name} is {age} years old")

# break and continue the loop

cars = ["ok", "ok","ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Found faulty car, skipping...")
        continue
    print(f"This car is {status}.")
    print("Shipping new car to customer!")

for status in cars:
    if status == "faulty":
        print("This car is faluty")
        break
    print(f"This car is o{status}.")

# repeating loops with range
for i in range(20):
    print(i)

kid_ages = (3, 7, 12)
for age in kid_ages:
    print(f"I have a {age} year old kid.")

# Printing 1 to 100 including 100
# Instead of printing multiples 3 print fizz
# instead of printing multiples 5 print buzz

for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

