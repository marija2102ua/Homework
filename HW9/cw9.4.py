class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__info = f"{self.name}s age is {self.age}"
    @property
    def info(self):
        return self.__info