class Employee:
    company= "Google"   #class-attribute
    salary= 100         #class-attribute

harry = Employee()
rajni = Employee()

# creating instance-attribute salary for both the objects
# harry.salary = 300      # instance-attribute
# rajni.salary = 400      # instance-attribute
harry.salary = 45         # creating a new instance-attribute/variable
print(harry.salary)
print(rajni.salary)

# below line throws an error as address is not present in instance/class
# print(rajni.address)