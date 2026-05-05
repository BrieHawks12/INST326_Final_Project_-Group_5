
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

