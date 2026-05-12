from Classes.Player import Player
from Classes.CPUPlayer import CPUPlayer

class SetupPlayer:
    """
    Creates human player to choose their token and CPU player
    Author: Melanie Abzun
    """
    token_piece= {
        "1":"Testudo",
        "2": "Shuttle Bus",
        "3": "Maryland Flag",
        "4": "Kermit the Frog",
        "5":"Bike",
        "6":"Scooter"
    }
    def setup(self):
        """
        Creates player 1(user) and 3 cpu players.
        Asks player 1 for name and to choice a token piece. 
        CPU players are then created and will automatically get remaining pieces.
        Returns: 
            list: All 4 players in the game
        Author: Melanie Abzun
        """
        print("\n===== UMD Monopoly =====")
        name = input("Enter your name: ")
        print("Choose Your Token Piece: ")
        for number,token in self.token_piece.items():
            print(f" {number}:{token}")
        
        choice = input("Enter the number of the piece: ").strip()
        while choice not in self.token_piece:
            choice= input("Invalid response. Choose from the numbers displayed: ")
        
        player1_token = self.token_piece[choice]
        player1= Player(name,player1_token)
        
        remaining_pieces=[]
        for number, token in self.token_piece.items():
            if token != player1_token:
                remaining_pieces.append(token)
        
        player2_cpu = CPUPlayer("Player 2", remaining_pieces[0])
        player3_cpu = CPUPlayer("Player 3", remaining_pieces[1])
        player4_cpu = CPUPlayer("Player 4", remaining_pieces[2])
        
        print("===== Players =====")
        print(f"{player1.name}: {player1.piece}")
        print(f"{player2_cpu.name}: {player2_cpu.piece}")
        print(f"{player3_cpu.name}: {player3_cpu.piece}")
        print(f"{player4_cpu.name}: {player4_cpu.piece}")
        return[player1,player2_cpu,player3_cpu, player4_cpu]
        
        
        