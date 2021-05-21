import random

# snake water gun or rock paper scissors
def gameWin(comp, you):
    # if two values are equal, declare a tie!
    if comp == you:
        return None

#check for all possibilities when computer chose s
# case 1:-
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True


#check for all possibilities when computer chose w            
# case 2:- 
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True


#check for all possibilities when computer chose g
# case 3:-    
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


print("computer Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'


you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")