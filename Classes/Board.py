#from filename import classname     
from BoardSpace import BoardSpace
       
class Board:
    def __init__(self):
        """
        Creates the Monopoly board as list
        
        Arg:
        self: instance of the class
        
        Returns:
            
        
        Authors: Briana Bristow
        """
        self.spaces = self.create_board()
     
    #Creates Monopoly Board in order    
    def create_board(self):
        """
        Creates the Monopoly board as list
        
        Arg:
        self: instance of the class
        
        Returns:
            list: UMD buildings as property with prices
        
        Authors: All team members collaborated
        """
        
        return[
            BoardSpace( 0, "Go", "go", 0),
            BoardSpace(1, "Adele H. Stamp Student Union", "property", 60),
            BoardSpace(2, "Community Chest", "community_chest", 0),
            BoardSpace(3,  "H.J. Patterson Hall", "property", 60),
            BoardSpace(4, "Income Tax",  "tax", 0),
            BoardSpace(5, "Reading Railroad",  "railroad", 200),#purple line??
            BoardSpace(6, "McKeldin Library", "property", 100),
            BoardSpace(7, "Chance",  "chance",0),
            BoardSpace(8, "Edward St. John Learning & Teaching Center","property",100),
            BoardSpace(9, "Microbiology Building ",  "property",  120),
            
            BoardSpace(10, "Jail\Just Visiting", "jail", 0),
            BoardSpace(11,  "Hornbake Library", "property", 140),
            BoardSpace(12, "Electric Company", "utility", 140),
            BoardSpace(13,  "States Avenue",  "property",  140),
            BoardSpace(14,  "Virginia Avenue",  "property",  160),
            BoardSpace(15,  "Pennsylvania Railroad", "railroad",200),
            BoardSpace(16, "St. James Place", "property", 180),
            BoardSpace(17, "Community Chest", "community_chest", 0),
            BoardSpace(18, "Tennessee Avenue", "property", 180),
            BoardSpace(19, "New York Avenue", "property", 200),
            
            BoardSpace(20, "Free Parking", "free_parking", 0),
            BoardSpace(21, "Plants and Science", "property", 220),
            BoardSpace(22, "Chance", "chance", 0),
            BoardSpace(23, "Cole Activities Building", "property", 220),
            BoardSpace(24, "Jule Hall", "property", 240),
            BoardSpace(25, "B. & O. Railroad", "railroad", 200),
            BoardSpace(26, "Martin Hall", "property", 260),
            BoardSpace(27, "Symons Hall", "property", 260),
            BoardSpace(28, "Water Works", "utility", 150),

            BoardSpace(29, "Xfinity Center", "property", 280),
            BoardSpace(30, "Go To Jail", "go_to_jail", 0),
            BoardSpace(31, "Tawes Hall", "property", 300),
            BoardSpace(32, "Shoemaker Bldg", "property", 300),
            BoardSpace(33, "Community Chest", "community_chest", 0),
            BoardSpace(34, "Tydings Hall", "property", 320),
            BoardSpace(35, "Shuttle-UM", "railroad", 200),
            BoardSpace(36, "Chance", "chance", 0),
            BoardSpace(37, "Park Lot 1", "property", 350),
            BoardSpace(38, "Parking Citaion", "tax", 0),
            BoardSpace(39, "Reckord Armory", "property", 400)
                       
        ]                  
                        
           
          
           
        
    def get_space(self, position):
        """
        Returns the postion of the player at the given moment in the gameplay
        
        Args:
        self:instance of a class
        postion:postion on a board
        
        Returns:
        list: postion on the board
        
        Author: Briana Bristow
        """
        
        return self.spaces[position]
    
    
    def move_postion(self, current_postion:int, steps:int)-> int:
        """
        Calculates board position after moving steps
        Args: 
            current_postion:player's current positon
            steps: numper of spaces forward
            
        Returns:
            int: new position space
        Author: Melanie Abzun
        """
        new_postion = (current_postion + steps) % len(self.spaces)
        return new_postion
    
#Below are used for testing purposes    
b1 = Board()
space = b1.get_space(35)
print(space)

new_postion = b1.move_postion(38,5)
print(new_postion)



        
    
    