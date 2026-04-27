from Classes import BoardSpace

#using inheratince technique with BoardSpace
class Go_To_Jail_Space(BoardSpace):
    #method overriding-polymorphism
    def land_on(self, player,game):
        print (f"{player.name} landed on go to jail.")
        player.go_to_jail()