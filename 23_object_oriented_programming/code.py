class Student:
    def __init__(self, name):
        self.name = name
        self.grades = (1, 2, 3, 4)
    
    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("emre")
print(Student.average(student))
print(student.average())