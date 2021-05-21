class Employee:
    company = "Google"
    def getSalary(self):  #if we don't write 'self' here,,, then it will show a wierd error...
        #print("salary is 10k")
        print(f"salary for this employee working in {self.company} is {self.salary}")  #jis bhi object pr aap ye function run krrhe ho uska salary attribute yhapr ye print krega...i.e. "harry"

harry = Employee()
harry.salary = 100000
harry.getSalary()  #last line is equivalent to:--->   Employee.getSalary(harry)
