class Person:
    def __init__(self,name,age):
        self.persons = []
        self.name = name
        self.__age = age
        print(f"person {name} with age: {age} created")

    def greet(self):
        print(f"hello {self.name} how you doin")

    def get_age(self):
        print(f'your age is {self.__age}')

    def set_age(self,age):
        self.__age = age
        print(f"age changed to {age}")
        return (self.name,self.__age)

per = Person("bob",45)
per.greet()
per.get_age()
per.set_age(55)
per.get_age()