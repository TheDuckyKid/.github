import json
import random

print("Hello, Timeline!")

def loadDeck(file_path):
    try:
        with open(file_path, "r") as file:
            deck = json.load(file)
        print("Deck loaded successfully.")
        return deck
    except FileNotFoundError:
        print("Error: JSON file not found. Please ensure the file is in the correct directory.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Please check the file's format.")
        return []

# Main timeline function
def timeline(json_file):
    deck = loadDeck(json_file)
    if not deck:
        return
    
    print("Starting the Timeline game...")
    game_settings = showGameMenu()
    player_count, player_names, bots_enabled, difficulty = game_settings
    setupNewGame(player_count, player_names, bots_enabled, deck)
    winner = play(player_count, player_names, bots_enabled, deck)
    showWinner(winner)

def showGameMenu():
    print("Welcome to The Timeline Game")
    
    player_count = int(input("Please enter the number of players: "))
    player_names = []
    for i in range(player_count):
        name = input("Please enter the name of Player " + str(i + 1) + ": ")
        player_names.append(name)
    
    bots_enabled = input("Would you like to add bots? (Yes/No): ").strip().lower() in ['yes', 'y']
    difficulty = None
    if bots_enabled:
        difficulty = int(input("Set the difficulty level [1-10]: "))
    
    return player_count, player_names, bots_enabled, difficulty

def setupNewGame(player_count, player_names, bots_enabled, deck):
    print("Setting up a new game...")
    random.shuffle(deck)  # Shuffle the deck
    player_hands = {name: [] for name in player_names}

    if bots_enabled:
        bot_name = "Bot"
        player_names.append(bot_name)
        player_hands[bot_name] = []
    
    for _ in range(5):  # Deal 5 cards to each player
        for player in player_names:
            if deck:
                card = deck.pop()
                player_hands[player].append(card)
    
    print("Player hands:")
    for player in player_hands:
        print(player + ": " + str(player_hands[player]))
    
    return player_hands

def play(player_count, player_names, bots_enabled, deck):
    print("Starting the game...")
    current_player_index = 0
    timeline = []
    
    while True:
        current_player = player_names[current_player_index]
        print(current_player + "'s turn!")
        action_result = takeTurn(current_player, timeline, deck)
        
        if action_result == "win":
            return current_player
        
        current_player_index = (current_player_index + 1) % player_count

def takeTurn(player, timeline, deck):
    if len(timeline) == 0:
        print("The timeline is empty. You can play any card.")
        return "continue"
    
    print("Current timeline:")
    for event in sorted(timeline, key=lambda x: x["title"]):
        print(event["title"] + " - " + str(event["month"]))
    
    if deck:
        played_card = deck.pop()
        print(player + " plays: " + played_card["title"] + " (" + played_card["month"] + ")")
        
        timeline.append(played_card)
        return "continue"
    else:
        return "win"

def showWinner(winner):
    print("Congratulations, " + winner + "! You have won the game!")

import os
print("Current Working Directory:", os.getcwd())

# Run the timeline game with the JSON file
timeline("timeline project/deck.json")
