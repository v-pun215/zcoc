def binary_search(sorted_list,x):
    low = 0
    high = len(sorted_list)-1
    while low<=high:
        middle = low + (high-low)//2
        if sorted_list[middle]>x:
            high = middle-1
        elif sorted_list[middle]<x:
            low = middle+1
        else:
            return middle
    return -1

print(binary_search([1,2,3], 3))