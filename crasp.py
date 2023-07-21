from die import Die

class Player:
    def __init__(self):
        self.roll = ""
        self.rollsCount = 0
        self.atStartup = True
        self.winner = False
        self.loser = False

    def rollDice(self):
        dice1 = Die()
        dice2 = Die()
        dice1.roll()
        dice2.roll()
        total = dice1.getValue() + dice2.getValue()
        self.roll = f"{dice1.getValue()}, {dice2.getValue()}"
        if self.atStartup:
            self.atStartup = False
            self.firstRoll = total
            if total in (7, 11):
                self.winner = True
            elif total in (2, 3, 12):
                self.loser = True
        else:
            if total == 7:
                self.loser = True
            elif total == self.firstRoll:
                self.winner = True
        self.rollsCount += 1
        return dice1.getValue(), dice2.getValue()

    def getNumberOfRolls(self):
        return self.rollsCount

    def isWinner(self):
        return self.winner

    def isLoser(self):
        return self.loser

def playOneGame():
    player = Player()
    print("Rolling the dice...")
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
