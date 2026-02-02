# implementation of dijkstra's algorithm: single source shortest paths
import queue, math

'''
            700
        3 ------ 4
  800 / |
    /   | 60
  /     |             500
 1------2 ------ 5 --------- 6
   100      200    \       /
                 100 \   / 50
                       7

'''
adj_list = {
    1: [(2, 100), (3, 800)],
    2: [(1, 100), (3, 60), (5, 200)],
    3: [(1, 800), (2, 60), (4, 700)],
    4: [(3, 700)],
    5: [(2, 200), (6, 500), (7, 100)],
    6: [(5, 500), (7, 50)],
    7: [(5, 100), (6, 50)]
}
INF = math.inf
def dijkstra(v,adj):
    que = queue.PriorityQueue() # queue must contain DISTANCES!
    marked = set()

    dist = {v:0.0}
    parent = {}
    que.put((0.0, v)) # distance to self = 0
    while not que.empty():
        d_u, u = que.get()
        if u in marked:
            continue # skip if in marked
        marked.add(u)
        print("we're at", u, "(dist =", d_u, ")")
        
        for item in adj.get(u, []):
            vertex, w = item
            if vertex in marked:
                continue
            w_val = float(w)
            nd = d_u + w_val
            if nd < dist.get(vertex, INF):
                dist[vertex] = nd
                parent[vertex] = u
                que.put([nd, vertex])
                print("arrived at", v, "(new dist =", nd, ")")

    print("nothing in queue")
    return dist

print(dijkstra(1, adj_list))
