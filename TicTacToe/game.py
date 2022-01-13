from prettytable import PrettyTable
import os

#Function to clear the screen
def cls():
    os.system("cls")

#Texts of prints and messages
def generalMessages():
    #First phase
    introPhaseOne = "Welcome to: TIC-TAC-TOE"
    getUserName_X = "\nPlease enter the name of the first player (x): "
    getUserName_O = "Please enter the name of the second player (o): "
    
    #Second phase
    introPhaseTwo = "Perfect! Now les't go to set the Grid\n"
    getGrid = "How many rows and columns do you want your grid?: "

    #Dictionary with all the text
    messagesDict = {
        #Fisrt Phase
        "introPhaseOne": introPhaseOne,
        "getUserName_X": getUserName_X,
        "getUserName_O": getUserName_O,

        #Second phase
        "introPhaseTwo": introPhaseTwo,
        "getGrid": getGrid
    }
    return messagesDict

def main():
    #Global variables
    text = generalMessages()

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

if __name__ == "__main__":
    main()