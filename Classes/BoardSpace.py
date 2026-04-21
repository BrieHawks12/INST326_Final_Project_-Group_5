class BoardSpace:
    def __init__(self, position, name, category, price=0):
       
       self.poistion = position
       self.name = name
       self.category = category
       self.price = price
       

    def is_purchasable(self):
        if self.category in ["property","railroad","utility"]:
            return True
    
    def __str__(self):
        return f"{self.poistion}: {self.name} {self.category} - ${self.price}"
               