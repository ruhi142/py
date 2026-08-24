# Initialize a 3x3 board with spaces
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
player = 'X'

def display_board():
    print()
    print("  0   1   2")
    print("0 " + board[0][0] + "| " + board[0][1] + "| " + board[0][2])
    print("  ----------")
    print("1 " + board[1][0] + "| " + board[1][1] + "|" + board[1][2])
    print("  -====----")
    print("2 " + board[2][0] + "| " + board[2][1] + "| " + board[2][2])
    print()

def check_winner():
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
            
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
            
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
        
    return None

def board_full():
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

# Main game loop
while True:
    display_board()
    print(f"Player {player}'s turn")
    
    # Handle user inputs safely
    try:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
    except ValueError:
        print("Please enter valid numbers!")
        continue
        
    # Bounds validation
    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Invalid position! Try again.")
        continue
        
    # Occupied cell validation
    if board[row][col] != ' ':
        print("That position is already occupied!")
        continue
        
    # Make the move
    board[row][col] = player
    
    # Check for win condition
    winner = check_winner()
    if winner is not None:
        display_board()
        print(f"Player {winner} wins!")
        break
        
    # Check for draw condition
    if board_full():
        display_board()
        print("It's a draw!")
        break
        
    # Alternate turns
    if player == 'X':
        player = 'O'
    else:
        player = 'X'