# A better attempt, that attempt was getting way too messy and was not good anyway.
from collections import defaultdict, deque
from pprint import pprint
import queue
# input management
nm = list(map(int, input().split()))
N = nm[0]
M = nm[1]
days_list = list(map(int, input().split()))

'''
Eg.
N=6 M=5
10 6 4 3 -1 6
1 2
2 6
1 6
3 4
4 6

friend_list = {
    1: [2, 6],
    2: [1, 6],
    6: [2, 1, 4],
    3: [4],
    4: [3, 6]
}
'''

friend_list = defaultdict(list)
all_friends = set()
for i in range(M):
    values = list(map(int, input().split()))
    for z in values:
        all_friends.add(z)
    friend_list[values[0]].append(values[1])
    friend_list[values[1]].append(values[0])
friend_list = dict(friend_list)

def BFS(v, adj):
    adj = dict(adj)
    marked = set()
    marked.add(v)
    parent = {}
    parents = defaultdict(list)
    length = {}
    length[v] = 0
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
    return length



answer = []
for guy in range(N):
    earliest_day = days_list[guy]
    if earliest_day == -1:
        answer.append(-1)
        continue
    if not guy+1 in all_friends:
        print("EARLIEST DAY FOUND!", earliest_day)
        answer.append(earliest_day)
        continue
    levels = BFS(guy+1, friend_list)
    friends_days = []
    minus = False
    for key in levels:
        if key == guy+1:
            continue
        value = levels[key]
        day_for_key = days_list[key-1]
        if day_for_key==-1:
            minus=True
        friends_days.append((key, day_for_key, value))
    max_day = -float('inf')
    max_day_person = None
    max_day_distance = None


    arithmetic = earliest_day  # Start with the person's own constraint
    for person, day, distance in friends_days:
        if day == -1:
            continue  # Skip -1 for now, handle separately
        required_start = day - distance
        if required_start > arithmetic:
            arithmetic = required_start

    if minus:  # Check this FIRST!
        arithmetic = -1

    answer.append(arithmetic)

print(*answer)