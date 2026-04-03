class Employee:
    language = "python"  # this is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("good morning")    

harry = Employee()
harry.language = "Javascript"  # this is an object(instance) attribute
harry.getInfo()
harry.greet()
# Employee.getInfo(harry)
