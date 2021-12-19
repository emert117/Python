class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self): # for users
        return f"Name: {self.name} Age: {self.age}"

    def __repr__(self): # for developer or tools
        return f"<Person('{self.name}', {self.age})>"

bob = Person("Bob", 34) 
print(bob)