import random
randNumber = random.randint(1,100)      # generate random no. including 1 and 100 also
userGuess = None                        # define userGuess as None, otherwise we'll get userGuess is not defined(in line no.:-9,8)
guesses = 0

# userGuess = int(input("Enter your guess: " ))

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: " ))  
    guesses += 1
    if(userGuess==randNumber):
        print("you guessed it right!")
    else:
        if(userGuess > randNumber):
            print("you guessed it wrong! Enter a smaller number")
        else:
            print("you guessed it wrong! Enter a larger number")

print(f"you guessed the number in {guesses} guesses")

with open("hiscore.txt", "r") as f:    # first we have to create 'hiscore.txt' file,otherwise we'll get this error i.e.:- no such file or directory: ' hiscore.txt'
    hiscore = int(f.read())            # typecast in integer, bcoz 'f.read()' is in string

if(guesses < hiscore):
    print("you have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))         # typecast in string, bcoz "guesses's-value" is in integer