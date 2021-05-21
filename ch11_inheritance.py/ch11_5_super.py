class Person:
    country = "india"
    company = "DigitalIindia"

    def __init__(self):     #constructor created... 
        print("initializing person...\n")

    def takeBreak(self):
        print("i am breathing...")

class Employee(Person):
    company = "Honda"

    
    def __init__(self):     #constructor created...
        super().__init__() 
        print("initializing employee...\n")

    def getSalary(self):
        print(f"salary is {self.salary}")

    def takeBreak(self):
        super().takeBreak()    # 'super' will print its super class "takeBreak()" first, then it will print its own "takeBreak
        print("i am an employee so i am lukily breating...")

class programmer(Employee):
    company = "fiverr"

    def __init__(self):     #constructor created... 
        super().__init__()
        print("initializing programmer...\n")

    def getSalary(self):
        print("no salary to programmer")

    def takeBreak(self):
        super().takeBreak()    # 'super' will print its super class "takeBreak()" first, then it will print its own "takeBreak"
        print("i am a programmer, i'm breathing++ ")
p = Person()
e = Employee()
pr = programmer()

p.takeBreak()
e.takeBreak()
pr.takeBreak()  


