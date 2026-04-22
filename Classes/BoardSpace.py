class BoardSpace:
    def __init__(self, position, name, category, price=0):
        """
        Creates the BoardSpace class
        
        Arg:
        self: instance of the class
        postion:position on the board
        name: name of board space
        category: category of board space
        price: price of board space
        
        Returns:
            
        
        Authors: Briana Bristow
        """
        
        
        
        self.poistion = position
        self.name = name
        self.category = category
        self.price = price
       

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
               