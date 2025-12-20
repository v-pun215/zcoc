n = int(input())
if n == 1:
    print(1)
    exit()
arr = []
for i in range(1,n+1):
    arr.append(i)

odd = []
even = []
for i in arr:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

perm = []
if abs(even[-1]-odd[0])>1:
    perm = even+odd
elif abs(odd[-1]-even[0])>1:
    perm = odd+even

if not len(arr) == len(perm):
    print("NO SOLUTION")
else:
    print(*perm)