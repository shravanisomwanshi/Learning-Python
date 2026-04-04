class Employee:
    def __init__(self) -> None:
        print("constructor of employee")
    a = 1

class programmer(Employee):
    b = 2

class Manager(programmer):
    c = 3

o = Employee()
print(o.a) # prints the a attribute
# print(o,b)  # shows an error as there is no b attribure in Employee class

o = programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)
