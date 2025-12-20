n = int(input())
arr = list(map(int, input().split()))
previous = None
moves = 0
for index, element in enumerate(arr):
    if previous == None:
        previous = element
        continue
    if previous>element:
        diff = previous-element
        moves+=diff
    else:
        previous = element
print(moves)