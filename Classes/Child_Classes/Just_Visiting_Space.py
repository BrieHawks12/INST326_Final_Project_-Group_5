from Classes import BoardSpace

#using inheratince technique with BoardSpace
class Just_Visiting_Space(BoardSpace):
    #method overriding-polymorphism
    def land_on(self, player,game):
        print (f"{player.name} is just visiting jail.")