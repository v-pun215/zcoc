# floyd warshall impl
import math
INF = math.inf
# all pair shortest paths
def floyd_warshall(matrix, no_edge_value=0):
    n = len(matrix)
    dist = [[INF] * n for _ in range(n)] # initialise distances to maximum possible value (infinity & beyond!)
    nxt = [[None] * n for _ in range(n)] # helps reconstruct paths later down the line

    for i in range(n):
        for j in range(n):
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
# adj matrix
matrix = [
    [0, 1, 4],    # 0→1 (weight 1), 0→2 (weight 4)
    [0, 0, 2],    # 1→2 (weight 2)
    [0, 0, 0]     # no outgoing edges from 2
]
mat = [[1, 0, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0]]
print(floyd_warshall(matrix))