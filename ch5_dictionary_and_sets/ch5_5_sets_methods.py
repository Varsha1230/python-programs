#creating an empty set------------
b=set()
print(type(b))


#now adding the items into empty set------------
b.add(4)
b.add(5)

print(b)

b.add(4)
b.add(4)
b.add(4)
b.add(5)
b.add(5)
b.add(5)
print(b)  #no repetition:----- it will ignore all repetitive values and print only {4,5}


''' #Importtant:-- can we add 'list' into the set??---> No, bcoz list can be altered/manipulated
b.add([4,5,6])

print(b)         #TypeError: unhashable type: 'list' '''


#can we add 'tuple' into the set??---> Yes, bcoz tuple can't be altered/manipulated
b.add((4,5,6))
print(b)

'''#can we add 'dictionary' in the set?----->

b.add({4:5})
print(b)           #TypeError: unhashable type: 'dict'  '''
 

#length of the set-----------------------------------
print(len(b))   #prints the length of this set


#remove item from set--------------------------------
b.remove(5)
print(b)        #remove 5 from the set



#b.remove(15)    #throws an error:--> bcoz 15 is not present in the set
#print(b)

print(b.pop())  # it removes any random value from the set, and will return the ......
print(b)

# print(b.pop())
# print(b)






















