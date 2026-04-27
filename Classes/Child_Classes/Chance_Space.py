from Classes import BoardSpace

#using inheratince technique with BoardSpace
class Chance_Space(BoardSpace):
    #method overriding-polymorphism
    def land_on(self, player,game):
        print (f"{player.name} laned on chance")