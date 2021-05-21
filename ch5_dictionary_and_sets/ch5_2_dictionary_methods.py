myDict={
    "fast":"In a Quick Manner",
    "harry":"A Coder", 
    "marks":[1,2,5],
    "anotherdict":{'harry':'Player'},
    1:2
}


print(myDict.keys())     #print keys in the form of list

print(type(myDict.keys())) #print the type i.e. 'dict_keys' (not list)


#Dictionary methods---------------------------------------------------------------------
print(list(myDict.keys()))  #typecasting into list   (bcoz it's by default type is dict_keys)     (print the keys of dictionary)
print(myDict.values())      #prints the values of the dictionary
print(myDict.items())       #prints the (key,values)pair for all contents/items of the dictionary



print(myDict)
updateDict={
    "lovish": "Friend",
    "divya" : "Friend",
    "shubham": "Friend",
    "harry"  : "a dancer"     #also update the value of the key i.e. harry,,, which is present before in above dictionary
}
myDict.update(updateDict)    #update(updated_dict_variable)..... it updates the dictionary by adding key-value pairs from updateDict_variable 
print(myDict)

print(myDict.get("harry"))    # .get() method:--> prints value associated with key "harry"
print(myDict["harry"])        # returns same output as .get() method ,, so why we are going to use .get()method....
#bcoz if the corresponding key is not present in the dictionary then it will throws an error,,, whereas .get()method will return "None"
 
#for example--------- difference between .get() and []  syntax in Dictionaries

print(myDict.get("harry2"))       #.get() method----> returns None as harry2 is not present in the dictionary
#print(myDict["harry2"])           # it will throw an error as harry2 is not present in the dictionary































