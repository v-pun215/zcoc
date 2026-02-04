#input management
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
    n = len(arr)-1
    for j in range(n):
        if (arr[j]%power(2,i+1)) < power(2,i):
            l.append(arr[j])
        else:
            r.append(arr[j])
    l = order(l, i+1)
    r = order(r, i+1)
    c = concatenate(l,r)
    return c

for _ in range(T):
    p, idx = map(int, input().split())
    print("P and idx", p, idx)
    a = []
    for i in range(2**p):
        a.append(i)
    ans = order(a, 0)
    print(ans)