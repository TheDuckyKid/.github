print("hello timeline")

#play timeline
#def timeline():
    #1. game menu
    #1.1 select number of players
    #1.2 bots [on or of]
    #1.3 difficulty [level]
    #2. setup new game
    #2.1 deal cards to each player
    #2.3 pick starting player
    #3. play game (player turns)
    #3.1 starting player turn
    #3.2 select next player
    #3.3 take turn
    #3.4 check if player won/game is over, if true go to 4
    #3.5 go back to 3.2
    #4 show who winner is     

def timeline():
    print("starting timeline game")
    showGameMenu()
    setupNewGame()
    play()
    showWinner()

def showGameMenu():
    print("test gamemenu")
    print("Welcome to The Timeline Game")
    playernums = int(input("Please enter the amount of players you have: "))
    bots = input("Would you like bots: (Yes/No) ")
    




def setupNewGame():
    print("test setupNewGame")

def play():
    print("test play")
    currentPlayer = 1
    while not gameOver():
        takeTurn(currentPlayer)
        currentPlayer = pickNextPlayer

def takeTurn():
    print(f"player{player} is taking their turn...")

def gameOver():
    print("test gameover")

def pickNextPlayer():
    print("test picknextplayer")

def showWinner():
    print("test play")

timeline()
