#step 1 show a menu
#step 2 set up game
#step 3 play
#step 4 show winner

def showmenu():
    print("menu is showing")
    numberofplayers = int(input("type number of players"))


def setupgame(numberofplayers):
    print("setting up game")
    cards = []
    for i in range(numberofplayers):
        cards.append(getstartingcards())
    return cards


def play():
    print("game is being played")

def showwinner():
    print("winner of the game")

def playgame():
    print("game is running")
    showmenu()
    setupgame()
    play()
    showwinner()
playgame()