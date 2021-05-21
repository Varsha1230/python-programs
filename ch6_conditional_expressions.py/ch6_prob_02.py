sub1=int(input("enter  subject 1 marks: "))
sub2=int(input("enter  subject 2 marks: "))
sub3=int(input("enter  subject 3 marks: "))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail, bcoz you have less than 33% in subject(s)")


elif(sub1+sub2+sub3)/3 <40:
    print("you are fail, due to your percentage is less than 40")

else:
    print("Congratulations,you are passed the exams")