#create a dictionary of hindi words with values as their english translation. provide the user with an option to look it up.

myDict={
    "pankha":"fan",
    "dabba":"box",
    "vastu":"item"
}
print("options are", myDict.keys())
a=input("enter the hindi word:\n")
#print("the meaning of your word is:", myDict[a])       #by using []:->if the key is not available in the dictionary then it will throw an error

print("the meaning of your word is:",myDict.get(a))     #by using .get():-> if key is not present then it will return 'None' as the output,,, here .get() is used to avoid error












