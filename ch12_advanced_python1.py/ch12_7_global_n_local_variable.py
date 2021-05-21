a=54   # Global variable
def fun1():
    global a   # it will change the value of global variable 'a'...  (from 54 to 8) 
    print(f"print statement 1: {a}")   # but this line will print 54, as we said use a=54,,,due to this line 'global a' 
    a=8   # Local variable, if global keyword is not used
    print(f"print statement 2: {a}")

fun1()    # calling function1     ans=> 8                      
print(f"print statement 3: {a}")   # accessing global variable 'a'   ans=> 54          (due to line-->  'global a' , the output will be 8 )



