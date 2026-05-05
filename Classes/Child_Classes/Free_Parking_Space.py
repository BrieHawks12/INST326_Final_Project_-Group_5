from Classes.BoardSpace import BoardSpace

#using inheratince technique with BoardSpace
class Free_Parking_Space(BoardSpace):
    #method overriding-polymorphism
    def __init__(self, position, name):
    
        super().__init__(position, name, "free_parking", 0)
    
    def land_on(self, player):
        """
        Uses polymorphism to establish that a player has landed on Free Parking
        
        Args:
        self: instance of the class
        player: player that landed on chance
        
        
        Returns:
        string: f string that the player landed on Free Parking 
        
        Author: Bristow

        
        """
        print (f"{player.name} land on Free Parking, nothing happens.")