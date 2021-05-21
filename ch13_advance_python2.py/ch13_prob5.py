from functools import reduce

l = [3,8,4,2,5,45,455]

#print(max(7, 34))

a = reduce(max, l)    # don't call the function, just write the name of the function in "reduce-function"
print(a)