class Employee:
    company = "camel"       # class-attribute
    location = "Delhi"      # class-attribute
    salary = 100            # class-attribute

# def changeSalary(self, sal):
#     self.__class__.salary = sal    # dunder class       (we can use this for same task,but it is related to object, here oue motive is just use the class method only)

@classmethod
def changeSalary(cls, sal):
    cls.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)