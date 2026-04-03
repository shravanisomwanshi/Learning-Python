class Employee:
    language = "py"  # this is a class attribute
    salary = 1200000

harry = Employee()
harry.name = "Harry"  # this is an object(instance) attribute
print(harry.name, harry.language, harry.salary) 

rohan = Employee()
rohan.name = "rohan roro robinson"
print(rohan.name, rohan.salary, rohan.language)

# here name is object(instance) attribute and salary and language
#  are class attributes as they directly belong to the class