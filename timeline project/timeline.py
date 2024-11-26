import random
import json

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

#deck = "timeline.txt"

#main timeline function
def timeline(deck):
    #print statement stating that the timeline game has started
    print("starting timeline game")
    #list  
    s_list = showGameMenu()
    setupNewGame(s_list[0])
    play()
    showWinner()

def showGameMenu():
    print("test gamemenu")
    #1 game menu
    print("Welcome to The Timeline Game")
    #1.1 select/defining the number of players
    playernums = int(input("Please enter the amount of players you have: "))
    for duck in range(playernums):
        print("test pls work")
    #1.2 asking the user if they would like to enable bots
    bots = input("Would you like bots: (Yes/No) ")
    #1.3 difficulty
    if bots == "Yes" or bots == "yes" or bots == "Y" or bots == "y":
        difficulty  = input("What difficulty:[1-10] ")
        return difficulty
    return [playernums,bots]

deck  = {
    "title" : "placeholder",
    "year" : 2,
    "month" :3,
    "description" :4
}
   
def setupNewGame(Playercount):
    #2 setup new game
    print("test setupNewGame")
    #2.1 deal cards to player(s)/bots
    cardcheck = []
    print("Distributing cards")
    for duck in range(Playercount):
        cardchoice = random.randrange(0,19)
        print("Card number #" + str(cardchoice) + "for player: " + str(duck))
        #way to check if card number is already taken
        cardcheck.append(cardchoice)
        print(cardcheck)
        #if cardchoice = any thing in card check
        for card in cardcheck:
            if cardchoice == cardcheck[card]:
                print("yay")
            print(card)


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

timeline(deck)
