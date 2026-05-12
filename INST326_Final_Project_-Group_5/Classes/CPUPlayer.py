from Classes.Player import Player
import random

class CPUPlayer(Player):
    """
    Represents CPU player to play against human player.
    """
    
    def __init__(self,name,piece,balance=1500):
        """
        Initializes CPU player
        Args:
            name(str):CPU name
            piece(str): CPU token piece
            balance(int): Starting balance
        Author: Melanie Abzun
        """
        super().__init__(name,piece,balance)
    @property
    def is_cpu(self):
        """
        Indicates that this player is the CPU
        Author: Melanie Abzun
        """
        return True
    
    def decide_to_buy(self,space):
        """
        Uses random to decide if CPU will purchase property.
        Args:
            space(OwnableSpace):Property thats being considered
        Return:
            boolean: True is CPU buys, False if otherwise.
        Author: Melanie Abzun
        """
        if self._balance < space.price:
            return False
        return random.choice([True, False]) 
        