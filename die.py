import random

class Die:
    def __init__(self):
        self.value = 1

    def roll(self):
        self.value = random.randint(1, 6)

    def getValue(self):
        return self.value
