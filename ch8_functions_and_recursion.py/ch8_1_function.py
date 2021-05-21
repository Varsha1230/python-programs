#-------------------------------------

marks1=[45,78,86,77]
percentage1=(sum(marks1)/400)*100  #sum:-built-in function

marks2=[75,98,88,78]
percentage2=(sum(marks2)/400)*100

print(percentage1,percentage2)

#-----------------------------------------------

marks1=[45,78,86,77]
percentage1=((marks1[0] + marks1[1] + marks1[2] + marks1[3])/400)*100  #if 'sum':-built-in function is not there

marks2=[75,98,88,78]
percentage2=((marks2[0] + marks2[1] + marks2[2] + marks2[3])/400)*100

print(percentage1,percentage2)


# we can group this code through functions, so that we can use it again n again acc to need, it also reduces the lenght of code n imrove readability of code----------------------------------------------------------------
#once defined and used again n again.........
def percent(marks):    #here 'marks' is optional,means its may be can't take value
    p=((marks[0]+ marks[1]+ marks[2]+ marks[3])/400)*100     #we can also do this here: return((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
    return p

marks1=[45,78,86,77]
percentage1=percent(marks1)     # "marks1" copied into 'marks', then percent()function will return percentage

marks2=[75,98,78,91]
percentage2=percent(marks2)     # "marks2" copied into 'marks', then percent() function will return percentage

print(percentage1,percentage2)


