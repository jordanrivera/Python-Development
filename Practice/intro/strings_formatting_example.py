age = 34
age_as_str = str(age)
print("You are" + age_as_str)
name = "Yordan"
print(f"How are you, {name}")
name1 = "Yordan"
greeting = f"How are you, {name1}?"
print(greeting)
final_greeting = "How are you, {}?"
yordan_greeting = final_greeting.format(name)
print(yordan_greeting)

name = "Bob"
bob_greeting = final_greeting.format(name)
print(bob_greeting)
loco = "Name"
adress = f""" Name: {loco} Street: {name}"""
print(adress)
description = "{} is {} years old."
print(description.format("Bob", 30))
description1 = "{} is {age} years old."
print(description1.format("Bob", age=30))


