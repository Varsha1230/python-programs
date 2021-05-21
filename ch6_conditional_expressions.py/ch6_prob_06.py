marks = int(input("please enter your marks:\n"))

if 100 >= marks >= 90 :
    grade = "Ex" #print("excellent")

elif 90 > marks >= 80 :
    grade = 'A' 

elif 80 > marks >= 70 :
    grade = 'B' 

elif 70 > marks >= 60 :
    grade = 'C' 

elif 60 > marks >= 50 :
    grade = 'D' 

elif 50 > marks :
    grade = 'E' 

else:
    grade = 'F'

print("your grade is", grade)

