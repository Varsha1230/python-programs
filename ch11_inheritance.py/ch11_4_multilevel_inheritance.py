class Person:
    country = "india"
    company = "DigitalIindia"
    
    def takeBreak(self):
        print("i am breathing...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"salary is {self.salary}")

    def takeBreak(self):
        print("i am an employee so i am lukily breating...")

class programmer(Employee):
    company = "fiverr"

    def getSalary(self):
        print("no salary to programmer")

    def takeBreak(self):
        print("i am a programmer, i'm breathing++ ")
p = Person()
e = Employee()
pr = programmer()

p.takeBreak()
e.takeBreak()
pr.takeBreak()   #what will be the output of this line


#--> next-line, will through an error
#print(p.company) ---> not same as -->  p.company()  
print(p.company)
print(e.company)
print(pr.company)
print(pr.country)
