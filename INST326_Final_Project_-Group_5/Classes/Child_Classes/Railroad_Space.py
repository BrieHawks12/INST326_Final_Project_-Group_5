from Classes.OwnableSpace import OwnableSpace

# using inheritance technique with OwnableSpace
class Railroad_Space(OwnableSpace):
    # method overriding-polymorphism
    def __init__(self, position, name, price):
        """
        Creates the Railroad_Space class
        Args:
        self: instance of the class
        position: position on the board
        name: name of position on the board
        price: price of railroad space
        
        Returns:
        nothing

        Author: Zhang
        """
        super().__init__(position, name, "railroad", price)

    def calculate_rent(self):
        """
        Calculates the rent of the railroad space

        Args:
        self: instance of the class

        Returns:
        int: price of rent

        Author: Zhang
        """
        return 25

    def __str__(self):
        if self.owner:
            owner_name = self.owner.name
        else:
            owner_name = "None"

        return (
            f"{self.position}: {self.name} [Railroad] | "
            f"Price: ${self.price} | "
            f"Rent: ${self.calculate_rent()} | Owner: {owner_name}"
        )