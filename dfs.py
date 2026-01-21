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
from collections import deque
v = [1,2,3,4,5,6,7,8]
ad = {
    1: [2,3],
    2: [1,3,4],
    3: [1, 2],
    4: [2,5,8],
    5: [4, 6],
    6: [5, 7],
    7: [6, 8],
    8: [4, 7]
}


def DFS(graph, node, marked, parent):
    print(node)
    marked.add(node)
    for neighbour in graph[node]:

        if not neighbour in marked:
            parent[neighbour] = node
            print("arrived at", neighbour)
            DFS(graph, neighbour, marked, parent)

marked = set()
parent = {}
DFS(ad, 1, marked, parent)
print(parent)
def retrace_steps(start,  finish, parent):
    li = deque()
    li.append(finish)
    while True:

        first =  li[0]
        parente = parent[first]
        li.appendleft(parente)
        if parente == 1:
            break
    return list(li)

print(retrace_steps(1, 8, parent))