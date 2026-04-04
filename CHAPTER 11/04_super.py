class Employee:
    def __init__(self):
        print("constructor of employee")
    a = 1

class programmer(Employee):
    def __init__(self):
        print("constructor of employee")
    b = 2

class Manager(programmer):
     def __init__(self):
        super().__init__()
        print("constructor of Manager")
     c = 3

# o = Employee()
# print(o.a) # prints the a attribute
# # print(o,b)  # shows an error as there is no b attribure in Employee class

# o = programmer()
# print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)
