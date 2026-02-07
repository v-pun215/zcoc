from collections import defaultdict
import queue

N, M = map(int, input().split()) # N is num of ppl in class, M is pair of friends

D = list(map(int, input().split()))
D_dict = {}
for index, i in enumerate(D):
    D_dict[index+1] = i

friend_list = defaultdict(list)
for _ in range(M):
    e, f = map(int, input().split())
    friend_list[e].append(f)
    friend_list[f].append(e)


def BFS(v, adj):
    if not adj[v]:
        return [], {}
    marked = set()
    marked.add(v)
    que = queue.Queue()
    parent = {}
    que.put(v)
    level = {}
    level[v] = 0
    while not que.empty():
        u = que.get()
        for neighbour in adj[u]:
            if not neighbour in marked:
                marked.add(neighbour)
                que.put(neighbour)
                level[neighbour] = level[u]+1
                parent[neighbour] = u
    marked.remove(v)
    level.pop(v)
    return list(marked), level

def calculate_earliest_day(person, friend_list, level):
    earl = D_dict[person]
    
    for fren in friend_list:
        fren_value = D_dict[fren]
        fren_level = level[fren]
        if fren_value>earl:
            earl=fren_value-fren_level
        if fren_value == -1:
            earl = -1
            break
    return earl
anser = []

for index, i  in enumerate(D):
    friends, friend_levels = BFS(index+1, friend_list)
    name = index+1
    # no friends: the earliest they can find out is their own D (or -1 if they never should learn)
    if not friends:
        anser.append(D_dict[name])
        continue

    anser.append(calculate_earliest_day(name, friends, friend_levels))

print(*anser)