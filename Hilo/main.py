import random

#Classes (Cards and Score)
class cards:
    def __init__(self):
        self.currentNumber = random.randint(1, 13)
        self.nextNumber = random.randint(1, 13)

    def startGame(self):
        print(f"The card is:{self.currentNumber}")
        userStatus = input("Higher or lower? (h/l): ")
        realStatus = self.cardStatusDefinition()
        self.cardComparison(realStatus, userStatus)

    def cardStatusDefinition(self):
        return "h" if self.currentNumber > self.nextNumber else "l"       

    def cardComparison(self, realStatus, userStatus):
        scores.sumScore(scores, 100) if realStatus == userStatus else scores.subsScore(scores, 75)
            

class scores:
    def __init__(self):
        self.currentScore = 0
    
    def sumScore(self, lastScore):
        self.currentScore + lastScore
        self.print()

    def subsScore(self, lastScore):
        self.currentScore - lastScore
        self.print()
    
    def print(self):
        print(self.currentScore)

def main():
    score = scores()
    card = cards()
    card.startGame()

if __name__ == "__main__":
    main()
