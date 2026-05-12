from abc import ABC,abstractmethod 
from Classes.BoardSpace import BoardSpace 
#from Player import Player


class OwnableSpace(BoardSpace, ABC):
    def __init__(self, position, name, category, price):
        """
        creating the OwnableSpace class and inheriting postion, name and 
        category from BoardSpace
        
        Args:
        self: instance of a class
        postion: position on the board
        category: category of the specific space
        price: price of space
        price
        
        Returns: Nothing
        
        Author: Bristow
        
        """       
        super().__init__(position, name, category)
        self._price = price
        self._owner = None
        
    @property
    #need getter methods to get the private values
    def price(self):
        """
        getter that allows the use of the price attribute
        
        Args:
        self: instance of the class
     
        Returns:
        int: price of the class
        
        Author: Bristow
        
        """
        return self._price

    @property
    def owner(self):
        """
        getter that allows the use of the owner attribute
        
        Args:
        self: instance of the class
     
        Returns:
        string: name of the owner of the space
        
        Author: Bristow
        
        """
        return self._owner
    
    @owner.setter
    def owner(self, player):
        self._owner = player

    def is_owned(self):
        """
        getter that allows the use of the owner attribute
        
        Args:
        self: instance of the class
     
        Returns:
        boolean: True or False
        
        Author: Bristow
        
        """
        if self._owner is not None:
            return True
        else:
            return False
    
    @abstractmethod
    def calculate_rent(self):
        """
        used to calculate the rent of the specific space
        
        Args:
        self: instance of the class
     
        Returns:
        nothing
        
        Author: Bristow
        """
        pass
    
    def land_on(self, player):
        """
        Behavior when you land on a specific space. Uses Player Class
        
        Args:
        self: instance of the class
        player: Player Class being used
        
        returns:
        prints string about the summary of the specific space
        
        Author: Bristow, Zhang
        
        """

        if not self.is_owned():
            print(f"{player.name} landed on {self.name}, which is unowned.")
             
            buy_choice = input(f"Do you want to buy {self.name} for ${self.price}? (yes/no): ")
            if buy_choice.lower() == "yes":
                player.buy_property(self)
            else:
                print(f"{player.name} chose not to buy {self.name}.")
            player.buy_property(self)

        elif self.owner == player:
            print(f"{player.name} landed on their own property: {self.name}.")
            if self.category == "property":
                print(f"Current houses: {self.houses}")
                house_choice = input("Do you want to buy a house for $50? (yes/no): ")
                
                if house_choice.lower() == "yes":
                    if player.balance >= 50:
                        if self.add_house():
                            player.pay_money(50)
                            print(f"{player.name} bought a house on {self.name}.")

                    else:
                        print("Not enough money to buy a house.")

        else:
            rent = self.calculate_rent()
            print(f"{player.name} landed on {self.name}, owned by {self.owner.name}.")
            print(f"{player.name} must pay ${rent} in rent.")
            player.pay_money(rent)
            self.owner.gain_money(rent)