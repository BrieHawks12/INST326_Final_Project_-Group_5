from Classes import BoardSpace

#using inheratince technique with BoardSpace
class Just_Visiting_Space(BoardSpace):
    #method overriding-polymorphism
    def land_on(self, player):
        """
        Uses polymorphism to establish that a player has landed on just visiting jail
        
        Args:
        self: instance of the class
        player: player that landed on chance
        
        
        Returns:
        string: f string that the player landed on just visiting jail 
        
        Author: Bristow
       
        """
        print (f"{player.name} is just visiting jail.")