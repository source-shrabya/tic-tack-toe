
def boards(board):
    for i in board:
        print("  | ".join(i))
        print("_"*9)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        elif board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    for i in range(3):
        if board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        elif board[2][0] == board[1][1] == board[0][2]:
            return board[1][1]
def if_draw(board):
    for row in board:
        if " " in row:
            True
        else:
            False
def ask_user():
    board = [[ '' for i in range (3)] for i in range (3)]
    boards(board)
    print("Welcome to the game")
    players = ["X","O"]
    current = 0
    while True:
        print(f"It is {players[current]} turn ")
        try:
            i, j = map(int, input("Enter the row and column(0-2): ").split())
            if board[i][j] != '':
                print("This square is already taken, try again.")
                continue
            else:
                board[i][j]=players[current]
                boards(board)
                if check_winner(board):
                    print(f"Congrats! Player {current} has won.")
                    break
                elif if_draw(board):
                    print(f"It's draw")
                    break
                else:
                    current = 1 - current
                
                    continue 
            
        except(ValueError, IndexError):
            print("Invalid Input. Plase enter the number from 0 to 2. Hello ")

ask_user()


        
        





