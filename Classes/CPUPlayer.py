from Classes.Player import Player

class CPUPlayer(Player):
    def __init__(self,name,piece,balance=1500):
        super().__init__(name,piece,balance)
    @property
    def is_cpu(self):
        return True