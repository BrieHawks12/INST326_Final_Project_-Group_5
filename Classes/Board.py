#from filename import classname     
#from BoardSpace import BoardSpace
from Classes.Child_Classes.Go_Space import Go_Space
from Classes.Child_Classes.Property_Space import Property_Space
from Classes.Child_Classes.Community_Chest_Space import Community_Chest
from Classes.Child_Classes.Tax_Space import Tax_Space
from Classes.Child_Classes.Chance_Space import Chance_Space
from Classes.Child_Classes.Just_Visiting_Space import Just_Visiting_Space
from Classes.Child_Classes.Free_Parking_Space import Free_Parking_Space
from Classes.Child_Classes.Go_To_Jail import Go_To_Jail_Space
from Classes.Child_Classes.Railroad_Space import Railroad_Space
from Classes.Child_Classes.Utility_Space import Utility_Space
       
class Board:
    def __init__(self):
        """
        Creates the Monopoly board as list
        
        Arg:
        self: instance of the class
        
        Returns:
            
        
        Authors: Briana Bristow
        """
        self._spaces = self._create_board()
        
    @property
    def spaces(self):
        return self._spaces
        
    
     
    #Creates Monopoly Board in order    
    def _create_board(self):
        """
        Creates the Monopoly board as list
        
        Arg:
        self: instance of the class
        
        Returns:
            list: UMD buildings as property with prices
        
        Authors: Bristow, Zhang, Abzun
        """
        
        return [

            Go_Space(0, "Go"),
            Property_Space(1, "Adele H. Stamp Student Union", 60, 2),
            Community_Chest(2, "Community Chest"),
            Property_Space(3, "H.J. Patterson Hall", 60, 4),
            Tax_Space(4, "Income Tax", 100),
            Railroad_Space(5, "Metro Green Line", 200),
            Property_Space(6, "McKeldin Library", 100, 6),
            Chance_Space(7, "Chance"),
            Property_Space(8, "Edward St. John Learning & Teaching Center", 100, 6),
            Property_Space(9, "Microbiology Building ", 120, 8),
            Just_Visiting_Space(10, "Jail / Just Visiting"),
            Property_Space(11, "Hornbake Library", 140, 10),
            Utility_Space(12, "UMD Electricity", 140),
            Property_Space(13, "Stem Library", 140, 10),
            Property_Space(14, "Brendon Iribe Building", 160, 12),
            Railroad_Space(15, "College Park Metro", 200),
            Property_Space(16, "Skinner Building", 180, 14),
            Community_Chest(17, "Community Chest"),
            Property_Space(18, "A James Clark", 180, 14),
            Property_Space(19, "Glenn L. Martin Hall", 200, 16),
            Free_Parking_Space(20, "Free Parking"),
            Property_Space(21, "Plants and Science", 220, 18),
            Chance_Space(22, "Chance"),
            Property_Space(23, "Cole Activities Building", 220, 18),
            Property_Space(24, "Jule Hall", 240, 20),
            Railroad_Space(25, "Purple Line", 200),
            Property_Space(26, "Martin Hall", 260, 22),
            Property_Space(27, "Symons Hall", 260, 22),
            Utility_Space(28, "UMD Water System", 150),
            Property_Space(29, "Xfinity Center", 280, 24),
            Go_To_Jail_Space(30, "Go To Jail"),
            Property_Space(31, "Tawes Hall", 300, 26),
            Property_Space(32, "Shoemaker Bldg", 300, 26),
            Community_Chest(33, "Community Chest"),
            Property_Space(34, "Tydings Hall", 320, 28),
            Railroad_Space(35, "Shuttle-UM", 200),
            Chance_Space(36, "Chance"),
            Property_Space(37, "Park Lot 1", 350, 35),
            Tax_Space(38, "Parking Citation", 100),
            Property_Space(39, "Reckord Armory", 400, 50)

        ]     
                        
           
          
           
        
    def get_space(self, position):
        """
        Returns the position of the player at the given moment in the gameplay
        
        Args:
        self:instance of a class
        position:position on a board
        
        Returns:
        list: position on the board
        
        Author: Bristow
        """
        
        return self.spaces[position]
    
    
    def move_position(self, current_position:int, steps:int)-> int:
        """
        Calculates board position after moving steps
        Args: 
            current_position:player's current positon
            steps: numper of spaces forward
            
        Returns:
            int: new position space
        Author: Melanie Abzun
        """
        new_position = (current_position + steps) % len(self.spaces)
        return new_position
    
    def board_size(self):
       return 40 
    
#Below are used for testing purposes    
#b1 = Board()
#space = b1.get_space(35)
#print(space)

#new_position = b1.move_position(38,5)
#print(new_position)



        
    
    