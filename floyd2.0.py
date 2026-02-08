import math
INF = math.inf


def floyd(matrix, no_edge_value=0):
    n = len(matrix)
    dist = [[INF] * n for _ in range(n)]
    nxt = [[None] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            w = matrix[i][j]
            if i == j:
                dist[i][j] = 0.0
                nxt[i][j] = j
                continue

            if w == no_edge_value:
                continue
            dist[i][j] = float(w)
            nxt[i][j] = j

    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue # skip those that are infinity
            for j in range(n):
                if dist[k][j] == INF:
                    continue
                new_distance = dist[i][k] + dist[k][j]

                if new_distance < dist[i][j]:
                    dist[i][j] = new_distance
                    nxt[i][j] = nxt[i][k]

    return dist
matrix = [
    [0, 1, 4],    # 0→1 (weight 1), 0→2 (weight 4)
    [0, 0, 2],    # 1→2 (weight 2)
    [0, 0, 0]     # no outgoing edges from 2
]
print(floyd(matrix))