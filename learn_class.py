
""" 
        Create a class named Person, use the __init__() function to assign values for fistName , lastName and age:
 """
class Student:
    def __init__(self, firstName,lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
    def __str__(self):
        return f"{self.firstName} {self.lastName} {self.age}"
    def hello(self):
        print(f"Hello {self.firstName}")

sharmake = Student("Sharmake", "Ibrahim", 23)


sharmake.hello()