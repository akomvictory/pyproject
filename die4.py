import random

class Player:
    def __init__(self):
        self.roll = None
        self.rollsCount = 0
        self.atStartup = True
        self.winner = False
        self.loser = False

    def rollDice(self):
        if self.atStartup:
            self.roll = self._getDiceValues()
            self.atStartup = False
            self.rollsCount = 1
        else:
            self.roll = self._getDiceValues()
            self.rollsCount += 1
            if sum(self.roll) in (2, 3, 12):
                self.loser = True
            elif sum(self.roll) in (7, 11):
                self.winner = True

        return self.roll

    def getRollsCount(self):
        return self.rollsCount

    def isWinner(self):
        return self.winner

    def isLoser(self):
        return self.loser

    def getNumberOfRolls(self):
        return self.rollsCount

    def _getDiceValues(self):
        return (random.randint(1, 6), random.randint(1, 6))

def playOneGame():
    player = Player()
    while not player.isWinner() and not player.isLoser():
        roll = player.rollDice()
        print(f"Roll {player.getRollsCount()}: {roll}")
    if player.isWinner():
        print("Congratulations! You won!")
    else:
        print("Sorry, you lost.")

def playManyGames(num_games):
    for _ in range(num_games):
        print("Playing a new game...")
        playOneGame()
        print("=" * 30)

# Example usage:
playManyGames(3)  # Play 3 games
