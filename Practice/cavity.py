def cavityMap(grid):
    for i in range(len(grid)):
        if i == 0 or i == len(grid)-1:
            continue
        grid[i] = list(grid[i])
        for j in range(len(grid[0])):
            if j == 0 or j == len(grid[0])-1:
                continue
            if grid[i][j] > grid[i][j+1] and grid[i][j] > grid[i][j-1] and grid[i][j] > grid[i+1][j] and grid[i][j] > grid[i-1][j]:
                grid[i][j] = "X"
        
        grid[i] = "".join(grid[i])
        
    
    return (grid)
        


x = "hello"

print(list(x))