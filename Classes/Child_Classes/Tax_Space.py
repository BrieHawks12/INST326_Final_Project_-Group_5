from Classes import BoardSpace,Player

class Tax_Space(BoardSpace):
    def __int__(self, position, name, tax_amount):
        super().__init__(position,name)
        self._tax_amount = tax_amount
        
    @property
    def tax_amount(self):
        return self._tax_amount
    
    def land_on(self, player, game):
        player.pay_money(self.tax_amount)
        print (f"{player.name} landed on {self.name} and paid ${self.tax_amount}")
        
            