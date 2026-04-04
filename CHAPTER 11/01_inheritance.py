class Employee:
    company = "ITC"
    def show(self):
        print(f"Tha name is {self.name} and the salary is {self.salary}")


# class programmer:
#     company = "ITC Infotech"
#     def show{self}:
#     print(f"The name is {self.name} and the salary is {self.salary}")

#     def showlanguage(self):
#         print(f"The name is (self.name) and he is good with {self.language} language") 


class programmer(Employee):
    company = "ITC Infotech"
    def showlanguage(self):
        print(f"The name is (self.name) and he is good with {self.language} language") 

a = Employee()
b = programmer()

print(a.company, b.company)


