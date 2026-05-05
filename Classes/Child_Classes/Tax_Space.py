from Classes.BoardSpace import BoardSpace

class Tax_Space(BoardSpace):
    def __init__(self, position, name, tax_amount):
        """
        Creating class Tax_Space and inherated postion and name from BoardSpace
        
        Args:
        self: instance of the class
        position: postion on the board
        name: name of the player
        tax_amount: amount of tax
                
        Returns:
        nothing
        
        Author: Bristow
       
        """
        super().__init__(position, name, "tax", 0)
        self._tax_amount = tax_amount
        
    @property
    #encapsulation
    def tax_amount(self):
        """
        getter that allows access the _tax_amount attribute
        
        Args:
        self: instance of the class
                   
        Returns:
        int tax amount
        
        Author: Bristow
       
        """
        return self._tax_amount
    
    def land_on(self, player):
        """
        uses Player class so that money can be subtracted from a user 
        
        Args:
        self: instance of the class
        player: name of the player
       
                
        Returns:
        string: f string of the summary of the user has to pay
        
        Author: Bristow
       
        """
        player.pay_money(self.tax_amount)
        print (f"{player.name} landed on {self.name} and paid ${self.tax_amount}")
        
            