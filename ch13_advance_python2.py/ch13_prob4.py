l = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,89,23,456,67,8,5,4,565,78,90,45]

a = filter(lambda a: a%5==0, l)
print(list(a))