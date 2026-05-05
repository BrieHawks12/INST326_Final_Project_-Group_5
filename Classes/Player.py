class Player:
    def __init__(self, name, piece, balance=1500):
        """
        Initialize a player with name, piece, and starting balance
        Args: name (str), piece (str), balance (int)
        Returns: None
        Author: Zhang
        Author: Bristow (added injail, and _ to balance, name and position, set balance=1500)
        """
        self._name = name
        self.piece = piece
        self._balance = balance
        self._in_jail = False
        self.properties = []
        self._position = 0
        
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
    def balance(self):
        """
        getter that allows the use of the balance attribute
        
        Args:
        self: instance of the class
     
        Returns:
        int: players balance
        
        Author: Bristow
        """
        return self._balance

    @property
    def in_jail(self):
        """
        getter that allows the use of the in_jail attribute
        
        Args:
        self: instance of the class
     
        Returns:
        boolean: is the player in jail
        
        Author: Bristow
        """
        return self._in_jail
        
    def pay_money(self, amount):
        """
        Deduct a certain amount of money from the player's balance
        Arg: amount(int)
        Return: None
        Author: Zhang
        """
        self._balance -= amount
    
    def gain_money(self, amount):
        """
        Increase a certain amount of money in the player's balance
        Arg: amount(int)
        Return: None
        Author: Zhang
        """
        self._balance += amount
        
    #def buy_property(self, property):
        """Check if the player's balance can afford the property,
        if so, add property to the player's properties and deduct price money;
        Arg: property(obj) - Property obj not yet created
        Return: True if affordable, False otherwise
        Author: Zhang"""
        #if self._balance >= property.price:
         #   self._balance = self._balance - property.price
          #  self.properties.append(property)
           # return True
        #else:
         #   return False
         
    def buy_property(self, property_space):
        if property_space.is_owned():
            print(f"{property_space.name} is already owned.")
            return False
        if self._balance < property_space.price:
            print(f"{self.name} does not have enough money to buy {property_space.name}.")
            return False
        self._balance -= property_space.price
        property_space.owner = self
        self.properties.append(property_space)
        print(f"{self.name} bought {property_space.name} for ${property_space.price}.")
        return True

            
    def move(self, steps, board):
        """Move the player piece's position on the board
        Arg: steps(int), board(obj)
        Return: None
        Author: Zhang, Bristow(provided little updates)"""
        old_position = self._position
        #new_position = self.position = board.move_position(self.position, steps)
        new_position = board.move_position(self._position, steps)
        self._position = new_position
        
        if old_position + steps >= board.board_size():
            self.gain_money(200)
            print(f"{self.name} passed GO and collected $200!")
            
        self._position = new_position
        return board.get_space(self._position)
    
    def player_current_space(self, board):
        """Check the player piece's current location on the board
        Arg: board(obj)
        Return: An int represents the piece's position
        Author: Zhang"""
        return board.get_space(self.position)
    
    
    def go_to_jail(self):
        """
        determins if a player is in jail
        
        Args: 
        self: instance of the class
        
        Returns: nothing
        
        Author: Bristow
             
        """
        
        self._position = 10
        self._in_jail = True

    def leave_jail(self):
        """
        determins if a player has left jail
        
        Args: 
        self: instance of the class
        
        Returns: nothing
        
        Author: Bristow
             
        """
        self._in_jail = False

    def __str__(self):
        """
        writes a string
        
        Args: 
        self: instance of the class
        
        Returns: f string of name, postion, balance and if the player is in jail
        
        Author: Bristow
             
        """
        return f"{self.name} | Position: {self.position} | Money: ${self._balance} | In Jail: {self.in_jail}"   
    