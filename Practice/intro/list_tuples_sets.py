#   Lesson about Lists

friends = ["Rolf", "Bob", "Anne"]
friends.append("Jen")
print (friends)
print(friends[0])
print(friends[1])

friends1 = [["Rolf", 24], ["Bob", 30], ["Anne", 27]]
friends1.remove(["Anne", 27])
print(friends1)
print(friends1[0][0])
print(friends1[1][1])

friend2 = [
    ["Rolf", 24],
    ["Bob", 30],
    ["Anne", 27],
    ["Charlie", 37],
    ["Jen", 25],
    ["Adam", 29],
]
print(friend2)

# Lection about tupples

shorty_tuple = "Rolf", "Bob"
a_bit_clearer = ("rolf", "Bob")
tuple_in_list = [("Rolf", "Bob")]
not_a_tuple = "Rolf"
friends4 = ("Rolf", "Bob", "Anne")
friends4 = friends4 + ("Jen",)      # you cannot append an element like a list
print(friends4)

# Lection about sets
art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}

art_friends.add("Joko")      # add value to a set
art_friends.remove("Joko")  # remove value to a set

print(art_friends)
print(science_friends)
# difference value in sets
art_but_not_science = art_friends.difference(science_friends)
science_but_not_art = science_friends.difference(art_friends)
print(art_but_not_science)
print(science_but_not_art)
# not repeating values in a set
not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)
# same / repeating values in a set
art_and_science = art_friends.intersection(science_friends)
print(art_and_science)
# unite all values from two sets
all_friends = art_friends.union(science_friends)
print(all_friends)







