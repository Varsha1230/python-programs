try:
    i = int(input("enter a number:  "))
    c = 1/i

except Exception as e:
    print(e)
    exit()

finally:
    print("we are done...")     # this line will be executed, even though we put exit() in finally-block... whether we made any mistake or not...

print("thanks for using the program...") #this line will be executed only when we don't make any mistake.... if we made any mistake then this line will not be executed   
  