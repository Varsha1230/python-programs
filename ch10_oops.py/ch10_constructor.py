class Employee:
    company = "Google"
    
def __init__(self, name, salary, subunit):   #creating constructor
    self.name = name                   # using the arguments... if we wants/needs to...
    self.salary = salary               # using the arguments... if we wants/needs to...
    self.subunit = subunit             # using the arguments... if we wants/needs to...
    print("Employee is created!")

def getDetails(self):
    print(f"The name of the employee is {self.name}")
    print(f"The salary of the employee is {self.salary}")
    print(f"The subunit of the employee is {self.subunit}")    

def getSalary(self, signature):  
    print(f"salary for this employee working in {self.company} is {self.salary} \n{signature}")

@staticmethod
def greet():
    print("Good Morning, Sir")

@staticmethod
def time():
    print("The time is 9AM in yhe morning")

harry = Employee("Harry", 100, "YouTube")    # we have to pass the arguments here, as we have defined them in the above constructor ... otherwise we will get the error...
#harry = Employee()---> this throws an error *(missing 3 required positional arguments:)... bcoz we have defined them in the above constructor...
harry.getDetails()