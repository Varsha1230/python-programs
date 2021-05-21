# to fill in a letter template given below with name and date.
#     letter=''' Dear<|NAME|>,
#     You're  selected!

#      Date:<|DATE|>
     

 
# letter=''' Dear<|NAME|>,
# You're  selected!

# Date:<|DATE|>
# '''
# print(letter)----------------------  it will be printed as it is 
# like:-   Dear<|NAME|>,
#          You're  selected!

#          Date:<|DATE|>




#if we want to cutomize it-----------------------


letter='''Dear <|NAME|>,
Greetings from ABC coding house. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and regards,
shanta
Date: <|DATE|>
'''

name=input("Enter your name:\n")
date=input("Enter date:\n")

letter=letter.replace("<|NAME|>", name)
letter=letter.replace("<|DATE|>", date)

print(letter)