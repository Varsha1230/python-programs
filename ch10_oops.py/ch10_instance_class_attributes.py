class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()

#creating instance attribute salary for both the objects
#harry.salary =300
#rajni.salary =400
harry.salary=46
print(harry.salary)
print(rajni.salary)

#below line throws an error as address is not present in instace and class
#print(rajni.address)