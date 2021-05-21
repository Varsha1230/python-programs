#  n! = 1x2x3x4x...........xn
#  5! = 1x2x3x4x5


n = int(input("enter a no."))

factorial =1

for i in range (1,n+1):
    factorial = factorial * i

print(f"the factorial of {n} number is {factorial}")