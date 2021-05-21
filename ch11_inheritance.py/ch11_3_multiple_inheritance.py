class Employee:
    company = "visa"
    eCode = 120

class Freelancer:
    company = "fiverr"
    level = 0

    def upgradeLevel(self):
        self.level =self.level + 1

class Programmer(Employee, Freelancer):   #multiple inheritance
    name = "Rohit"

p = Programmer()
print(p.level)
p.upgradeLevel() 
print(p.level)
print(p.company)   #what will be printed... due to this line---> ans:--> "visa", bcoz when we define child class then, we inherit employee-class first then freelancer-class
