from abc import abstractmethod 

class BoardSpace(ABC):
    def __init__(self, position, name, category, price=0):
        """
        Creates the BoardSpace class
        
        Arg:
        self: instance of the class
        position:position on the board
        name: name of board space
        category: category of board space
        price: price of board space
        
        Returns: Nothing
            
        Authors: Briana Bristow
        """
        #encapsolation technique being used by position and name
        self._position = position
        self._name = name
        self.category = category
        self.price = price
        
    @property    
    def position(self):
        """
        getter that allows the use of the postion attribute
        
        Args:
        self: instance of the class
        
        
        Returns:
        string: postion on the board
        
        Author: Bristow
       
        """
        return self._position
        
    @property
    def name(self):
        """
        getter that allows the use of the name attribute
        
        Args:
        self: instance of the class
     
        Returns:
        string: name of the player
        
        Author: Bristow
       
        """
        return self._name
    
    @abstractmethod
    def land_on(self, player):
        """
        Outlines what space a player lands on and the actions that happen based on the space
        
        Args:
        self: instance of the class
     
        Returns:
        string: name of the player
        
        Author: Bristow
           
        """
        
        pass
       

    def is_purchasable(self):
        """
        determines if space on the board is available for purchase
        
        Arg:
        self: instance of the class
        
        Returns:
            boolean: True or False
        
        Authors: Briana Bristow
        """
        if self.category in ["property","railroad","utility"]:
            return True
    
    def __str__(self):
        """
        Creates string with certain criteria 
        
        Arg:
        self: instance of the class
        
        Returns:
            string: name, category and price on the space on the board. 
        
        Authors: Briana Bristow
        """
        return f"{self.poistion}: {self.name} {self.category} - ${self.price}"
               