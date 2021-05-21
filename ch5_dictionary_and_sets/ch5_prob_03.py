#can we have a set with 18(int) and "18"(str) as a value in it...

s={18, "18"}
print(s)      #bcoz in phython both 18 are different


s={18,"18",18.1}
print(s)             # in python all these values are diff. i.e. int,str,float repectively


s={18,"18",18.0}
print(s)             # output:- {18, '18'} :-- bcoz here 18 and 18.0 are not unique

