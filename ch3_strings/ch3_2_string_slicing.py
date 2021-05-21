greeting="Good Morning, "
name="Harry"
print(greeting+name)  #concatenating two strings


#------------------------------------------------------

c=greeting+name       #concatenating two strings
print(c)

#--string slicing-------------------------------------------------------

name="Harry"
#print(name[2])-----accessing the string's characters-----output will be= r

print(name[1:4]) #string slicing----------it means:- index 1,2,3 will be printed, output= arr

#name[3]="d"-----------doesn't work, bocz we can't change the string, we can only access the string.......

print(name[:4])  #same as name[0:4] ----- automatically through python interpretor
print(name[1:])  #same as name[1:5] ----- automatically through python interpretor,,, here 5 is the length of the string




# negative indicies---------------------------------------------

c=name[-4:-1]  #same as the name[1:4]
print(c)