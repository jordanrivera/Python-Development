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

# comprehension with conditionals

ages = [22, 35, 27, 21, 20]
odds = [age for age in ages if age % 2 == 1]
print(odds)

friends = ["Rolf", "ruth", "charlie", "jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = set([f.lower() for f in friends])
guest_lower = set([g.lower() for g in guests])
present_friends = [
    name for name in guests if name.lower() in friends_lower
]
print(present_friends)

# dictionary comprehensions with nesteling
friends2 = ["Rolf", "ruth", "charlie", "Jen"]
guests2 = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends2_lower = {n.lower() for n in friends2}
guests2_lower = {n.lower() for n in guests2}
present2_friends = {name.title() for name in friends2_lower.intersection(guests2_lower)}
print(present2_friends)

# dictionary
friends3 = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = {
    friends3[i]:time_since_seen[i]
    for i in range(len(friends3))
    if time_since_seen[i] > 5
}
print(long_timers)

