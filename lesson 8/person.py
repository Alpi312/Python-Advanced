class Person:
    def __innit__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello i am {self.name},and i am {self.age} years old")

person1 = Person("Alp", 18)
person2 = Person("Alice", 17)

person1.greet()
person2.greet()