import random

print("Hello, Timeline!")

# Main timeline function
def timeline(deck):
    print("Starting the Timeline game...")
    game_settings = showGameMenu()
    player_count, player_names, bots_enabled, difficulty = game_settings
    setupNewGame(player_count, player_names, bots_enabled)
    winner = play(player_count, player_names, bots_enabled)
    showWinner(winner)

def showGameMenu():
    print("Welcome to The Timeline Game")
    
    # Select the number of players
    player_count = int(input("Please enter the number of players: "))
    player_names = []
    for i in range(player_count):
        name = input(f"Please enter the name of Player {i + 1}: ")
        player_names.append(name)
    
    # Ask if bots should be enabled
    bots_enabled = input("Would you like to add bots? (Yes/No): ").strip().lower() in ['yes', 'y']
    
    # Set difficulty if bots are enabled
    difficulty = None
    if bots_enabled:
        difficulty = int(input("Set the difficulty level [1-10]: "))
    
    return player_count, player_names, bots_enabled, difficulty

def setupNewGame(player_count, player_names, bots_enabled):
    print("Setting up a new game...")
    # Shuffle and deal cards
    deck = generateDeck()
    player_hands = {name: [] for name in player_names}

    if bots_enabled:
        bot_name = "Bot"
        player_names.append(bot_name)
        player_hands[bot_name] = []
    
    # Deal cards
    print("Distributing cards to players...")
    for _ in range(5):  # Give each player 5 cards
        for player in player_names:
            card = deck.pop(random.randrange(len(deck)))
            player_hands[player].append(card)
    
    print("Player hands:")
    for player, hand in player_hands.items():
        print(f"{player}: {hand}")
    
    return player_hands

def generateDeck():
    # Generate a simple deck with placeholder events
    return [
        {"title": f"Event {i}", "year": random.randint(1900, 2020)}
        for i in range(20)
    ]

def play(player_count, player_names, bots_enabled):
    print("Starting the game...")
    current_player_index = 0
    game_active = True
    timeline = []  # Timeline starts empty
    
    while game_active:
        current_player = player_names[current_player_index]
        print(f"{current_player}'s turn!")
        
        # Take turn
        action_result = takeTurn(current_player, timeline)
        
        # Check if the game is over
        if action_result == "win":
            return current_player
        
        # Move to the next player
        current_player_index = (current_player_index + 1) % player_count

def takeTurn(player, timeline):
    print(f"{player} is taking their turn...")
    
    if len(timeline) == 0:
        # First turn: any card can be played
        print("The timeline is empty. You can play any card.")
        return "continue"
    
    # Show the timeline to the player
    print("Current timeline:")
    for event in sorted(timeline, key=lambda x: x["year"]):
        print(f"{event['title']} - {event['year']}")
    
    # Simulate playing a card (in a real game, input would be handled here)
    played_card = {"title": f"Played by {player}", "year": random.randint(1900, 2020)}
    print(f"{player} plays: {played_card['title']} ({played_card['year']})")
    
    # Check if the card fits in the timeline
    if isCardInTimeline(played_card, timeline):
        print(f"{played_card['title']} fits correctly in the timeline!")
        timeline.append(played_card)
        return "continue"
    else:
        print(f"{played_card['title']} does NOT fit in the timeline!")
        return "lose"

def isCardInTimeline(card, timeline):
    years = [event["year"] for event in timeline]
    return min(years) <= card["year"] <= max(years)

def showWinner(winner):
    print(f"Congratulations, {winner}! You have won the game!")

timeline("timeline.json")
