li = [1    ,3    ,2    ,1    ,4    ,1    ,3    ,2    ,1    ,1    ,2]

def sliding_window(k, li):
    n = len(li)
    # for each i, compute if there is a segment starting at i that adds up exactly to K
    current_sum = 0
    start = 0
    results = []

    for end in range(n):
        current_sum += li[end]

        while current_sum > k and start <= end:
            current_sum-= li[start]
            start+=1

        if current_sum == k:
            print("solution found at index", start)
            results.append((start, end))

    return results

#print(sliding_window(8, li))
import math
INF = math.inf
def sliding_2_plots(K, li):
    n = len(li)
    lbest = [INF for _ in range(n)]
    rbest = [INF for _ in range(n)]

    current_sum, start = 0, 0
    for end in range(n):
        current_sum += li[end]
        while current_sum>K:
            current_sum-=li[start]
            start+=1
        if current_sum == K:
            length = end - start+ 1
            rbest[start] = length
            lbest[end] = length

    RBEST = [INF for _ in range(n)]
    LBEST = [INF for _ in range(n)]
    current_min = INF
    for i in range(n):
        current_min = min(current_min, lbest[i])
        LBEST[i] = current_min
    current_min = INF
    for i in reversed(range(n)):
        current_min = min(current_min, rbest[i])
        RBEST[i] = current_min
    
    global_min_combined = INF
    for i in range(n-1):
        if LBEST[i]!= INF and RBEST[i]!= INF:
            global_min_combined = min(global_min_combined, LBEST[i] + RBEST[i])
    return global_min_combined
l = [5, 1, 1, 1, 2, 5, 2, 3]
print(sliding_2_plots(5, l))