for i in range(10):
    print(i)
    if i==5:
        break
else:
    print("this is inside else of for-loop") # the else-statement is not executed bcoz the loop is not successfully/naturally terminated due to using break-statement.