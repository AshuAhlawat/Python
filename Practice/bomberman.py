from _timer import timeit

def transform(grid, re=False):
    trans_grid = []

    if re:
        for line in grid:
            trans_line = ""

            for point in line:
                if point >= 1:
                    trans_line += "O"
                else:
                    trans_line += "."

            trans_grid.append(trans_line)

    else:
        for line in grid:
            trans_line = []

            for point in line:
                if point ==".":
                    trans_line.append(0)
                else:
                    trans_line.append(1)
            
            trans_grid.append(trans_line)

    return trans_grid

def increment(grid, h,w):
    for i in range(h):
        for j in range(w):
            grid[i][j]+=1

def blast(grid, h, w):
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 2:
                if i+1<h:
                    if grid[i+1][j]!=2:
                        grid[i+1][j]=0
                if i>0:
                    if grid[i-1][j]!=2:
                        grid[i-1][j]=0
                if j+1<w:
                    if grid[i][j+1]!=2:
                        grid[i][j+1]=0
                if j>0:
                    if grid[i][j-1]!=2:
                        grid[i][j-1]=0
                grid[i][j]=0


def bomberMan(n, grid):
    height = len(grid)
    width = len(grid[0])
    
    grid = transform(grid)

    for i in range(n):

        if i%2==1:
            increment(grid, height, width)
        else:
            blast(grid, height, width)
        
        
        # print("Second :", i+1)

        # for j in transform(grid, re=True):
        #     print(j)
        # print("\n")

        if i+1 == n:
            return transform(grid, re=True)


grid1 = [
    '.......',
    '...O...', 
    '....O..', 
    '.......', 
    'OO.....', 
    'OO.....'
]
grid2 = [
    '.......',
    '...O.O.',
    '....O..',
    '..O....',
    'OO...OO',
    'OO.O...'
]
grid3 = [
'...O..O..OOOO..........OO..OO.O..OO..OOOO..OOO...O....O....OO.......O......O.O..................OO..OO......O..O.....O.O..O..........O.OOOO.O.O.O..O.O....O..OO.......O....O.OOO.OO.O.........',
'.O.O.O...O.O.O.......O.OOO..OO.OO.OO.....O...O.......O.O...O...OO..OOO......O....O......OO.....O....O..O.O....OO..O.O.O.O..OO...OO.O......OO....OOO.....O.O.O...O.....O.....OO.O....OOOO....O.',
'.O...O....O.....O....O..O.....OOOO......O..........O.....O.OO...........OOOO.O...O.OO..O...OO...O.OOO.O.......OOO.......OOO....OO.O..O...OO..OO.O....OO.....O....OO..O....OO....O..OO.....O.O.',
'.....OO.OOO....O.OO....O.OO....OOOO..O.....O.....O....O.O..OO.OOOO.......OO...O..O..OO.....O..O..O.OO...O.OO..OO..O..........O...O.OOO.O..O..O..O..O...O...O....O.OO...OO..O.O...O...O........',
'....O..O..O.O..O..OO...O.....O.OOO.O.....O..O.....O...O....OO...OO.O.........OOOOOO..OOO..OO.OOOO...O.O....O...O..O........O.OO.O.....OO.....O....O..O...O......O.OO....O..O......O......O..O.',
'O.O...O...OOOO.O.O..OOOOOO....O...O..OO.O...O..O.OO..O..O.O..O.......O..OOO....O.....OO....OO..O....OO.O.....OO..OO.OOO.O.....O.....O..O.O...O.O........O...O.OO.O..OO..O....O..O.O.OO.......O',
'.O.O.O.O............OO.O.O.O...O.OO..O....O....O..OO..OO.OOOO.O...OO..O.O.O.O..O.O...OO.O...O..O...O....OO.O.........O.O.O.....O....O..........O...........OOO...O......OO.OOO...O.O.O.O....O.',
'...OO...O..OO.OOO.OO......O...O....O.O....O..O..O..O.....O........OOO...OOO.......O..........O....OOO..O..O....OO.O.O..OOO.O...O..OO.O...O.....OO..OOOO..O...O......OOOO.O.OO.O.O.O..OO.O....O',
'OO..OOOOOO...OOO.OOOOOO.OO....OO..O....O...OOOO....O..O....OOO.O.OO.O.O.O...OOO.....O...O....OOO...OO..O.OO.O.OOO...O..O..O....OOO.OO......OOOO.O....O..O.O..O..OO.OO......OO...OOOOO.........',
'.......O.OO.......O..O..O.OOOO..O.....O..O.....OO.O...OOO.O...O..O.O..O..O.O....OOOO....O.O..OO....O........OO..O..O.O....OO...O......O.........O..O....OO..O..O...O..OOOOOO............O.O..O',
'.OO.OOO....OO.OO.O..OOO....O.....O........OO.OOOOO........OO...OO.O.....O.OOO......O.OOO..O...O....O.O..OOO..O.OO.....O..O.OOOO.....OO.O.OOOO..O.OO...OOOO..OO.O.......O..O..OO.OOO...O.O.O.OO',
'OO.....O.O...O..O....O...O...O...OO.O..O.OOO.............O...O..O..O..O...OOO..OO.OO..OOO.....O..OOO.OOO....O......OO....O......OO.O..O..O.....O.O.O..O.O......O..O......O...O.OO..O..O..O..OO',
'.O........O.O.....OOOOO...OOO..O..OO.O....O.O..OOOO.O.O..O........O..OO....O......OOOO..O...O..OOO.....OOO..OO.OO.O...OOO...O.O.O..O.O...O..O.O.O..OO..O...OO...O.......O..O...OO.O.......O.O.',
'...O..OOO..OO.OOOOO..OOO...OOO.OOO..O...OOO.OO..OOO...OO..O...O.....OOO.........OO.O.OOO..O....OO.O....O.....O.O........O.O.O..O........O..O.....O.O...O..OOO...O..O.....OO....OO..O....O..O..',
'..........O.O....O..OO.OO....OO..........OO......O.O....O...O.O.O.O..OO...O..O.O...O....O....O..OOO.....O..O.O..O.OOO...OO..OO....O.O..O.OO.O...OO.OO.....O.OO..O.O.......O..O..O...O....OOO..',
'.......O.....O.....O..OO..O.O..O....OO.O.O.OO.........O..OOOO....OO..O.OO.O..O.O...O.O...O...O.O.........OOOO.O....OO....O.OO..O.O.O...O...O..O........OO..OO.......OO.O.O.OOOO......O...O..O.',
'...O.OO.....O..O....O....O.......O......O.OOO...OO.OO..........O...O..O.O.O....O.O...O.O....OOO...........O..O...O........OO...O.....O.OO....OO.O........O.O..O..O..OOO.O..O.O...........O..O.',
'O..O.......OO...O..O....O....OOO...O......O.....OO.OO..............O..O......OO...O..O.OOOO....O....O.OO...OOOOO.........O...OO..OOO....OO.O..O..OO..O...O..O..O.OO...OO..O...O.O...OO...OOO.O',
'......OO.O.........O.O...O..OOO.O..OO....OO........O......OO..O.OO..OO.OO....OOO..O...OO.....O....O.O.OO...O.OO....O.......O.O.......OOO....O....O..OO....O..O..OO.O.O.....OOOO..O.O....O.....',
'.OO..OO.......O..O..O.....OO.......O...OOO...........OO.......OO..........O...O.OO.....OO.O.....O....OO.OO........O..O..OO....O...O..O.O.OO......O.OOO...O...O.O.OO.OOO.OO..O..OOO..O...O.O...',
'O......OO.O.OO.O..........O...O...O.O..OOO......OO.............O..OO.O.O.....O.....O...O...........O.O..OOO.O...O..O...O...O..OOO..O..O.......OO..OO.O.OOO..OOOO.O.O.O.OO..O...O..O.O.O.....OO',
'OOO...........O....OO......O.O.O...OOOO...O..OOO....OOOOO...OO....OOO....O.....OO.O..O.O..O...O..OO...........O.O.O..........O.O...O.O.O.OO....OO.OO..O.OO....O...O...OO.O......O.O.....OOO..O',
'O.OO.O..OO..........O.O....OO.......O....OO..OO...O...OO..O.O...OOOO....O......OO.O...O..O..O.O.O.....OOO....O.....OO..O..........O........O....O.O...OOO..O.OO..O.O.O...OO...OOO..O......OO.O',
'O.O..OOO..OO....O........OO....O.......O......OOOOOOO.O....OOO.O....OOO......O.O..O......OOOOO.O..O.........O.O.....O.O.OO...O..OOO.OOO............O..O.....OO.O..OOO..OO..O.....O...O..O.O...',
'O.OO.....OOO......OO..O.OO.O.OOOO..........OO..OOOOOOO...OO.....OO...OO..O......OO.O.O..O..OO..........OO..O..OO.O...O..O............O...OO..O.O...O.O....O.OO.....OO..OO..O..OO...O..OOOOO.O.',
'O.O.O...OO.OOO....O.OO....OOOO.O...O.O.......OOO.OO....OO..O..OO..OOO..O.O....O..O..OO..O..O.O....OO.....O.....O...O.O.O..O...OOO.O...O...OO.O.O.O..OO.O.O.O...O.....OO.OO.......O....O......O',
'...OO.....O.O.OO.OOO.O.O....O.O..OOOO..O.O...O.....O...O.O.OO.OOOO.O...OOOO.....OO........O.O..OOO........OO......OOO..O....O..OO...O...O...O..O........O.O.OO.O........O...OO..O.O.OOOOO..O.O',
'.......O.O...O.OO......OOOOO.O.OO.....OOO...O.O........O..O..O.O..O...O.O..O........OOO..OOOO......O.....O.....O..O..O....OO.O.O....O.O......O.O......OOO..O..O..OOOO..O.O.O......O..O...O....',
'..O...OO.....O.OO..O..OO....OO..OO....OOO...O......O.OOOOO..O..O..O..O..O...O.O..OOO.OO..O.O..OO......O........O........O.OO.O.O..................O..O..O.O...O.O.......O...O...O...OO....O.O.',
'.....O..O.O.OO.OO..........O.............OOO...OO....O..O.........OOO.O..OO.OOO...O...OO.O..O..OOOO...O.......O.O...OO...O....OOOO...O.O..O......O..O.O.O.....O..OO.OOO.O.....O.O..OO..O....OO',
'...O.O...O.OO..O.O.O........OO.OO..O...O.O...OO.......OOO..O...OOO.....O......O.OOOOOO......OO...O..O.O.OOO..O.O.OO.....O...O.....O.O.....OO...O.....O.O.OOOO.OO....O.O.O......OO.O...OO...O.O',
'O...........O....OO.O..OO..........OO.O.OO.......OOOO..O.....O.OO.....O...O....O.OO.O..OO..O..O..OO.........O.OO.OO..O.........O..O...OO..O..O.OO...OO..OO........OO.O...O.O.O.......O..OO.OOO',
'.....OO.............OO....OOO..O.OO...O..........O...OO.O...OO.O.........O...O...O..OO..OOO....O.......O....O..O.OOO...OO...............OOOO.O.....O.........O.......O.O..O.......OO..O.O....O',
'.....O...OO.O...O..OO..O..O...O.OO....OO..O..OO.O..O..OO...O......O.OO..O.......OO.O....O.O.......O..O...O...O..O.........OOOO..O..O....O.....O.O.....OO.OO.O...O...O....O....OOO..OOO...O..O.',
'...O..O..OOOO..........OO..OO.O..OO..OOOO..OOO...O....O....OO.......O......O.O..................OO..OO......O..O.....O.O..O..........O.OOOO.O.O.O..O.O....O..OO.......O....O.OOO.OO.O.........',
'.O.O.O...O.O.O.......O.OOO..OO.OO.OO.....O...O.......O.O...O...OO..OOO......O....O......OO.....O....O..O.O....OO..O.O.O.O..OO...OO.O......OO....OOO.....O.O.O...O.....O.....OO.O....OOOO....O.',
'.O...O....O.....O....O..O.....OOOO......O..........O.....O.OO...........OOOO.O...O.OO..O...OO...O.OOO.O.......OOO.......OOO....OO.O..O...OO..OO.O....OO.....O....OO..O....OO....O..OO.....O.O.',
'.....OO.OOO....O.OO....O.OO....OOOO..O.....O.....O....O.O..OO.OOOO.......OO...O..O..OO.....O..O..O.OO...O.OO..OO..O..........O...O.OOO.O..O..O..O..O...O...O....O.OO...OO..O.O...O...O........',
'....O..O..O.O..O..OO...O.....O.OOO.O.....O..O.....O...O....OO...OO.O.........OOOOOO..OOO..OO.OOOO...O.O....O...O..O........O.OO.O.....OO.....O....O..O...O......O.OO....O..O......O......O..O.',
'O.O...O...OOOO.O.O..OOOOOO....O...O..OO.O...O..O.OO..O..O.O..O.......O..OOO....O.....OO....OO..O....OO.O.....OO..OO.OOO.O.....O.....O..O.O...O.O........O...O.OO.O..OO..O....O..O.O.OO.......O',
'.O.O.O.O............OO.O.O.O...O.OO..O....O....O..OO..OO.OOOO.O...OO..O.O.O.O..O.O...OO.O...O..O...O....OO.O.........O.O.O.....O....O..........O...........OOO...O......OO.OOO...O.O.O.O....O.',
'...OO...O..OO.OOO.OO......O...O....O.O....O..O..O..O.....O........OOO...OOO.......O..........O....OOO..O..O....OO.O.O..OOO.O...O..OO.O...O.....OO..OOOO..O...O......OOOO.O.OO.O.O.O..OO.O....O',
'OO..OOOOOO...OOO.OOOOOO.OO....OO..O....O...OOOO....O..O....OOO.O.OO.O.O.O...OOO.....O...O....OOO...OO..O.OO.O.OOO...O..O..O....OOO.OO......OOOO.O....O..O.O..O..OO.OO......OO...OOOOO.........',
]
n = 10

ans = timeit(bomberMan, (n, grid3))
# print("Second :",n)
# for i in ans:
#     print(i)

