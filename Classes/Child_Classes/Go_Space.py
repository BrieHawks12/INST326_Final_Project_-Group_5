from Classes.BoardSpace import BoardSpace

#using inheratince technique with BoardSpace
class Go_Space(BoardSpace):
    #method overriding-polymorphism
    def __init__(self, position, name):
    
        super().__init__(position, name, "go", 200)
        
    def land_on(self, player):
        """
        Uses polymorphism to establish that a player has landed on Go
        
        Args:
        self: instance of the class
        player: player that landed on chance
        
        
        Returns:
        string: f string that the player landed on Go
        
        Author: Bristow

        
        """
        print (f"{player.name} land on GO.")
    