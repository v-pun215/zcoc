def bin_search(arr,x):
    low = 0
    high = len(arr)-1
    while low<=high:
        midindex = low+ (high-low)//2
        if arr[midindex]>x:
            high = midindex-1
        elif arr[midindex]<x:
            low = midindex+1
        else:
            return midindex
    return -1
    

print(bin_search([1,2,3],3))