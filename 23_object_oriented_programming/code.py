class Student:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.grades = (1, 2, 3, 4)
    
    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("emre", "mert")
print(Student.average(student))
print(student.average())