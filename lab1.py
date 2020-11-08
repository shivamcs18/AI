In [1]:
# Create a 3x3 tic tac toe board of "" strings for each value
board = [''] * 9
In [2]:
# Create a function to display your board
def display_board(board):
    print('     |      |')
    print('   '+ board[0]+ '  |    '+ board[1]+'  |  '+ board[2])
    print('     |      |')
    print('-------------------')
    print('     |      |')
    print('   '+ board[3]+ '  |    '+ board[4]+'  |  '+ board[5])
    print('     |      |')
    print('-------------------')
    print('     |      |')
    print('   '+ board[6]+ '  |    '+ board[7]+'  |  '+ board[8])
    print('     |      |')
    print('                             ')
display_board(board)
     |      |
     |      |  
     |      |
-------------------
     |      |
     |      |  
     |      |
-------------------
     |      |
     |      |  
     |      |
                             
In [3]:
#Create a function to check if anyone won, Use marks "X" or "O"
def check_win(player_mark, board):
    ## If the player has won then there must be 3 consecutive Player values
    return( (board[0]== player_mark and board[1]== player_mark and board[2]== player_mark0) or
            (board[3]== player_mark and board[4]== player_mark and board[5]== player_mark0) or
            (board[6]== player_mark and board[7]== player_mark and board[8]== player_mark0) or
            (board[0]== player_mark and board[3]== player_mark and board[6]== player_mark0) or
            (board[1]== player_mark and board[4]== player_mark and board[7]== player_mark0) or
            (board[2]== player_mark and board[5]== player_mark and board[8]== player_mark0) or
            (board[0]== player_mark and board[4]== player_mark and board[8]== player_mark0) or
            (board[2]== player_mark and board[4]== player_mark and board[6]== player_mark0) 
          )

check_win('X', board)
Out[3]:
False
In [4]:
# Create a function to check its a Draw
def check_draw(board):
        return ' ' not in board
In [5]:
# Create a Function that makes a copy of the board
def display_board(board):
    dupeBoard=[]
    for j in board:
        dupeBoard.append(j)
    return dupeBoard
In [6]:
#Immediate move checker
def test_win_move(move, player_mark, board):
    bCopy=board_copy(board)
    bCopy[move]=player_mark
    return check_win(player_mark, bCopy)
In [7]:
#Strategy if others fail
def win_strategy(board):
    def win_strategy(board):
        if board[4]== ' ':
            return 4
        for i in [0,2,6,8]:
            if board[i]==' ':
                return i
        for i in [1,3,5,7]:
            if board[i]==' ':
                return i
In [8]:
# Agents move
def get_agent_move(board):
    # Return agent move with your strategy
    for i in range(0, 9):
        if board[i] == ' ' and test_win_move(board, 'X', i):
            return i
    # Check player win moves
    for i in range(0, 9):
        if board[i] == ' ' and test_win_move(board, '0', i):
            return i
    
    for i in range(0, 9):
        if board[i] == ' ' and fork_move(board, 'X', i):
            return i
    
    for i in range(0, 9):
        if board[i] == ' ' and fork_move(board, '0', i):
            return i
    return win_strategy(board)
In [9]:
# Assemble the game
def tictactoe():
    ### Note you need to recreate your board again here if you wish to play the game more than once
    Playing = True
    while Playing:
        InGame = True
        board = [' '] * 9
        print('Would you like to go first or second? (1/2)')
        if input() == '1':
            playerMarker = '0'
        else:
            playerMarker = 'X'
            display_board(board)

        while InGame:
            if playerMarker == '0':
                print('Player go: (0-8)')
                move = int(input())
                if board[move] != ' ':
                    print('Invalid move!')
                    #continue
            else:
                move = get_agent_move(board)
            board[move] = playerMarker
            if check_win(playerMarker,board):
                InGame = False
                display_board(board)
                if playerMarker == '0':
                    print('Player wins!')
                else:
                    print('Agent wins!')
                continue
            if check_draw(board):
                InGame = False
                display_board(board)
                print('It was a draw!')
                continue
            display_board(board)
            if playerMarker == '0':
                playerMarker = 'X'
            else:
                playerMarker = '0'

        print('Type y to keep playing')
        inp = input()
        if inp != 'y' and inp != 'Y':
            Playing = False
In [10]:
# Play!!!
tictactoe(board)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-10-277459585011> in <module>
      1 # Play!!!
----> 2 tictactoe(board)

TypeError: tictactoe() takes 0 positional arguments but 1 was given
In [ ]:
class Tic_Tac_Toe:
    def __init__(self):
        pass
