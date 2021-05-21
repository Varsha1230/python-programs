a = [3, 6, 7 ,8, 8, 9, 9,23 ,65, 87,76, 23,6777777, 34253246,32.4]
#b = []

# for item in a:
#     if item%2==0:
#         b.append(item)
# print(b)

# we can do this task by using: list comprehension also....

b = [i for i in a if i%2==0]
print(b)