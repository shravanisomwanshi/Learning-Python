class Employee:
    company = "ITC"
    name = "default name"
    def show(self):
        print(f"Tha name of the employee is {self.name} and the company is {self.company}")


class Coder:
    language = "python"
    def printlanguages(self):
        print(f"out of all the languages here is your language: {self.language}")



class programmer(Employee, Coder):
    company = "ITC Infotech"
    def showlanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language") 
        

a = Employee()
b = programmer()

b.show()
b.printlanguages()
b.showlanguage()




