import random


board =[]

for x in range(8):
    board.append('0'*8)
board = [list(row) for row in board]

def printt(board):
    for row in board:
        print('  '.join(row))

print('lets start the game')



printt(board)

def random_row(board):
    return random.randint(0, len(board)-1)

def random_col(board):
    return random.randint(0, len(board)-1)

ship_row=random_row(board)
ship_col=random_col(board)



for turn in range(9):
    print('turn', turn)
    guess_row = int(input('guess row: '))
    guess_col = int(input('guess_col: ').strip())


    if guess_row== ship_row and guess_col==ship_col:
        print('congratulations! you sunk my battleship')
        break

    else:
        if ( guess_row<0 or guess_row>8 ) or (guess_col<0 or guess_col>8):
            print('out of range')

        elif(board[guess_row][guess_col]=='X'):
            print('you already guessed that')

        else:
             print('missed')
             board[guess_row][guess_col]='X'
           

        if turn==8:
            print('game over')
         

    turn=+1

    printt(board)







        