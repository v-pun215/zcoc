from collections import deque
with open("buckets.in", "r") as inp:
    input_ = inp.read().splitlines()

grid = list(map(list, input_))


def find_char(grid, char):
    for index, element in enumerate(grid):
        for i, e in enumerate(element):
            if e == char:
                return [index, i]
    return None

B_coords = find_char(grid, "B")
L_coords = find_char(grid, "L")



def bfs(grid, sr, sc, tr, tc):
    n = len(grid)
    m = len(grid[0])

    visited = [[False]*m for _ in range(n)]
    dist = [[-1]*m for _ in range(n)]

    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = True
    dist[sr][sc] = 0

    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    while q:
        r, c = q.popleft()

        if (r, c) == (tr, tc):
            return dist[r][c]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc] and grid[nr][nc] != 'R':
                    visited[nr][nc] = True
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

    return -1

anseer = bfs(grid, B_coords[0],B_coords[1], L_coords[0], L_coords[1])-1
with open("buckets.out", "w") as out:
    out.write(str(anseer))