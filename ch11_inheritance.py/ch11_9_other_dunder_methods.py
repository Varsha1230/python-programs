class Number:
    def __init__(self, num):   # dunder method
        self.num = num         # dunder method
    
    def __add__(self, num2):
        print("let's add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("let's multiply")
        return self.num * num2.num
  
    def __str__(self):
        return f"Decimal number: {self.num}"

    def __len__(self):
        return 1

n= Number(9)
print(n)
print(len(n))
