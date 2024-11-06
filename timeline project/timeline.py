import random

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
    setupNewGame(showGameMenu())
    play()
    showWinner()

def showGameMenu():
    print("test gamemenu")
    #1 game menu
    print("Welcome to The Timeline Game")
    #1.1 select/defining the number of players
    playernums = int(input("Please enter the amount of players you have: "))
    #1.2 asking the user if they would like to enable bots
    bots = input("Would you like bots: (Yes/No) ")
    #1.3 difficulty
    if bots == "Yes" or bots == "yes" or bots == "Y" or bots == "y":
        difficulty  = input("What difficulty: ")
        return difficulty
    return playernums


def setupNewGame(playernums):
    #2 setup new game
    print("test setupNewGame")
    #2.1 deal cards to player(s)/bots

    #2.2

def play():
    print("test play")
    currentPlayer = 1 #default number for testing
    #3.1 starting a player's turm
    takeTurn()
    #3.2 seleting next player

    while not gameOver():
        takeTurn(currentPlayer)
        currentPlayer = pickNextPlayer

def takeTurn():
    #3.2 select next player 
    print(f"player{player} is taking their turn...")



def gameOver():
    #3.4 
    print("test gameover")

def pickNextPlayer():
    print("test picknextplayer")

def showWinner():
    print("test winner")

timeline()
