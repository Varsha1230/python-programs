def readFile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    
    except FileNotFoundError:
        print(f"File {filename} is not found")

readFile("ch12_prob1_1.txt")
readFile("ch12_prob1_2.txt")
readFile("ch12_prob1_3.txt")