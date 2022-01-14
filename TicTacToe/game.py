import os, random
from ssl import Options
from tabulate import tabulate

#Function to clear the screen
def cls():
    os.system("cls")

#Texts of prints and messages
def generalMessages():
    #Dictionary with all the text
    messagesDict = {
        #First Phase
        "introPhaseOne": "Welcome to: TIC-TAC-TOE",
        "getUserName_X": "\nPlease enter the name of the first player (x): ",
        "getUserName_O": "Please enter the name of the second player (o): ",

        #Second phase
        "introPhaseTwo": "Perfect! Now les't go to set the Grid\n",
        "getGrid": "How many rows and columns do you want your grid? (minimun 3): ",

        #Third phase
        "introPhaseThree": "Let's play!\n",
        "endGame": "Thank you for playing!"
    }
    return messagesDict

#Function to generate the Grid
def generateGrid(grid):
        #General variabels
        gridMatrix = []
        Columns = int(grid)
        counter = 1

        #Generate brutal matriz
        for i in range(Columns):
            gridMatrix.append([i])
            gridMatrix[i].pop()
            for _ in range(Columns):                
                gridMatrix[i].append(counter)
                counter = counter + 1
        return gridMatrix, True

#Function to change the Grid
def modifyGrid(grid, userChoice, userID):
        try:
            elementIndex = find(userChoice, grid)
            grid[elementIndex[0]][elementIndex[1]] = userID
            return grid, True
        except:
            return grid, False
        

#Funtion to get the index of a matrix 
def find(element, matrix):
    element = int(element)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                return (i, j)

#print Grid
def printGrid(grid):
    print(tabulate(grid, tablefmt='grid'))

def verifyGrid(grid):
    return True

def main():
    #Global variables
    text = generalMessages()
    options = ["O", "X"]

    #Introduction message
    cls()
    print(text["introPhaseOne"])

    #Get users names
    userName_X = input(text["getUserName_X"])
    userName_O = input(text["getUserName_O"])

    #Create the Grid -  Phase two
    cls()
    print(text["introPhaseTwo"])
    getGrid = input(text["getGrid"])

    #Generate and print the Grid
    cls()
    print(text["introPhaseThree"])
    grid = generateGrid(getGrid)
    printGrid(grid[0])

    #ask options and rewrite the grid
    controlLoop = True
    controlUser = random.choice(options)
    while controlLoop:
        if controlUser == "O":
            userChoice = input(f"{userName_O.capitalize()}({controlUser}), your turn: ")
        if controlUser == "X":
            userChoice = input(f"{userName_X.capitalize()}({controlUser}), your turn: ")

        #Reprint new grid
        grid = modifyGrid(grid[0], userChoice, controlUser)
        if not grid[1]:
            print("This cell have being selected, choose other one...")
        else:
            cls()
            printGrid(grid[0])
        
            #Change the user
            if controlUser == "X":
                controlUser = "O"
            else:
                controlUser = "X"

        #Verify grid
        controlLoop = verifyGrid(grid[0])
    
    print(text["endGame"])

if __name__ == "__main__":
    main()