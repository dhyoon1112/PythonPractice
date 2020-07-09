
'''
def board(size):
    size = input("Game Board Size, 3x3, 8x8, 19x19? ")
    x = int(size) * ' ---'
    line = '\n'
    y = (int(size) + 1) * '|   '

    print((x + line + y + line) * int(size))

    return 
''' 

def victor(game):
    sampleboard = game

    sampleboardx0 = sampleboard[0]
    sampleboardx1 = sampleboard[1]
    sampleboardx2 = sampleboard[2]
    sampleboardy0 = [sampleboard[0][0],sampleboard[1][0],sampleboard[2][0]]
    sampleboardy1 = [sampleboard[0][1],sampleboard[1][1],sampleboard[2][1]]
    sampleboardy2 = [sampleboard[0][2],sampleboard[1][2],sampleboard[2][2]]
    sampleboardxy0 = [sampleboard[0][0],sampleboard[1][1],sampleboard[2][2]]
    sampleboardxy1 = [sampleboard[0][2],sampleboard[1][1],sampleboard[2][0]]

    if sampleboardx0.count('X') == 3 or sampleboardx1.count('X') == 3 or sampleboardx2.count('X') == 3 or sampleboardy0.count('X') == 3 or sampleboardy1.count('X') == 3 or sampleboardy2.count('X') == 3 or sampleboardxy0.count('X') == 3 or sampleboardxy1.count('X') == 3:
        victor = "Player 1 Wins!"
        
    elif sampleboardx0.count('O') == 3 or sampleboardx1.count('O') == 3 or sampleboardx2.count('O') == 3 or sampleboardy0.count('O') == 3 or sampleboardy1.count('O') == 3 or sampleboardy2.count('O') == 3 or sampleboardxy0.count('O') == 3 or sampleboardxy1.count('O') == 3:
        victor = "Player 2 Wins!"
        
    else:
        victor = "Keep playing"

    return victor


def gameboard():
    game = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
    turncount = 2
    
    while True:
        if turncount % 2 == 0:
            turn = input("Player X, enter your mark [i.e '1,1' or '3,3']: ")
            turn = turn.split(',')
            if game[int(turn[0])-1][int(turn[1])-1] in ('X','O'):
                turn = input("Player X, try again. That spot is already taken [i.e '1,1' or '3,3': ")
            game[int(turn[0])-1][int(turn[1])-1] = 'X'
            
        elif turncount % 2 == 1:
            turn = input("Player O, enter your mark [i.e '1,1' or '3,3': ")
            turn = turn.split(',')
            if game[int(turn[0])-1][int(turn[1])-1] in ('X','O'):
                turn = input("Player O, try again. That spot is already taken [i.e '1,1' or '3,3': ")
            game[int(turn[0])-1][int(turn[1])-1] = 'O'
            

        turncount += 1
        print(str(game[0]) + '\n' + str(game[1]) + '\n' + str(game[2]))

        if 'Wins' in victor(game):
            print(victor(game))
            break
        else:
            print(victor(game))

    return game


gameboard()
