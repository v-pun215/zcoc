#Bubblesort
'''
compare adjacent elements to sort list



'''
def bubblesort(arr):
    n = len(arr) # no of elements

    for i in range(n): # 0 to n
        swapped = False 
        for j in range(0,n-i-1): # 0 to n-1-1 (if first it of i, i = 0; n=8;so till 7)
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
'''
arr=[9,8,7,6,5,4,2,1]
bubblesort(arr)
print(arr)
'''
#--------------
#Mergesort
'''
keep dividing into 2 and solve seperately

'''

def merge(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    new_arr = []

    while n1> 0 and n2 >0:
        print("arr1[0]", arr1[0])
        print("arr2[0]",arr2[0])
        new_arr.append(min(arr1[0],arr2[0]))
        if arr1[0]<arr2[0]:
            arr1.pop(0)
        elif arr2[0]<arr1[0]:
            arr2.pop(0)
        else:
            arr1.pop(0)
            arr2.pop(0)
        n1 = len(arr1)
        n2 = len(arr2)
    if n1==0 and n2 != 0:
        for e in arr2:
            new_arr.append(e)
    elif n2==0 and n1!=0:
        for e in arr1:
            new_arr.append(e)
    return new_arr



def mergesort(arr):
    n = len(arr)
    if n == 1:
        print("n is 1", arr)
        return arr
    elif n == 2:
        if arr[0]>arr[1]:
            arr[0],arr[1] = arr[1],arr[0]
        print("n is 2", arr)
        return arr
    mid = (n//2 ) if n%2==0 else n//2+1
    first = arr[:mid]
    second = arr[mid:]
    print("first", first)
    print("second", second)
    print("--------------")
    return merge(mergesort(first),mergesort(second))

array = [9,9,999,6,2,5,3,2,8]
#print(mergesort(array))


# Quicksort
'''
take any element as "pivot", here taking first element


'''

def quicksort(arr):
    n = len(arr)
    if n ==0:
        return []
    elif n == 1:
        return arr
    pivot = arr[0]
    arr.pop(0)
    lesser = []
    greater = []
    for e in arr:
        if e>pivot:
            greater.append(e)
        else:
            lesser.append(e)
    return quicksort(lesser)+[pivot]+quicksort(greater)
print(quicksort(array))
