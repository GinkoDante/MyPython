class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

# The Pass the Ball game involves players passing a potato from
# one person to the next
# We can simulate who has the potato by using a queue ogf the players
# names and constantly queueing and dequeue the players a
# number of times and removing the person at the front of the queue

def hotPotato(playersList, numPasses):

    playerQueue = Queue()

    for playerName in playersList:
        playerQueue.enqueue(playerName)

    while playerQueue.size() > 1:

        for passIndex in range(numPasses):
            oldFirstPlayer = playerQueue.dequeue()
            playerQueue.enqueue(oldFirstPlayer)

        # Remove first player with ball permanently
        playerQueue.dequeue()


    return playerQueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))