a=input("enter first no.")
b=input("enter second no.")
c=a+b
print(c)  #1st way for getting output



c=print(a+b)  #2nd way for getting output


'''we are getting the output 23, bcoz in input function they are treated as the string, 
so here string concatenation operation is performed... then we need to typecast here...'''


a=input("enter first no.")
a=int(a)  #typecast
b=input("enter second no.")
b=int(b)  #typecast
c=a+b
print(c)  #1st way for getting output

c=print(a+b)  #2nd way for getting output

#----------------------------------------------------------------------------

a=34
b=34
print("the sum of a and b is=", a+b)