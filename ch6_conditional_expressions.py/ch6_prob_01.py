num1=int(input("enter number 1: "))
num2=int(input("enter number 2: "))
num3=int(input("enter number 3: "))
num4=int(input("enter number 4: "))

if(num1>num2):
    f1=num1
else:
    f1=num2

if(num3>num4):
    f2=num3
else:
    f2=num4

if(f1>f2):
    print(str(f1) + "is greatest")      #here, we can also use it--->    print("the greatest no. is: ", f1)
else:
    print(str(f2) + "is greatest")      #here, we can also use it--->    print("the greatest no. is: ", f2)
