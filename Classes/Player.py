class Player:
    def __init__(self, name, piece, balance):
        """
        Initialize a player with name, piece, and starting balance
        Args: name (str), piece (str), balance (int)
        Returns: None
        Author: Zhang
        """
        self.name = name
        self.piece = piece
        self.balance = balance
        self.properties = []
        self.position = 0
        
    def pay_money(self, amount):
        """
        Deduct a certain amount of money from the player's balance
        Arg: amount(int)
        Return: None
        Author: Zhang
        """
        self.balance -= amount
    
    def gain_money(self, amount):
        """
        Increase a certain amount of money in the player's balance
        Arg: amount(int)
        Return: None
        Author: Zhang
        """
        self.balance += amount
        
    def buy_property(self, property):
        """Check if the player's balance can afford the property,
        if so, add property to the player's properties and deduct price money;
        Arg: property(obj) - Property obj not yet created
        Return: True if affordable, False otherwise
        Author: Zhang"""
        if self.balance >= property.price:
            self.balance = self.balance - property.price
            self.properties.append(property)
            return True
        else:
            return False
            
    def move(self, steps, board):
        """Move the player piece's position on the board
        Arg: steps(int), board(obj)
        Return: None
        Author: Zhang"""
        self.position = board.move_position(self.position, steps)
    
    def player_current_space(self, board):
        """Check the player piece's current location on the board
        Arg: board(obj)
        Return: An int represents the piece's position
        Author: Zhang"""
        return board.get_space(self.position)
    
    