class Employee:
    company = "Google"

    def showDetails(self):
        print("this is an employee")

class Programmer(Employee):
    language = "Python"
    # company = "Youtube"

    def getLanguage(self):
        print(f"the language is {self.language}")

    def showDetails(self):
        print("this is a programmer")

e=Employee()
e.showDetails()
p=Programmer()
p.showDetails()
print(p.company)