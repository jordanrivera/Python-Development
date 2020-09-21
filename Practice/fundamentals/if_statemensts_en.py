# If statements

friend = "Rolf"
user_name = input("Enter your name: ")

if user_name == friend:
    print("Hello, friend")
else:
    print("Hello, stranger")
# Bool of a empty / string
name = input("Enter your name: ")
print(bool(name))
if name:
    print("We know your name")

# if statement iterate in an list
friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]

user_name = input("Enter your name: ")

if user_name in friends:
    print("Hello, friend")
elif user_name in family:
    print("Hello, family!")
else:
    print("I don't know you.")

