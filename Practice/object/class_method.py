class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


rolf = Student('Rolf', 'MIT')

rolf.marks.append(78)
rolf.marks.append(99)

print(rolf.average())


class Foo:
    @classmethod
    def hi(cuca):
        print(cuca.__name__)


my_object = Foo()
my_object.hi()


class Bar:
    @staticmethod
    def hi():
        print("Hello, i don\'t take parameters.")


another_object = Bar()
another_object.hi()




