a=3
b=4

# Arithmetic operators--------------------------------------------
print("The value of 3+4 is", 3+4)
'''----string-------      
3+4:-- it is an arithmetic expression, which is calculated/evaluated and gives 7 as the output'''

print("The value of 3-4 is", 3-4)
print("The value of 3*4 is", 3*4)
print("The value of 3/4 is", 3/4)


#Assignment operators---------------------------------------------
a=34
a+=12     # '+=' to change the no. and add into it
print(a)  #46

a-=10     #  to subtract the no. 
print(a)  # 24X       ans:- 36

a *= 10
print(a) # 36*10= 360

a /= 10
print(a) #360/10= 36.0

#--------------------------------------------------------------

a = 34
a -= 12
a *= 12
a /= 12
print(a) # 34-12= 22     22*12= 264     264/12= 22.0'''


#Comparision operator-----------------------------------------------------

b=(14>7)
print(b)    #True

a=(7>14)
print(a)    #False

c=(14>=7)   
print(c)    #True

e=(14<=7)
print(e)    #False

e=(14==7)
print(e)    #False

e=(14!=7)
print(e)    #True


# Logical operators--------------------------------------------------------

bool1 = True
bool2 = False
print("The value of bool1 and bool2 is", (bool1 and bool2))     #False 
print("The value of bool1 or bool2 is", (bool1 or bool2))      #True
print("The value of not bool2 is", (not bool2))           #True
