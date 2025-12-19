'''
Binary Search

list = [1,2,3,4,5,6,7,8,9] (must be sorted)

we search for 6
get middle element: 5
middle is less than search
hence we must now look in second part: [6,7,8,9]
middle here is n+1/2: 8
6 is less than 8, so we now see in first part: [6,7]
we take middle here as n+1/2: 7
as 6 is less than 7, we must now see first part: [6]
as middle here is just the element, middle = 6
as middle = search, we can see it is here!


'''
# lets code this!
elements = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
to_search = 4
def binary_search(elements, to_search):
    no_of_elements = len(elements)

    if no_of_elements ==1:
        return elements[0]==to_search
    else:
        pass
    middle_index = ((no_of_elements)/2)-1 if no_of_elements%2==0 else ((no_of_elements+1)/2)
    middle_element = elements[int(middle_index)]
    first_half = elements[:int(middle_index)]
    second_half = elements[int(middle_index):]
    if middle_element>to_search:
        return binary_search(first_half, to_search)
    elif middle_element<to_search:
        return binary_search(second_half, to_search)
    elif middle_element==to_search:
        return True
#print(binary_search(elements, to_search))

'''
better, iterative binary search (im too dumb)

we have a function that takes the arr to search in and the value to search x

so we take var low as 0 
we take high as no of elements in arr - 1 to counteract 0 based indexing

while low is lower than high
we take mid point as low + (high -low) // 2

if arr[mid] is less than x:
    low = mid+1
elif arr[mid] is more than x:
    high = mid-1
else: # it can be = to
    return mid

return -1 (if not found)
'''
# WORKING!

def iterative_bs(arr, x):
    low =0
    high = len(arr)-1

    while low<=high:
        mid_index = low + (high-low)//2

        if arr[mid_index]<x:
            low = mid_index+1
        elif arr[mid_index]>x:
            high = mid_index-1
        else:
            return mid_index
    return -1

print(iterative_bs([2, 8, 10, 6, 5, 1, 3, 7, 4], 1))