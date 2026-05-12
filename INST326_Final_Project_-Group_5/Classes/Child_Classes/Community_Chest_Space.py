from Classes.BoardSpace import BoardSpace

#using inheratince technique with BoardSpace
class Community_Chest(BoardSpace):
    #method overriding-polymorphism
    def __init__(self, position, name):
    
        super().__init__(position, name, "community_chest", 0)
    
    def land_on(self, player):
        """
        Uses polymorphism to establish that a player has landed on Community Chest
        
        Args:
        self: instance of the class
        player: player that landed on chance
        
        
        Returns:
        string: f string that the player landed on Community Chest
        
        Author: Bristow

        
        """
        player.gain_money(100)
        print (f"{player.name} landed on Community Chest and recieved $100")