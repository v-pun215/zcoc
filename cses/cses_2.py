n = int(input())

arr = list(map(int, input().split()))

s = set(arr)
ideal_arr = range(1, n+1)



for i in ideal_arr:
    if i not in s:
        print(i)
        break



'''
def quicksort(arr):
    n = len(arr)
    if n==0:
        return []
    elif n==1:
        return arr
    pivot = arr[0]
    arr.pop(0)
    lesser = []
    greater = []
    for i in arr:
        if i<=pivot:
            lesser.append(i)
        elif i>pivot:
            greater.append(i)
    return quicksort(lesser)+[pivot]+quicksort(greater)
arr = quicksort(arr)'''

'''
for i, e in enumerate(ideal_arr):
    try:
        if e!=arr[i]:
            print(ideal_arr[i])
            break
    except IndexError:
        print(ideal_arr[i])
        break
'''

