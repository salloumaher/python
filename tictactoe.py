# TIC TAC TOE game
import random
# function to print a tic-tao-toe grid stored as a list of 3 lists
def print_grid(grid):
    for row in grid:
        for e in row:
            print(e, end = ' ')
        print()

#test the function print_grid
g = [ ['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_'] ]
#print_grid(g) 

emptycells=[]
for i in range(3):
    for j in range(3):
        t=(str(i),str(j))
        emptycells.append(t)


def check_win(grid, player):
    '''your code goes here'''
    if (grid[0][0]== player and grid[0][1]== player and grid[0][2]== player ) or (grid[1][0]==player and grid[1][1]==player and grid[1][2]==player) or (grid[2][0]==player and grid[2][1]==player and grid[2][2]==player) or (grid[0][0]==player and grid[1][1]==player and grid[2][2]==player) or (grid[0][2]==player and grid[1][1]==player and grid[2][0]==player) or (grid[0][0]==player and grid[1][0]==player and grid[2][0]==player) or (grid[0][1]==player and grid[1][1]==player and grid[2][1]==player) or (grid[0][2]==player and grid[1][2]==player and grid[2][2]==player) :
        print( player, " has won")
        return True

def get_user_pick(emptycells, grid):
    ''' your code goes here'''
    # assume user is x
    r= input("pick a row number: ")
    e= input("pick a line number: ")
    if (r,e) in emptycells :
        emptycells.remove((r,e))
        g[int(r)][int(e)] = "x"
        print_grid(g)
    else:
       get_user_pick(emptycells,grid)

#get_user_pick(emptycells, g)

def computer_pick(empty_cells, grid):
    '''your code goes here'''
    #assume pc is o
    y=random.choice(emptycells)
    emptycells.remove(y)
    g[int(y[0])][int(y[1])]="o"
    print_grid(g)
#computer_pick(emptycells, g)


def tictactoe():
    ''' Your code goes here
    '''
    grid=g
    print_grid(grid)
    l=[True, False]
    turn=random.choice(l)
    while True:
        if turn== True:
            computer_pick(emptycells, grid)
            if len(emptycells)==0:
                break
        if turn == False:
            get_user_pick(emptycells, grid)
            if len(emptycells)==0:
                print("it is a tie")
                break
        if check_win(grid, "o"):
            break
        if check_win(grid, "x"):
            break
        turn= not turn
        
tictactoe()
# start the game
