a=input("enter your name")
print(a)


a=input("enter your no")
print(a)
print(type(a))  #type of the input is-- string,,, coz input() function is always taken input as the string... so,if we want the input in another type then we need to typecast that,,, as shown below


a=input("enter your no.")
a=int(a)  #typecasting:-- convert string into integer (only when if possible)
print(a)
print(type(a))
