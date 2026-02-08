import math; INF = math.inf
# single source shortest paths
def bellman(v, adj):
    n = len(adj)
    dist = [INF] * n
    parent = [None] * n

    dist[v] = 0.0

    for i in range(n-1):
        changed = False
        for u in range(n):
            if dist[u] == INF:
                continue
            for (vertex, distance) in adj[u]:
                if dist[u] + distance < dist[vertex]:
                    dist[vertex] = dist[u] + distance
                    parent[vertex] = u
                    changed = True

            if not changed:
                break

    # detect negative cycles
    neg = False
    for u in range(n):
        if dist[u] == INF:
            continue
        for (vertex, distance) in adj[u]:
            if dist[u] + distance < dist[vertex]:
                neg = True # negative cycle exists
                break

    return dist, parent, neg