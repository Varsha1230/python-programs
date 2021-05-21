class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus = 500
    # totalSalary = 6100

    @property                                # property-decorator
    def totalSalary(self):                   # this is a function, which is treated as a property, due to property decorator ...(we make it as a property of the class by using property decorator)
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val - self.salary

e = Employee()
print(e.totalSalary)
e.totalSalary = 5800
print(e.salary)
print(e.salarybonus) 