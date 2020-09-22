# slicing lists

friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]

print(friends[2:3])
# you can also use negative numbers
print(friends[-3:])

# list comprehensions
numbers = [0, 1, 2, 3, 4]
doubled_numbers = []

doubled_numbers = [number * 2 for number in numbers]
print(doubled_numbers)

friend_ages = [22, 31, 35, 37]
age_strings = [f"My friend is {age} years old." for age in friend_ages]
print(age_strings)
 # lower case iteration
names = ["Rolf", "Bob", "Jen"]
lower = [name.lower() for name in names]
print(lower)

friend = input("Enter your friend name: ")
friends1 = ["Rolf", "Bob", "Charlie", "Anne"]
friends_lower = [name.lower() for name in friends1]
if friend.lower() in friends_lower:
    friend_titlecased = friend.title()
    print(f"{friend_titlecased} is one of your friends.")
