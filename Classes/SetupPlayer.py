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
        Asks player for name and to choice a token piece. CPU players are then created.
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
        
        player1_token = Player(name, self.token_piece[choice])   
        player1= Player(name,player1_token)
        
        remaining_pieces=[]
        for number, token in self.token_piece.items():
            if token != player1_token:
                remaining_pieces.append(token)
        
        player2_cpu = CPUPlayer("Player 2", remaining_pieces[0])
        player3_cpu = CPUPlayer("Player 3", remaining_pieces[1])
        player4_cpu = CPUPlayer("Player 4", remaining_pieces[2])
        