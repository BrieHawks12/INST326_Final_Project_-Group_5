import random

class Dice:
    def roll_dice(self):
        """
        Rolls two six sided dice
        Returns:
            int: Total of the two dice rolls. Max of 12
        Author: Melanie Abzun
        """
        dice1= random.randint(1,6)
        dice2 =random.randint(1,6)
        return dice1+dice2