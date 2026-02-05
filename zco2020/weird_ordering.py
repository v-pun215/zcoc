#input management
import sys
#all_inp = sys.stdin.read().splitlines()
T = int(input())

def power(x,y):
    return x**y
def concatenate(x,y):
    return x+y

def order(arr, i):
    if len(arr) <=1:
        return arr
    l = []
    r= []
    n = len(arr)
    for j in range(n):
        if (arr[j]%power(2,i+1)) < power(2,i):
            l.append(arr[j])
        else:
            r.append(arr[j])
    l = order(l, i+1)
    r = order(r, i+1)
    c = concatenate(l,r)
    return c

inputs = []
for i in range(T):
    ben_stocks = list(map(int, input().split()))
    inputs.append(ben_stocks)
'''
import time
start = time.time()
for i in inputs:

    p, idx = i
    a = []
    for i in range(2**p):
        a.append(i)
    ans = order(a, 0)
    print(ans[idx])
end = time.time() - start
print("time taken:",end)

'''
def solve(p, idx):
    result = 0
    current_idx = idx
    part_size = 2**(p-1)


    for i in range(p):
        if current_idx>=part_size:
            result+=2**i
            current_idx-=part_size
        part_size/=2

    return result


for inp in inputs:
    p, idx = inp
    print(solve(p,idx))