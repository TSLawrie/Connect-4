#! python -u

"""Program to play Connect Four in your terminal."""


from c4_tools import printGrid, pHoriWin, pVertWin, pDiagWin, bHoriWin, bVertWin, bDiagWin, addCheckerX, addCheckerO
from random import randint
from time import sleep


print("\nWelcome to Connect 4 for Terminal!")

while True:
    choice = input("1 player or 2 players?\nPlease enter [1] or [2]: ")
    if choice == "1" or choice == "2":
        break

print("Here is the board you'll be playing with:")

grid = [" ", " ", " ", " ", " ", " ", " ",
        " ", " ", " ", " ", " ", " ", " ",
        " ", " ", " ", " ", " ", " ", " ",
        " ", " ", " ", " ", " ", " ", " ",
        " ", " ", " ", " ", " ", " ", " ",
        " ", " ", " ", " ", " ", " ", " "]

printGrid(grid)

if choice == "1":
    print("""You'll play against a bot, taking it in turns to place your checkers in columns 1 to 7.\nThe slots you fill with checkers will be represented by an 'x' and the ones the bot fills with an 'o'.\nHave fun!""")
if choice == "2":
    print("""Take it in turns to place your checkers in colums 1 to 7.\nThe slots that Player 1 fills with checkers will be represented by an 'x' and the ones that Player 2 fills by an 'o'.\nHave fun!""")

if choice == "1":

    turn = 0

    while True:

        print("--------------------")

        if pHoriWin(grid) or pVertWin(grid) or pDiagWin(grid):
            print("Congratulations, you won!")
            printGrid(grid)
            break

        if bHoriWin(grid) or bVertWin(grid) or bDiagWin(grid):
            print("Too bad, you lost.")
            printGrid(grid)
            break

        if turn % 2 == 0:

            print("Player turn:")
            printGrid(grid)

            while True:

                column = input("Please enter the column you would like to put your checker in (1-7): ")
                if not column.isdigit():
                    continue
                
                col = int(column)
                if col >= 1 and col <= 7:
                    break
            
            addCheckerX(grid, col)

        if turn % 2 == 1:

            print("Bot turn:")
            printGrid(grid)

            col = randint(1, 7)     # Generate a random number from 1 to 7 (inclusive)
            addCheckerO(grid, col)

            print("Column selected by bot: ", end="")
            sleep(3)
            print(col)

        sleep(1)
        turn += 1

if choice == "2":

    turn = 0

    while True:

        print("--------------------")

        if pHoriWin(grid) or pVertWin(grid) or pDiagWin(grid):
            print("Player 1 wins!")
            printGrid(grid)
            break

        if bHoriWin(grid) or bVertWin(grid) or bDiagWin(grid):
            print("Player 2 wins!")
            printGrid(grid)
            break

        if turn % 2 == 0:

            print("Player 1 turn:")
            printGrid(grid)

            while True:

                column = input("Please enter the column you would like to put your checker in (1-7): ")
                if not column.isdigit():
                    continue
                
                col = int(column)
                if col >= 1 and col <= 7:
                    break
            
            addCheckerX(grid, col)

        if turn % 2 == 1:

            print("Player 2 turn:")
            printGrid(grid)

            while True:

                column = input("Please enter the column you would like to put your checker in (1-7): ")
                if not column.isdigit():
                    continue
                
                col = int(column)
                if col >= 1 and col <= 7:
                    break
            
            addCheckerO(grid, col)

        sleep(1)
        turn += 1