# Object oriented exercise

my_student = {
    "name": "Rolf Smith",
    "grades": [70, 88, 90, 99],
    "average": None
}


def average_grade(student):
    return sum(student['grades']) / len(student['grades'])


class Student:
    def __init__(self, new_name, new_grade):
        self.name = new_name
        self.grade = new_grade

    def average(self):
        return sum(self.grade) / len(self.grade)


student_one = Student('Rolf Smith', [70, 88, 90, 99])
student_two = Student('Jose', [50, 60, 99, 100])

print(student_one.average())
print(Student.average(student_one))