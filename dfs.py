matrix = [
    [70, 80, 80, 70],
    [60, 30, 20, 30],
    [50, 40, 10, 50],
    [45, 60, 20, 10]
]
def DFS(v, end, matrix):
    marked = set()
    marked.add(v)
    #right
    x = v[0]
    y = v[1]
    if x+1 < len(matrix[y])+1:
        if abs(matrix[y][x+1]-matrix[y][x])<=10:
            if not [x+1, y] in marked:
                vare = [x+1,y]
                DFS(vare, end, matrix)
    if y+1 < len(matrix)+1:
        if abs(matrix[y+1][x]-matrix[y][x])<=10:
            if not [x,y+1] in marked:
                vare  = [x,y+1]
                DFS(vare,end,matrix)
    if y-1 >=0:
        if abs(matrix[y-1][x]-matrix[y][x])<=10:
            if not [x,y-1] in marked:
                vare = [x,y-1]
                DFS(vare,end,matrix)
    if x-1>=0:
        if abs(matrix[y][x-1]-matrix[y][x])<=10:
            if not [x-1,y] in marked:
                vare = [x-1,y]
                DFS(vare,end,matrix)