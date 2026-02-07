# this works!

N, M, K, B = map(int, input().split())
testcases = [] # (H, W)
for _ in range(N):
    testcases.append(tuple(map(int, input().split())))

'''
formula to get dist traveled by boat:
abs(H - W) + B

formula to get dist travelled by bridge at index BR
abs(H- BR) + abs(W-BR) + 1

'''
boat_distances = []
for value in testcases:
    H, W = value
    dist = abs(H - W) + B
    boat_distances.append(dist)

all_bridge_indexes = range(K)
tolerances = []
for BR in all_bridge_indexes:
    T = []
    for index, value in enumerate(testcases):
        H, W = value
        bridge_dist = abs(H - BR) + abs(W - BR) + 1
        T.append(bridge_dist - boat_distances[index])
    T.sort()
    tolerances.append(T)

T = min(tol[M-1] for tol in tolerances)
print(max(0, T))
