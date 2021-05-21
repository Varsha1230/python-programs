num = int(input("please enter a number of which you want to print a table"))

for i in range (1,11):
    #print(str(num) + "x" + str(i) + "=" + str(num*i))


# we can do the above task with the help of "fstring" also------ it is more easier then above method

    print(f"{num}x{i}={num*i}")