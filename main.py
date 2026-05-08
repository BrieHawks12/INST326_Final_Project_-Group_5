
from Classes.Board import Board
from Classes.Player import Player
from Classes.Dice import Dice

board = Board()
player = Player("Briana", "Turtle")
dice = Dice()

roll = dice.roll_dice()
print(f"Rolled: {roll}")

space = player.move(roll,board)
print(player)
print(space)

space.land_on(player)

print(player)
print("Owned properties:", [p.name for p in player.properties])
try:
    if space.owner:
        space_owner_displayed = space.owner.name
    else:
        space_owner_displayed = "None" 
except AttributeError:
    space_owner_displayed = "None"
