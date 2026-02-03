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

print(sliding_window(8, li))
