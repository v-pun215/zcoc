# Bellman-Ford implementation in Python!

adjacency_list = { # vertex, weight
  0: [(1, 5),  (3, 10)],
  1: [(2, 3)],
  2: [(3, 1)],
  3: [(1, -2)]
}
# single source shortest paths
import math
INF = math.inf
def bellman_ford(root, adj):
    n = len(adj)
    dist = [INF] * n 
    parent = [None] *n 
    
    dist[root] = 0.0

    for i in range(n-1):
        changed = False
        for u in range(n):
            if dist[u] == INF:
                continue
            for (v, w) in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = u
                    changed = True
        if not changed:
            break
    neg_cycles = False
    for u in range(n):
        if dist[u] == INF:
            continue
        for (v, w) in adj[u]:
            if dist[u]+w < dist[v]:
                print("NEGATIVE CYCLE EXISTS!!!")
                neg_cycles = True
                break

    return dist, parent, neg_cycles

print(bellman_ford(0, adjacency_list))