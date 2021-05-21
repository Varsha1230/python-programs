class Number:
    def __init__(self, num):   # dunder method
        self.num = num         # dunder method
    
    def __add__(self, num2):
        print("let's add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("let's multiply")
        return self.num * num2.num


n1 = Number(4)     # n1 is the number object, it is not an integer
n2 = Number(6)     # n2 is the number object, it is not an integer
sum = n1 + n2      # this line always going to call add-method, due to operator overloading 
mul = n1 * n2      # this line always going to call mul-method, due to operator overloading 
print(sum)
print(mul)