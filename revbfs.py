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
import queue
from collections import *
v = [1,2,3,4,5,6,7]
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

def BFS(start, finish, neighbours):
    neighbours = dict(neighbours)
    marked = set()
    marked.add(start)
    parent = dict()
    que = queue.Queue()
    que.put(start)
    while not que.empty():
        u = que.get()
        print("we're at",u)
        if u == finish:
            print("found target!")
        for n in neighbours[u]:
            if n not in marked:
                que.put(n)
                print("arrived at",n)
                parent[n]=u
                marked.add(n)
                if n == finish:
                    print("found target!")
    print("nothing left in queue!")
    if finish not in parent and finish!= start:
        return None

    # retrace steps
    li = deque()
    li.append(finish)
    while True:
        if li[0]==start:
            break
        li.appendleft(parent[li[0]])
    return list(li)

boi = BFS(1,8, ad)
print(boi)