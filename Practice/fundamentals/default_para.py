# default parameter functions

def add(x, y=3):
    total = x + y
    return total


print(add(x=5, y=6))
# change the space between default parameters
print(1, 2, 3, 4, 5, sep=" - ")

default_y = 3


def add(x, y=default_y):
    total = x + y
    print(total)

add(2)

def hi():
    print("Hellop")
def greet():
    return "Hellok"
x = hi()
y = greet()



