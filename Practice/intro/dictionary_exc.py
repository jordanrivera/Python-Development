# Dictionary examples

friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
print(friend_ages["Rolf"])

# Add a value in to a dictionary or change a existing one
friend_ages["Bob"] = 20
friend_ages["Rolf"] = 25
print(friend_ages)
# A set in an Dictionary
friends = ({"name": "Rolf Smith", "age": 24},
          {"name": "Adam Wool", "age": 30},
          {"name": "Anne Pun", "age": 27})
print(friends)
# Printing a value from a dictionary
print(friends[0]['name'])
print(friends[1]['age'])

# converting data into a Dictionary
friends1 = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]
friends_ages = dict(friends1)
print(friends_ages)
