# head
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: David Skoruša
email: d.skorusa@post.cz
discord: David Skoruša#7746
"""

# TODO board
def display_board(board):
    for row in board: 
        print("+---+---+---+")
        print("| {} | {} | {} |".format(row[0], row[1], row[2]))
    print("+---+---+---+")

# TODO check win (rows, colums and diagonals)
def check_win(board, player):
    for A in range(3):
        if all([board[A][B] == player for B in range(3)]) or \
           all([board[B][A] == player for B in range(3)]):
            return True
        
    if all([board[A][A] == player for A in range(3)]) or \
       all([board[A][2 - A] == player for A in range(3)]):
        return True
        
    return False
# TODO greet
def greet():
    print(f"Welcome to Tic Tac Toe")
    print("=" * 40)
# TODO rules
def rules():
    print(f"GAME RULES:")
    print("Each player can place one mark (or stone)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print("=" * 40)
    print("Let's start the game")
# TODO main game
def main():
    greet()
    rules()

    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    players = ['X', 'O']
    current_player = 0
    moves = 0

    while True: 
        print("--------------------------------------------")
        display_board(board)
        print("=" * 40)
# TODO input from player
        player = players[current_player]
        move = input(f"Player {player} | Please enter your move number: ")

        if not move.isdigit() or int(move) not in range(1, 10):
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        row = (int(move) - 1) // 3
        column = (int(move) - 1) % 3

        if board[row][column] != ' ':
            print("This cell is already occupied. Try again.")
            continue

        board[row][column] = player
        moves += 1
        current_player = (current_player + 1) % 2

        if moves >= 5 and check_win(board, player):
            display_board(board)
            print("=" * 40)
            print(f"Congratulations, the player {player} WON!")
            print("=" * 40)
            break

        if moves == 9:
            display_board(board)
            print("=" * 40)
            print("It's a DRAW!")
            print("=" * 40)
            break

if __name__ == "__main__":
    main()
