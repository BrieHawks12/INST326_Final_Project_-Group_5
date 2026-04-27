from Classes import BoardSpace

#using inheratince technique with BoardSpace
class Free_Parking_Space(BoardSpace):
    #method overriding-polymorphism
    def land_on(self, player,game):
        print (f"{player.name} land on Free Parking, nothing happens.")