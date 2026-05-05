from Classes.OwnableSpace import OwnableSpace

# using inheritance technique with OwnableSpace
class Utility_Space(OwnableSpace):
    # method overriding-polymorphism
    def __init__(self, position, name, price):
        """
        Creates the Utility_Space class

        Args:
        self: instance of the class
        position: position on the board
        name: name of position on the board
        price: price of utility space

        Returns:
        nothing

        Author: Zhang
        """
        super().__init__(position, name, "utility", price)

    def calculate_rent(self):
        """
        Calculates the fixed rent of the utility space

        Args:
        self: instance of the class

        Returns:
        int: rent price

        Author: Zhang
        """
        return 50

    def __str__(self):
        if self.owner:
            owner_name = self.owner.name
        else:
            owner_name = "None"

        return (
            f"{self.position}: {self.name} [Utility] | "
            f"Price: ${self.price} | "
            f"Rent: ${self.calculate_rent()} | Owner: {owner_name}"
        )