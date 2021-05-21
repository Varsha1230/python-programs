# use open function to read the content of the file-------

#f=open("sample.txt", "r")
f=open("ch9_1_sample.txt")    #by default the mode is r
#data=f.read()     # read is a built-in function,which is used to read the content of a file
data=f.read(5)     #reads first 5 characters from the file
print(data)
f.close()    # file must be closed after performing your task, so that other programs can do their work on that file,,, otherwise other programs can't do
