class ChessGame:
    def __init__(self):
        self.board = self.initialize_board()
        self.current_player = "white"

    def initialize_board(self):
        # Initialize the chess board with pieces
        board = [["  "]*8 for _ in range(8)]
        board[0] = ["BT","BC","BA","BQ","BR","BA","BC","BT"]
        board[1] = ["BP","BP","BP","BP","BP","BP","BP","BP"]
        board[6] = ["WP","WP","WP","WP","WP","WP","WP","WP"]
        board[7] = ["WT","WC","WA","WQ","WR","WA","WC","WT"]
        return board

    def print_board(self):
        print("  a b c d e f g h")
        for i, row in enumerate(self.board):
            print(8-i, end=" ")
            for cell in row:
                print(cell, end=" ")
            print(8-i)
        print("  a b c d e f g h")

    def is_valid_move(self, start, end):
        # Check if the move is valid (e.g. piece can move to that square)
        piece = self.board[start[0]][start[1]]
        if piece == "  ":
            return False
        if piece[0] == "W" and self.current_player != "white":
            return False
        if piece[0] == "B" and self.current_player != "black":
            return False
        # Check if the piece can move to the destination square
        if piece[1] == "P":  # Pawn
            if start[0] == end[0] and abs(start[1] - end[1]) == 1:
                return True
            if start[1] == end[1] and abs(start[0] - end[0]) == 1:
                return True
        elif piece[1] == "R":  # Rook
            if start[0] == end[0] or start[1] == end[1]:
                return True
        elif piece[1] == "N":  # Knight
            if abs(start[0] - end[0]) == 2 and abs(start[1] - end[1]) == 1:
                return True
            if abs(start[0] - end[0]) == 1 and abs(start[1] - end[1]) == 2:
                return True
        elif piece[1] == "B":  # Bishop
            if abs(start[0] - end[0]) == abs(start[1] - end[1]):
                return True
        elif piece[1] == "Q":  # Queen
            if start[0] == end[0] or start[1] == end[1] or abs(start[0] - end[0]) == abs(start[1] - end[1]):
                return True
        elif piece[1] == "K":  # King
            if abs(start[0] - end[0]) <= 1 and abs(start[1] - end[1]) <= 1:
                return True
        return False

    def make_move(self, start, end):
        # Move the piece from start to end
        self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
        self.board[start[0]][start[1]] = "  "

    def play_game(self):
        while True:
            self.print_board()
            start = input("Ingrese primera posición(e.g. e2): \n")
            end = input("Ingrese posición final (e.g. e4): \n")
            start = (8-int(start[1]), ord(start[0])-97)
            end = (8-int(end[1]), ord(end[0])-97)
            if self.is_valid_move(start, end):
                self.make_move(start, end)
                self.current_player = "black" if self.current_player == "white" else "white"
            else:
                print("Invalid move!")

if __name__ == "__main__":
    game = ChessGame()
    game.play_game()