# Dictionary to store information about the rooms in the adventure
rooms = {
    'living_room': {
        'description': 'You are in the living room. There is a door to the kitchen and a hallway.',
        'exits': ['kitchen', 'hallway']
    },
    'kitchen': {
        'description': 'You are in the kitchen. There is a door to the living room and a fridge.',
        'exits': ['living_room']
    },
    'hallway': {
        'description': 'You are in a dark hallway. There is a door to the living room and a bedroom.',
        'exits': ['living_room', 'bedroom']
    },
    'bedroom': {
        'description': 'You are in the bedroom. There is a door to the hallway.',
        'exits': ['hallway']
    }
}

# Helper function to display room details
def show_room(room_name):
    print(f"\n{rooms[room_name]['description']}")
    print("Exits: ", ", ".join(rooms[room_name]['exits']))

# Main game function
def play_game():
    current_room = 'living_room'
    
    while True:
        # Show the current room's description and available exits
        show_room(current_room)
        
        # Get the player's next move
        move = input("\nWhere do you want to go? ").lower()
        
        # Check if the move is valid
        if move in rooms[current_room]['exits']:
            current_room = move
        else:
            print("\nThat's not a valid exit. Try again.")
        
        # Ask if the player wants to continue
        continue_game = input("\nDo you want to keep exploring? (yes/no): ").lower()
        if continue_game != 'yes':
            print("Thanks for playing!")
            break

# Start the game
play_game()