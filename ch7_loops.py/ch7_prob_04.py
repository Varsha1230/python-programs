num = int(input("please enter a number of which you want to check whether it is prime or not: "))

prime = True

for i in range(2,num):
    if (num%i==0):
        prime = False
        break

if prime:
    print("This no. is prime")
else:
    print("This no. is not prime")