from collections import defaultdict, deque

# input management
nm = list(map(int, input().split()))
N = nm[0]
M = nm[1]
days_list = list(map(int, input().split()))

friend_list = defaultdict(list)
for i in range(M):
    values = list(map(int, input().split()))
    friend_list[values[0]].append(values[1])
    friend_list[values[1]].append(values[0])

def BFS(v, adj):
    marked = set()
    marked.add(v)
    length = {}
    length[v] = 0
    que = deque([v])
    while que:
        val = que.popleft()
        neighbours = adj.get(val, [])
        for u in neighbours:
            if u not in marked:
                marked.add(u)
                length[u] = length[val] + 1
                que.append(u)
    return length, marked

# Find connected components
visited_global = set()
answer = [0] * N

for person in range(1, N + 1):
    if person in visited_global:
        continue
    
    # Run BFS to find component
    if person in friend_list:
        distances, component = BFS(person, friend_list)
        visited_global.update(component)
    else:
        component = {person}
        visited_global.add(person)
        answer[person - 1] = days_list[person - 1]
        continue
    
    # Check for -1 in component
    has_minus_one = False
    for p in component:
        if days_list[p - 1] == -1:
            has_minus_one = True
            break
    
    if has_minus_one:
        for p in component:
            answer[p - 1] = -1
    else:
        # For each person, calculate their earliest possible day
        for target in component:
            # BFS from target to get distances
            dist_from_target, _ = BFS(target, friend_list)
            
            # Calculate when we'd need to seed at target
            # to satisfy all constraints
            seed_day = days_list[target - 1]
            for p in component:
                if p == target:
                    continue
                # Person p is at distance dist_from_target[p] from target
                # If we seed at target on day T, p learns on day T + dist
                # We need: T + dist >= days_list[p-1]
                # So: T >= days_list[p-1] - dist
                required = days_list[p - 1] - dist_from_target[p]
                seed_day = max(seed_day, required)
            
            # Target learns on seed_day
            answer[target - 1] = seed_day

print(*answer)