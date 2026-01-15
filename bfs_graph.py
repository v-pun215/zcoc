from collections import *
import queue
r'''
          1
         / \
        2---3
        |                   
        4---8
        |   |
        5   7
         \ /
          6

'''
vertices = [1, 2, 3, 4, 5, 6, 7, 8]
edges = [
    (1, 2),
    (1, 3),
    (2, 3),
    (2, 4),
    (4, 5),
    (4, 8),
    (5, 6),
    (6, 7),
    (7, 8)
]


def build_adj(vertices, edges):
    output = {v: [] for v in vertices}
    for u, v in edges:
        output[u].append(v)
        output[v].append(u)
    return output

adj = build_adj(vertices,edges)

def BFS(v, end, adj):
    adj = dict(adj)
    marked = set()
    marked.add(v)
    parent = {}
    parents = defaultdict(list)
    length = {}
    length[v] = 1
    que = queue.Queue()
    que.put(v)
    while not que.empty():
        val = que.get()
        neighbours = adj.get(val)
        for u in neighbours:
            parents[u].append(val)
            if not u in marked:
                marked.add(u)
                length[u] = length[val]+1
                parent[u] = val

                que.put(u)

    # Recover path
    li = deque()
    li.append(end)
    while True:
        value =parent.get(li[0])

        li.appendleft(value)
        if value == 1:
            break
    return list(li), dict(parents)
print(BFS(1, 8, adj))