# who doesnt love fruits (subtle foreshadowing)

#imports
import queue
from collections import deque, defaultdict

# input management
nmk = list(map(int, input().split()))
N, M, K = nmk[0], nmk[1], nmk[2]

matrix = []
for i in range(N):
    inp = list(map(int, input().split()))
    matrix.append(inp)


Q = int(input())
operations = []
for i in range(Q):
    operations.append(list(map(int, input().split())))

'''
INPUT TAKEAWAY
N = number of rows
M = number of columns
K = number of DISTINCT fruits (labelled 1 to K)
we get a matrix of the farm. (i, j) represents a field.

OPERATIONS:
In input, we get the type of operation and then the variables required by the operation to take place.

2 TYPES:
Type 1 (T=1) - we recieve (i, j) and a fruit X and we must change the value of (i, j) in matrix to X (if not already X)
Type 2 (T=2) - we recieve 2 distinct fuits U and V. we need to find field (x1, y1) that grows fruit U and field (x2, y2) that grows fruit V such that a bee (that always takes the shortest path) will take the longest time to traverse.

OUTPUT:
For each Type 2 operation, output largest time possible whilst still taking the shortest path ofc.

(Type 1 operation changes values internally so no output required.)
'''

'''
DRY RUN

N=5 M=5 K=9

MATRIX
7 1 5 5 4
2 4 6 2 8
7 1 3 5 6
9 4 4 8 2
1 3 6 9 3

Q = 1
T=2 U=1 V=3 (since op is type 2, we get U and V)

adjacency list:

'''
def BFS(v,end, matrix):
    # v must be (x1, y1) (1 based indexing on both axes)
    # end must be (x2, y2) (1 based indexing on both axes)

    marked = set()
    marked.add(v)
    que = queue.Queue()
    que.put(v)
    length = {}
    length[v] = 0
    while not que.empty():
        u = que.get()
        x = u[0]
        y = u[1]
        if u == end:  
            return length[u]
        if x+1<len(matrix[y]): # go right
            neighbor = (x+1, y)
            if not neighbor in marked:
                length[neighbor] = length[u]+1
                marked.add(neighbor)
                que.put(neighbor)
        
        if x-1>=0: # go left
            neighbor = (x-1, y)
            if not neighbor in marked:
                length[neighbor] = length[u]+1
                marked.add(neighbor)
                que.put(neighbor)
            
        if y-1>=0: # go up
            neighbor = (x, y-1)
            if not neighbor in marked:
                length[neighbor] = length[u]+1
                marked.add(neighbor)
                que.put(neighbor)
        
        if y+1<len(matrix): # go down
            neighbor = (x, y+1)
            if not neighbor in marked:
                length[neighbor] = length[u]+1
                marked.add(neighbor)
                que.put(neighbor)
    return None

def manhattan(v, end):
    x1 = v[0]
    y1 = v[1]
    x2 = end[0]
    y2 = end[1]

    new_york = abs(x1-x2) + abs(y1-y2)
    return new_york

def change_fruit(field, X, mrx, fruits):
    x = field[0]
    y = field[1]
    value = mrx[y][x]
    if not value == X:
        mrx[y][x] = X
        fruits[value].remove((x,y))
        fruits[X].append((x,y))
    return mrx, fruits
    

def get_all(U, V,matrix):
    all_u = []
    all_v = []
    for indexk, k in enumerate(matrix):
        for indexj, j in enumerate(k):
            if j == U:
                all_u.append((indexj,indexk))
            if j == V:
                all_v.append((indexj, indexk))
    return all_u, all_v

fruit_positions = defaultdict(list)
for i in range(N):
    for z in range(M):
        fruit_positions[matrix[i][z]].append((z,i))
for op in operations:
    T = op[0]
    if T == 1: # operation 1
        i = op[1]-1
        j = op[2]-1
        X = op[3]
        matrix, fruit_positions = change_fruit((j,i), X, matrix, fruit_positions)
    elif T == 2: #operation 2
        U = op[1]
        V = op[2]
        all_u, all_v = fruit_positions[U], fruit_positions[V]
        comparisons = []
        for u in all_u:
            for v in all_v:
                comparisons.append(manhattan(u,v))
        '''
        leftmost_u = min(all_u, key=lambda x: x[0])
        leftmost_v = min(all_v, key=lambda x: x[0])

        rightmost_u = max(all_u, key=lambda x: x[0])
        rightmost_v = max(all_v, key=lambda x: x[0])

        topmost_u = min(all_u, key=lambda x: x[1])
        topmost_v = min(all_v, key=lambda x: x[1])

        bottommost_u = max(all_u, key=lambda x: x[1])
        bottommost_v = max(all_v, key=lambda x: x[1])

        extremes_u = [leftmost_u, rightmost_u, topmost_u, bottommost_u]
        extremes_v = [leftmost_v, rightmost_v, topmost_v, bottommost_v]

        for u in extremes_u:
            for v in extremes_v:
                comparisons.append(manhattan(u, v))'''
        print(max(comparisons))

