from Classes.OwnableSpace import OwnableSpace
class Property_Space(OwnableSpace):
    def __init__(self, position, name, price, base_rent):
        """
        Creates the PropertySpace class
        
        Arg:
        self: instance of the class
        postion: postion on the board
        name: name of postion on the board
        color: color of the postion on the board
        price: price of space on the board
        base_rent: rent of the space on the board
        
        Returns:
            nothing
        
        Authors: Bristow
        """
        
        super().__init__(position, name, "property", price)
        #self._color = color
        self._base_rent = base_rent
        self._houses = 0
        
    
    @property
    def base_rent(self):
        """
        Returns the rent of the space
        
        Args:
        self: instance of the class
        
        Returns:
        INT: Rent Price
        
        Author: Bristow
        """
        return self._base_rent

    @property
    def houses(self):
        """
        Returns the number of houses on the property
        
        Args:
        self: instance of the class
        
        Returns:
        INT of the number of houses
        
        Author: Bristow
        """
        return self._houses
    
    def add_house(self):
    
        """
        Allows a user to add houses to a property
        
        Args:
        self: instance of the class
        
        Returns:
        Boolean True or False
        
        Author: Bristow
        """
        if self._houses < 4:
            self._houses += 1
            print(f"Added a house to {self.name}. Total houses: {self._houses}")
            return True
        print(f"{self.name} already has 4 houses. Max capacity")
        return False
    
    def calculate_rent(self):
        """
        Calculates the rent of the space dependent on the number of houses
        
        Args:
        self: instance of the class
        
        Returns:
        INT: price of rent
        
        Author: Bristow

        """

        if self._houses == 0:
            return self._base_rent
        
        elif self._houses == 1:
            return self._base_rent * 2

        elif self._houses == 2:
            return self._base_rent * 3

        elif self._houses == 3:
            return self._base_rent * 4

        elif self._houses == 4:
            return self._base_rent * 5
        
    def __str__(self):
        """
        Provides summary of property
        
        Args:
        self: instance of the class
        
        Returns:
        string: f string of the summary of the property
        
        Author: Bristow

        """
    
        if self.owner:
            owner_name = self.owner.name
        else:
            owner_name = "None"
        return (
            f"{self.position}: {self.name} [Property] | "
            f"Price: ${self.price} | "
            f"Rent: ${self.calculate_rent()} | Owner: {owner_name}"

        )

   