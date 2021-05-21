try:
    a= int(input("enter a number:   "))
    c=1/a

#except Exception as e:
 #   print("Exception1 occured:  ")
  #  print(e)


# except ValueError as e:
#     print("Exception2 occured:  ")
#     print(e)


# except ZeroDivisionError as e:
#     print("Exception3 occured:  ")
#     print(e)

except ValueError as e:
    print("please enter a valid value")

except ZeroDivisionError as e:
    print("make sure you aren't dividing by 0")
    

print("Thanks for using this code!")





