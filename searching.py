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
to_search = 0
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
print(binary_search(elements, to_search))