from Classes import BoardSpace

#using inheratince technique with BoardSpace
class Community_Chest(BoardSpace):
    #method overriding-polymorphism
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
        
        print (f"{player.name} landed on Community Chest")