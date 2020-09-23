# zip function in python to create dictionary's

friends = ["Rolf", "Bob", "Jen","Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = zip(friends, time_since_seen)

print(long_timers)

# enumerate functions in python
friends1 = ["Rolf", "John", "Anna"]


for counter, friend in enumerate(friends1):
    print(counter)
    print(friend)
print(list(enumerate(friends1)))
print(dict(enumerate(friends1)))
