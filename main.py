
from Classes.Board import Board
from Classes.Player import Player
from Classes.Dice import Dice
from Classes.SetupPlayer import SetupPlayer

"""
Main Monopoly loop and display: rolls dice, players take turns, and returns space interactions.
Authors: Melanie Abzun, Briana Bristow, Siddhi Patel, Jiayang Zhang
"""
board = Board()
dice = Dice()
setup= SetupPlayer()
players = setup.setup()

while True:
    
    for player in players:
        print(f"{player.name}'s turn")
        if not player.is_cpu:
            input("Press Enter to roll dice: ")
        else:
            input("Press Enter to watch next Player turn: ")

        roll = dice.roll_dice()
        print(f"{player.name} rolled: {roll}")

        space = player.move(roll,board)
        print(player)
        print(space)

        space.land_on(player)
        #Land on the same property for testing house-buying functions.
        #print("\nTesting landing on same property again...\n")
        #space.land_on(player)

        if not player.is_cpu:
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
