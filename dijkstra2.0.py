import queue,math
INF = math.inf

adj_list = {
    1: [(2, 100), (3, 800)],
    2: [(1, 100), (3, 60), (5, 200)],
    3: [(1, 800), (2, 60), (4, 700)],
    4: [(3, 700)],
    5: [(2, 200), (6, 500), (7, 100)],
    6: [(5, 500), (7, 50)],
    7: [(5, 100), (6, 50)]
}
# single source shortest paths.
def dijkstra(v, adj):
    que = queue.PriorityQueue()
    marked = set()

    dist = {v:0.0} # initialise dist dict with 0 distance for starting vertex
    parent = {} # to retrieve path
    que.put((0.0, v)) # dist, vertex

    while not que.empty():
        d_u, u = que.get() # pull index

        if u in marked:
            continue # skip u if already marked

        marked.add(u)

        for neighbor in adj.get(u, []):
            vertex, weight = neighbor
            if vertex in marked:
                continue # skip if neighbor already marked
            w = float(weight)

            new_distance = d_u + w
            if new_distance < dist.get(vertex, INF):
                dist[vertex] = new_distance
                parent[vertex] = u
                que.put((new_distance, vertex))

    return dist

print(dijkstra(1, adj_list))