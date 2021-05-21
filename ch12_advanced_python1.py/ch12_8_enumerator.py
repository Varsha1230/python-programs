list1 = [3, 43, 4, False, 4.5, "harry"]

# index = 0
# for item in list1:
#     print(index, item)
#     index += 1

# we can do the above task by using : enumerator.......

for index, item in enumerate(list1):    # here order is necessary, index must be written first-place only
    print(index,item)