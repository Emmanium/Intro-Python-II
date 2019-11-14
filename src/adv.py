from room import Room
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Declare items
items = {
    'rock':    Item("Rock", "Potentially deadly"),

    'pebble':    Item("Pebble", "Potentially sweet"),

    'sword':    Item("Sword", "Poke it with the pointy end"),

    'shield':    Item(
        "Shield", "A good dinner plate")
}

# For convenience sakes
# creates a variable with the same name as an item and makes sure the name is all lowercase
rock = items['rock'].name.lower()
pebble = items['pebble'].name.lower()
sword = items['sword'].name.lower()
shield = items['shield'].name.lower()

# Add items to Rooms
room['outside'].items = [rock, pebble]
room['foyer'].items = [sword, shield]

#
# Main
#


def main():
    # Establish re-usable variables
    valid_inputs = ['n', 's', 'e', 'w', 'q']
    flag = True
    start_room = room['outside']
    curr_room = start_room
    while flag:
        user_input = input(
            'Type a direction:\nn, s, e, w\nOr try taking an item using the following format:\ntake item_name_here\nPress q quit\n')
        # split and create copy of the user_input after making it all lowercase
        ui_copy = user_input.lower().split()
        # # If length is greater than two, print help message
        if len(ui_copy) > 2:
            print("Please only enter one or two words")
        # If the length is 2 and the first string in the dictionary is "take", loop through the items in the room
        elif len(ui_copy) == 2 and ui_copy[0] == "take":
            if ui_copy[1] in curr_room.items:
                print("you got it")
            else:
                print(f"{ui_copy[1]} doesn't exist in the room")
        # If the length is 1 and the user input is in valid_inputs proceed onwards
        elif len(ui_copy) == 1 and user_input in valid_inputs:
            # If the user moves North and the room exists
            if user_input == 'n' and curr_room.n_to is not None:
                curr_room = curr_room.n_to
                print(curr_room)
            # Same Idea As Above Except South
            elif user_input == 's' and curr_room.s_to is not None:
                curr_room = curr_room.s_to
                print(curr_room)
            # Now East
            elif user_input == 'e' and curr_room.e_to is not None:
                curr_room = curr_room.e_to
                print(curr_room)
            # And West
            elif user_input == 'w' and curr_room.w_to is not None:
                curr_room = curr_room.w_to
                print(curr_room)

            elif user_input == 'q':
                quit()
        else:
            print("Please move in a valid direction")


if __name__ == "__main__":
    main()
# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
