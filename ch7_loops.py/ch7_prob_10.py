num = int(input("Enter the number\n"))
for i in range(10,0,-1):
    print(f"{num}X{i}={num*i}")

# # 2nd way--------------------------------
# a = int(input("enter a number"))
# n =10
# for i in range(1,10):
#      print(a ,"X", n, "=",(n*a))
#      n-=1

# # 3rd way_---------------------
# a = 5
# for i in range(10,0,-1):
#        print(f"{a}X{i}={a*i}")

#4th way--------------------------------------------
n=int(input("Enter the number you want table of: "))
for i in reversed(range(1,11)):
    print(f"{n} X {i} = {n*i}")



