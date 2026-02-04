N, M = list(map(int, input().split())) # n = number of rows, m = no of columns

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

Q = int(input()) # q = number of days the chef will travel
travels = []
for _ in range(Q):
    travels.append(list(map(int, input().split())))
import queue
def grid_BFS(start, end, adj):
    marked = set()
    marked.add(start)
    length = {} # we will be multiplying so 0 is not ideal here
    length[start] = matrix[start[1]][start[0]]
    que = queue.Queue()
    que.put(start)
    while not que.empty():
        u = que.get() # get first vertice
        x, y = u[0], u[1]
        current_val = matrix[y][x]

        # go right
        if x+1<=M-1:
            if not (x+1, y) in marked:
                marked.add((x+1, y))
                que.put((x+1, y))
                length[(x+1,y)]=length[u]*matrix[y][x+1]
                if (x+1,y) == end:
                    break
        
        # go down
        if y+1<=N-1:
            if not (x, y+1) in marked:
                marked.add((x, y+1))
                que.put((x, y+1))
                length[(x, y+1)] = length[u]*matrix[y+1][x]
                if (x, y+1) == end:
                    break
    
    return length



for (a, b, c, d) in travels:
   start = (b-1, a-1)
   end = (d-1, c-1)
   answer = grid_BFS(start, end, matrix)
   print(answer[end])
