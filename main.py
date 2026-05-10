
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
#Land on the same property for testing house-buying functions.
#print("\nTesting landing on same property again...\n")
#space.land_on(player)

print(player)
check_status = input("Do you want to check your status? (yes/no): ")
if check_status.lower() == "yes":
    print("\n===== PLAYER STATUS =====")

    print(f"Name: {player.name}")
    print(f"Current Position: {player.position}")
    print(f"Balance: ${player.balance}")
    print(f"In Jail: {player.in_jail}")

    if player.properties:
        print("Owned Properties:")
        for property in player.properties:
            print(f"- {property.name}")
    else:
        print("Owned Properties: None")

    print("=========================\n")

try:
    if space.owner:
        space_owner_displayed = space.owner.name
    else:
        space_owner_displayed = "None" 
except AttributeError:
    space_owner_displayed = "None"
