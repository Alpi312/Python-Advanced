class Student:
    school_name = "Digital school"

    def __innit__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

student_1 =Student("Alpi",18,"DS")
print(student_1.course)