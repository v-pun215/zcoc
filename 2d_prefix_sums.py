def max_mango_trees(grid, N):
    # M[i][j] = number of mangos in rectangle from (0,0) to (i,j)
    M = [[0] * (N + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            tree_value = grid[i-1][j-1]  # 1 if tree, 0 otherwise
            M[i][j] = tree_value + M[i-1][j] + M[i][j-1] - M[i-1][j-1]
    
    total_mangos = M[N][N]
    max_min_rectangle = 0
    
    #try all possible cuts
    for x in range(1, N):
        for y in range(1, N):
            
            top_left = M[x][y]
            top_right = M[N][y] - M[x][y]
            bottom_left = M[x][N] - M[x][y]
            bottom_right = total_mangos - top_left - top_right - bottom_left
            
            # ramu gets
            min_rectangle = min(top_left, top_right, bottom_left, bottom_right)
            
            # maximize the minimum
            max_min_rectangle = max(max_min_rectangle, min_rectangle)
    
    return max_min_rectangle



grid = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0]
]

N = 6
result = max_mango_trees(grid, N)
print(f"Maximum mango trees Ramu can guarantee: {result}")
def print_grid(grid, N):
    for row in grid:
        print(' '.join(['#' if x == 1 else '.' for x in row]))

print("\nOriginal grid:")
print_grid(grid, N)