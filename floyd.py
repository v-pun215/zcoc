# floyd warshall impl
import math
INF = math.inf

def floyd_warshall(matrix, no_edge_value=0):
    n = len(matrix)
    dist = [[INF] * n for _ in range(n)]
    nxt = [[None] * n for _ in range(n)]

    for i in range(n):
        for j in range (n):
            w = matrix[i][j] #weight from adj mrx
            if i == j:
                dist[i][j] = 0.0
                nxt[i][j] = j
                continue

            if w is None:
                continue
            if (no_edge_value is not None) and (w == no_edge_value):
                continue
            if isinstance(w, (int, float)) and math.isinf(w):
                continue

            dist[i][j] = float(w)
            nxt[i][j] = j
    
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                if dist[k][j] == INF:
                    continue
                nd = dist[i][k] + dist[k][j]
                if nd < dist[i][j]:
                    dist[i][j] = nd
                    nxt[i][j] = nxt[i][k]

    return dist, nxt

matrix = [
    [0,   5,   0,  10],   # 0 -> 1 (5), 0 -> 3 (10)
    [0,   0,   3,   0],   # 1 -> 2 (3)
    [0,   0,   0,   1],   # 2 -> 3 (1)
    [0,  -2,   0,   0],   # 3 -> 1 (-2)  (negative edge, but no negative cycle)
]

print(floyd_warshall(matrix))