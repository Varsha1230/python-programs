class Employee:        #parent/base class
    company = "Google"

    def showDetails(self):
        print("this is an employee")

class Programmer(Employee):    #child/derived class
    language = "python"
    # company = "YouTube"

    def getLanguage(self):
        print("the language is {self.language}")

    def showDetails(self):   #overwrite showDetails()-fn of class "Employee"
        print("this is an programmer")



e = Employee()      # object-creation
e.showDetails()     # fn-call by using object of class employee
p = Programmer()    # object-creation
p.showDetails()     # fn-call by using object of class programmer
print(p.company)    # using claas-employee's attribute by using the object of class programmer
