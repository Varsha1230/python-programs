# n! = (n-1)! * n
# sum(n) = sum(n-1) + n


#-- there is no exit/stop statement in this loop------------------------------------------------
# def sum(n):
#     return (sum(n-1) + n)

# num = int(input("please enter a no.: "))
# add = sum(num)
# print("the sum of n natural numbers is: "  + str(add))


#--------------------------------------------------------------------

def sum(n):
    if n==1 :
        return 1
    else :
        return  n + sum(n-1)    

m=int(input("Enter a natural number : "))
x=sum(m)
print("The sum of first  " + str(m)+ " natural number is "+ str(x))