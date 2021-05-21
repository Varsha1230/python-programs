# l1=[1,8,7,2,21,15]
# l1_sorted=l1.sort()---------this is the wrong way
# print(l1_sorted)



l1=[1,8,7,2,21,15]
print(l1)
l1.sort()          #sorts the list
print(l1)



l1=[1,8,7,2,21,15]
print(l1)
l1.reverse()          #reverse the list
print(l1)



l1=[1,8,7,2,21,15]
print(l1)
l1.append(45)          #adds 45 at the end of the list
l1.append(8)          #adds 8 at the end of the list
print(l1)



l1=[1,8,7,2,21,15]
print(l1)
l1.insert(0,544)        #insert 544 at index 0
l1.insert(1,5)          #nsert 5 at index 1
l1.insert(3,0)          #insert 0 at the index 3
print(l1)


l1.pop(2)           #pop delete element at index 2
print(l1)               


l1.remove(21)       #remove 21 from the list
print(l1)