# top sort
import queue
r'''
        -->d-------->c
       /        /     \
      a-------->b      -->g
       \     /   \    /
         -->e------->f
'''
adj = {
    "a": ["b", "d", "e"],
    "b": ["c", "f"],
    "c": ["g"],
    "d": ["c"],
    "e": ["f"],
    "f": ["g"],
    "g": []
}


def compute_indegree(v, adj):
    counter = 0
    for i in adj:
        for z in adj[i]:
            if z == v:
                counter+=1
    return counter



def top_sort(adjee):
    adj = adj = {k: v[:] for k, v in adjee.items()}
    indegree = {}
    for i in adj:
        indegree[i] = compute_indegree(i, adj)
    rank = {}
    que = queue.Queue()
    for v in indegree:
        if indegree[v] == 0:
            rank[v] = 0
            que.put(v)
    print("start adj:",adj)
    print("start indegrees:",indegree)
    while not que.empty():
        u = que.get()

        if u not in adj:
            continue
        print("HERE IS ADJ", adj)
        neighbors = adj[u]
        del adj[u]

        for w in neighbors:
            indegree[w] -=1
            if indegree[w] == 0:
                rank[w] = rank[u]+1
                que.put(w)
    return rank

print(top_sort(adj))