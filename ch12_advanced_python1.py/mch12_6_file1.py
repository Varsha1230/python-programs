def greet(name):
    print(f"Good morning, {name}")

#print(__name__)

if __name__ == "__main__":    # if we don't want to import these 2-lines (which are written below in second module(or other program/files)i.e. ch12_file2.py)

    n=input("enter a name: \n")
    greet(n)    # function