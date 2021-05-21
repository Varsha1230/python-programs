# writing in files-----------------

# f = open('another.txt', 'w')
# f.write("please write this to the file \n")       # write function print these line 'how many times' =  jitni bar aapne write fn likha hoga
# f.write("please write this to the file \n")
# f.write("please write this to the file \n")
# f.write("please write this to the file \n")
# f.write("please write this to the file \n")
# f.write("please write this to the file \n")



# appending-------------------

f = open("another.txt", 'a')   
f.write("I am appending")           #jitni bar code run krege utni bar ye print hoga same file me, due to append mode
f.close()