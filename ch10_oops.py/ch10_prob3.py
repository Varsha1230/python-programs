class Sample:
    a = "Harry"   #class-attribute

obj = Sample()    #creating object
obj.a="Vikky"     #instance-attribute:- it doesn't change the class-attribute,,, bcoz it is another attribute with same name
#Sample.a="Vikky"  #if we want to change the attribute:- we have to use this statement

print(Sample.a)
print(obj.a)