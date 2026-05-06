from Classes.BoardSpace import BoardSpace

#using inheratince technique with BoardSpace
class Chance_Space(BoardSpace):
    
    def __init__(self, position, name):
    
        super().__init__(position, name, "chance", 0)
    #method overriding-polymorphism
    def land_on(self, player):
        """
        Uses polymorphism to establish that a player has landed on Chance
        
        Args:
        self: instance of the class
        player: player that landed on chance
        
        
        Returns:
        string: f string that the player landed on Chance
        
        Author: Bristow

        """
        player.gain_money(100)
        print (f"{player.name} landed on chance and recieved $100")