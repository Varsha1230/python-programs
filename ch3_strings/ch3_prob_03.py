#to detect double spaces in a string-----------------------

poem='''Twinkle, twinkle,   little star                         --------3spaces
How I  wonder what you are                                      --------2spaces
Up above the  world so high
Like a   diamond in the sky'''

print(poem.find("  "))


# 2nd way---------------------------------

st="this is a string with double  spaces"

doubleSpaces=st.find("  ")
print(doubleSpaces)






