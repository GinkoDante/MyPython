import random

class Player:

    def __init__(self, id):
        self.id = id
        self.handValue = 0
        self.numCards = 0
        self.busted = False

    def updateHand(self, newCardValue):
        self.handValue += newCardValue

    def updateNumCards(self):
        self.numCards += 1

    def testBust(self):

        if self.handValue > 21:
            self.busted = True

        else:
            self.busted = False

        return self.busted

    def testWinner(self):
        if self.handValue == 21:
            return True
        else:
            return False

    def getID(self):
        return self.id

    def getHand(self):
        return self.handValue

def BlackJackSim(numPlayers):

    playerList = []

    for playerID in range(numPlayers):
        player = Player(playerID)
        playerList.append(player)

    winner = False

    while (not winner):

        for index in range(len(playerList)-1):
            playerList[index].updateHand(random.randrange(1, 11))

            if playerList[index].testBust():
                # Remove player from game
                del playerList[index]

            if playerList[index].testWinner():
                winner = True
                winnerIndex = index

    print("The winner is ", playerList[winnerIndex])


BlackJackSim(4)