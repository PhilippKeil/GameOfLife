__author__ = 'philipp'
import grid

def new_game(size_x, size_y, markers):
    # Init the game grid
    global game_grid
    game_grid = grid.Grid(size_x, size_y, markers)

    # Define the starting points of the game
    # Set as many coordinates as you want
    while 1:
        x = int(input('x: '))
        y = int(input('y: '))
        if game_grid.is_empty(x, y):
            # Field is empty
            # Make the field occupied
            game_grid.write_to_grid(int(x), int(y), 1)
        else:
            # Field is already occupied
            # Do nothing other than inform user
            print('Field is already occupied')

        # Ask the user if he wants to fill another field
        inp = raw_input('Do you want to set another field? (Yes = Y, No = everything else) ')
        if inp == 'Y':
            # User wants to set another field
            # Restart the loop
            continue
        else:
            # Jump out of the loop, because the user is ready for the game to begin
            break

    # Print the final game_grid

    # Start the game by calling the game cycle once


new_game(10, 10, ['O', 'X'])