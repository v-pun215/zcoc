# Soldiers and Bananas

inp = list(map(int, input().split()))
k = inp[0]
n = inp[1]
w = inp[2]


cost = 0
for i in range(1, w+1):
    cost+=i*k

if cost>n:
    borrow = cost-n
else:
    borrow = 0

print(borrow)