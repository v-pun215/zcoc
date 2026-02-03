import itertools
def naive(li):
    n = len(li)
    n_list = range(n)
    all_pairs = list(itertools.combinations_with_replacement(n_list, 2))
    sums = []
    for i in all_pairs:
        current_slice = li[i[0] : i[1] + 1]
        sums.append(sum(current_slice))

    return max(sums)
li = [3, -1,  2, -1,  2, -3,  4, -2, 1,  2,  1]

def smarter(li):
    n = len(li)
    n_list = range(n+1)
    all_pairs = list(itertools.combinations_with_replacement(n_list, 2))
    prefixSum = [0]
    current = 0
    for i in li:
        current +=i
        prefixSum.append(current)
    sums = []
    for (i, j) in all_pairs:
        sum_ = prefixSum[j] - prefixSum[i]
        sums.append(sum_)
    return max(sums)
from functools import lru_cache

@lru_cache(None)
def best_ending_at(i, li):
    if i == 0:
        return (li[0], 0)
    
    prev_sum, prev_start = best_ending_at(i-1, li)

    if li[i] > li[i] + prev_sum:
        return (li[i], i)
    else:
        return (li[i] + prev_sum, prev_start)

def smartest(li):
    results = [best_ending_at(i, tuple(li)) for i in range(len(li))]
    max_sum, start = max(results, key=lambda x: x[0])

    return max_sum
import random

# A list of 5,000 numbers between -100 and 100
test_li = [random.randint(-100, 100) for _ in range(5000)]
import time
# Analysis
start_time = time.time()
print(smartest(test_li)) # O(n)
print(time.time() - start_time)

start_time = time.time()
print(smarter(test_li)) # O(n^2)
print(time.time() - start_time)

start_time = time.time()
print(naive(test_li)) # O(n^3)
print(time.time() - start_time)

'''
OUTPUT:
9521                # smartest
0.15636801719665527 
9521                # smarter
0.9429628849029541  
9521                # naive
92.35004425048828
'''