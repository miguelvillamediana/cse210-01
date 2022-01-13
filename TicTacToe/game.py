def generalMessages():
    intro = "Welcome to: TIC-TAC-TOE"
    getUserName_X = "\nPlease enter the name of the first player (x): "
    getUserName_O = "Please enter the name of the second player (o): "

    messagesDict = {
        "intro": intro,
        "getUserName_X": getUserName_X,
        "getUserName_O": getUserName_O 
    }
    return messagesDict


def main():
    #Global variables
    gridGame = []
    text = generalMessages()

    #Introduction message
    print(text["intro"])

    #Get users names
    userName_X = input(text["getUserName_X"])
    userName_O = input(text["getUserName_O"])

if __name__ == "__main__":
    main()