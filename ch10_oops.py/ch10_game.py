class Remote():
    pass

class Player:
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveTop(self):
        pass
    def moveBelow(self):
        pass

remote1 = Remote()   #creating object i.e."remote1" of class Remote()
Player1 = player()   #creating object i.e."player1" of class Player()

if(remote1.isLeftPressed()):
    Player1.moveLeft() 