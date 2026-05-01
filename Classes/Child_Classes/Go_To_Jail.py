from Classes import BoardSpace

#using inheratince technique with BoardSpace
class Go_To_Jail_Space(BoardSpace):
    #method overriding-polymorphism
    def land_on(self, player):
        """
        Uses polymorphism to establish that a player has landed on go to jail
        
        Args:
        self: instance of the class
        player: player that landed on chance
        
        
        Returns:
        string: f string that the player landed on go to jail 
        
        Author: Bristow
       
        """
        print (f"{player.name} landed on go to jail.")
        player.go_to_jail()