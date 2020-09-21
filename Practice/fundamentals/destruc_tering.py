# destructuring excercise
# converting values of a tupel into different variables

currencies = 0.8, 1.2
usd, eur = currencies

# destructuring inside a for loop and list of tuples
friends = [("Rolf", 25), ("Anne", 37), ("Charlie", 31), ("Bob",22)]
for name, age in friends:
    print(f"{name} is {age} years old.")


