"""Tools for connect4 program."""


def printGrid(grid):
    """
    Print the grid in its current state.
    
    Args:
        grid (list): The grid being played on

    """
    print()

    # Iterate over the grid from left to right, then top to bottom
    for i in range(6):

        for j in range(7):
            print("[" + grid[j + 7*i] + "]", end="")

        print()
    
    for j in range(7):
        print(" " + str(j + 1) + " ", end="")
    
    print("\n")
        

def pHoriWin(grid):
    """
    Check if the player has won with a horizontal line.
    
    Args:
        grid (list): The grid being played on
    
    Returns:
        bool: returns True if the player has met the winning condition, else returns False

    """
    count = 0

    # Iterate over the grid from left to right, then top to bottom
    for i in range(6):

        for j in range(7):

            index = j + 7*i
            
            if grid[index] == 'x':
                count += 1
            if grid[index] != 'x':
                count = 0
            if count == 4:
                return True
        
        if i == 5:
            return False
    

def pVertWin(grid):
    """
    Check if the player has won with a vertical line.
    
    Args:
        grid (list): The grid being played on
    
    Returns:
        bool: returns True if the player has met the winning condition, else returns False

    """
    count = 0

    # Iterate over the grid from top to bottom, then left to right
    for i in range(7):

        for j in range(6):

            index = i + 7*j

            if grid[index] == 'x':
                count += 1
            if grid[index] != 'x':
                count = 0
            if count == 4:
                return True
        
        if i == 6:
            return False


def pDiagWin(grid):
    """
    Check if the player has won with a diagonal line.
    
    Args:
        grid (list): The grid being played on
    
    Returns:
        bool: returns True if the player has met the winning condition, else returns False

    """
    # To help visualize this function, imagine that the cursor starts and ends outside of the grid 
    
    count = 0

    # Iterate over the grid from top to bottom, then left to right
    for i in range(-2, 4):

        for j in range(6):

            index = i + 8*j     # Select the slot in a diagonal from top-left to bottom-right

            if (index == 4 or
                index == 5 or
                index == 6 or
                index == 12 or
                index == 13 or
                index == 20 or
                index == 21 or
                index == 28 or
                index == 29 or
                index == 35 or
                index == 36 or
                index == 37 or
                index > 41 or
                index < 0):
                continue        # Ignore the corners of the board where its impossible to form a big enough line

            if grid[index] == 'x':
                count += 1
            if grid[index] != 'x':
                count = 0
            if count == 4:
                return True

        count = 0       # Make sure the count isn't allowed to wrap around the table diagonally

    # Iterate over the grid from top to bottom, then left to right  
    for i in range(3, 9):

        for j in range(6):
            
            index = i + 6*j     # Select the slot in a diagonal from top-right to bottom-left
            
            if (index == 0 or
                index == 1 or
                index == 2 or
                index == 7 or
                index == 8 or
                index == 14 or
                index == 27 or
                index == 33 or
                index == 34 or
                index == 39 or
                index == 40 or
                index == 41 or
                index > 41 or
                index < 0):
                continue        # Ignore the corners of the board where its impossible to form a big enough line

            if grid[index] == 'x':
                count += 1
            if grid[index] != 'x':
                count = 0
            if count == 4:
                return True
        
        count = 0       # Make sure the count isn't allowed to wrap around the table diagonally

    return False


def bHoriWin(grid):
    """
    Check if the bot has won with a horizontal line.
    
    Args:
        grid (list): The grid being played on
    
    Returns:
        bool: returns True if the bot has met the winning condition, else returns False

    """
    count = 0

    # Iterate over the grid from left to right, then top to bottom
    for i in range(6):

        for j in range(7):

            index = j + 7*i
            
            if grid[index] == 'o':
                count += 1
            if grid[index] != 'o':
                count = 0
            if count == 4:
                return True
        
        if i == 5:
            return False
    

def bVertWin(grid):
    """
    Check if the bot has won with a vertical line.
    
    Args:
        grid (list): The grid being played on
    
    Returns:
        bool: returns True if the bot has met the winning condition, else returns False

    """
    count = 0

    # Iterate over the grid from top to bottom, then left to right
    for i in range(7):

        for j in range(6):

            index = i + 7*j

            if grid[index] == 'o':
                count += 1
            if grid[index] != 'o':
                count = 0
            if count == 4:
                return True
        
        if i == 6:
            return False


def bDiagWin(grid):
    """
    Check if the bot has won with a diagonal line.
    
    Args:
        grid (list): The grid being played on
    
    Returns:
        bool: returns True if the bot has met the winning condition, else returns False

    """
    # To help visualize this function, imagine that the cursor starts and ends outside of the grid 
    
    count = 0

    # Iterate over the grid from top to bottom, then left to right
    for i in range(-2, 4):

        for j in range(6):

            index = i + 8*j     # Select the slot in a diagonal from top-left to bottom-right
            
            if (index == 4 or
                index == 5 or
                index == 6 or
                index == 12 or
                index == 13 or
                index == 20 or
                index == 21 or
                index == 28 or
                index == 29 or
                index == 35 or
                index == 36 or
                index == 37 or
                index > 41 or
                index < 0):
                continue        # Ignore the corners of the board where its impossible to form a big enough line

            if grid[index] == 'o':
                count += 1
            if grid[index] != 'o':
                count = 0
            if count == 4:
                return True

        count = 0       # Make sure the count isn't allowed to wrap around the table diagonally

    # Iterate over the grid from top to bottom, then left to right  
    for i in range(3, 9):

        for j in range(6):
            
            index = i + 6*j     # Select the slot in a diagonal from top-right to bottom-left
            
            if (index == 0 or
                index == 1 or
                index == 2 or
                index == 7 or
                index == 8 or
                index == 14 or
                index == 27 or
                index == 33 or
                index == 34 or
                index == 39 or
                index == 40 or
                index == 41 or
                index > 41 or
                index < 0):
                continue        # Ignore the corners of the board where its impossible to form a big enough line

            if grid[index] == 'o':
                count += 1
            if grid[index] != 'o':
                count = 0
            if count == 4:
                return True
        
        count = 0       # Make sure the count isn't allowed to wrap around the table diagonally

    return False


def addCheckerX(grid, col):
    """
    Place an X checker in the column specified.
    
    Args:
        grid (list): The grid being played on
        col (int): The column where a checker is to be placed
    """
    for i in range(5, -1, -1):

        if grid[7*i + col - 1] == " ":
            grid[7*i + col - 1] = "x"
            break


def addCheckerO(grid, col):
    """
    Place an X checker in the column specified.
    
    Args:
        grid (list): The grid being played on
        col (int): The column where a checker is to be placed
    """
    for i in range(5, -1, -1):

        if grid[7*i + col - 1] == " ":
            grid[7*i + col - 1] = "o"
            break
