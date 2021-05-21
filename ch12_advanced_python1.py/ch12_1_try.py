while(True):
    print("--------------   PRESS 'Q'2 TO QUIT   ---------------")
    a = input("enter a number:")

    if a == 'q':
        break        # break while loop, if somebody press q

    try:
        a = int(a)
        if a>6:
            print("yes, you entered a number greater than 6")

        else:
            print("you entered a number smaller than 6")

    except Exception as e:
        #print(e)   
        print(f"your input resulted in an error {e}")    # customized error throw
    
print("Thanks for playing this game")