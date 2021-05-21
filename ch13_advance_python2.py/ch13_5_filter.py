def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False

g10 = lambda num: num>10     # lambda-function

l = [1,2,3,4,5,6,7,89,67,34,56,12]
print(list(filter(greater_than_5, l)))
print(list(filter(g10, l)))  # lambda-function