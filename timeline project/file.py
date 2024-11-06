#step 1 show a menu
#step 2 set up game
#step 3 play
#step 4 show winner

def showmenu():
    print("menu is showing")
    numberofplayers = int(input("type number of players"))
    return numberofplayers

def getstartingcards():
    return "A"

def setupgame(numberofplayers):
    print("setting up game")
    #get player names
    names = []

    cards = []
    for i in range(numberofplayers):
        cards.append(getstartingcards())
        names.append("Bob")
    return [cards,names]


def play():
    print("game is being played")

def showwinner():
    print("winner of the game")

def playgame():
    print("game is running")
    numberofplayers = showmenu()
    set_result = setupgame(numberofplayers)
    cards = set_result[0]
    play()
    showwinner()
playgame()