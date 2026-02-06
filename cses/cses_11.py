t = int(input())
testcases = []
for _ in range(t):
    testcases.append(tuple(map(int, input().split())))

for i in testcases:
    a, b = i
    total_sum = a+b
    result = None
    if total_sum%3 == 0 and max(a, b) <= 2 *min(a, b):
        result = True
    else:
        result = False

    print("YES" if result else "NO")