age = 20
is_over_age = age >= 18
is_under_age = age <= 18
is_twenty = age == 20
print(is_over_age)

my_number = 5
user_number = int(input("Enter a number: "))

matches = my_number == user_number
print(f"You got it right: {matches}.")

age = int(input("Enter your age: "))
can_learn_programming = age > 0 and age < 150
print(f"you can learn programming: {can_learn_programming}.")

age = int(input("Enter your age: "))
usually_working = age < 18 or age > 65
print(f"At {age}, you are usually working: {usually_working}.")

print(bool(35))
print(bool(""))


