import random

class Player:
    def __init__(self):
        self.roll = ""
        self.rollsCount = 0
        self.atStartup = True
        self.winner = False
        self.loser = False

    def rollDice(self):
        if self.atStartup:
            self.roll = self._rollDice()
            self.atStartup = False
        else:
            self.roll = self._rollDice()
            if self.roll == "7":
                self.loser = True
            elif self.roll == self.firstRoll:
                self.winner = True
        self.rollsCount += 1
        return tuple(map(int, self.roll.split(",")))

    def getNumberOfRolls(self):
        return self.rollsCount

    def isWinner(self):
        return self.winner

    def isLoser(self):
        return self.loser

    def _rollDice(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        return f"{dice1},{dice2}"

def playOneGame():
    player = Player()
    while not player.isWinner() and not player.isLoser():
        input("Press Enter to roll the dice...")
        dice_values = player.rollDice()
        print(f"Roll {player.getNumberOfRolls()}: {dice_values[0]} + {dice_values[1]} = {sum(dice_values)}")
    if player.isWinner():
        print("Congratulations! You win!")
    else:
        print("Oops! You rolled a 7. You lose!")

def playManyGames(num_games):
    for game in range(num_games):
        print(f"\nGame {game+1}:")
        playOneGame()

# Example usage:
playManyGames(3)
