# Bit strings!

import itertools

def all_possible_permutations(arr):
    return list(set(itertools.permutations(arr)))

def check(arr):
    # stupid brute force approach for a problem with a minimal constraint
    sum_all = sum(arr)
    half_sum = sum_all//2
    su1 = False
    set1 = None
    set2 = None
    for index, i in enumerate(arr):
        if not su1:
            su1 = i
            continue
        su1+=i
        if su1 == half_sum:
            set1 = arr[:index+1]
            set2 = arr[index+1:]
            break
    if not set1 == None and not set2 == None and sum(set1)==sum(set2):
        return set1, set2
    else:
        return False

def efficient_check(arr):
    n = len(arr)
    total_sum = n * (n+1) // 2

    if total_sum % 2 != 0:
        return False
    target = total_sum//2
    set1 = []
    set2 = []
    for i in range(n, 0, -1):
        if i <= target:
            set1.append(i)
            target-=i
        else:
            set2.append(i)

    return set2, set1

n = int(input())
arr = list(range(1, n+1))

answ = efficient_check(arr)
if answ:
    set1 = answ[0]
    set2 = answ[1]

if answ:
    print("YES")
    print(len(set1))
    print(*set1)
    print(len(set2))
    print(*set2)
else:
    print("NO")