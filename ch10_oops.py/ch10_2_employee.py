class Employee:
    company = "Google"     # class-attribute

harry = Employee()  #creating employee class object
rajni = Employee()  #creating employee class object

harry.salary =300      # instance-attribute
rajni.salary = 400     # instance-attribute
 
print(harry.company)
print(rajni.company)

Employee.company ="YouTube"  #changing class-attribute using class name i.e. Employee,,, bcoz comapny is the class Employee's attribute
print(harry.company)
print(rajni.company)

print(harry.salary)
print(rajni.salary)