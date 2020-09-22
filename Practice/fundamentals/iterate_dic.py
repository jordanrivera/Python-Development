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
    

