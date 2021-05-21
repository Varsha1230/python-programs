myDict={
    "Fast":"In a Quick Manner",
    "Harry":"A Coder", 
    "Marks": [1,2,5],
    "anotherdict":{'harry':'Player'}     # anotherdict:- is a dictionary under a dictionary(i.e. myDict)
# nested dictionary i.e. myDict
}

# print(myDict['Fast'])    output:- In a Quick Manner
# print(myDict['Harry'])   output:- A Coder
# print(myDict['Marks'])   output:- [1,2,5]
print(myDict['anotherdict'])

print(myDict['anotherdict']['harry'])    #nested dictionary

#------------------------------------------------------
myDict['Marks']=[45,78]    #example of mutable   #example of no duplicate keys