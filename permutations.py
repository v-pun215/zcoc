def generate_permutation(inp):
    # Convert the input string to a list of characters for easier manipulation
    characters = list(inp)
    length = len(characters)
    
    # Step 1: Find the rightmost character that is smaller than its next character
    # This is the "pivot" point where we need to make a change
    pivot = length - 2
    while pivot >= 0 and characters[pivot] >= characters[pivot + 1]:
        pivot -= 1
    
    # If no such pivot exists, the string is in descending order (last permutation)
    if pivot < 0:
        return None
    
    # Step 2: Find the smallest character to the right of pivot that is larger than pivot
    # This is the character we'll swap with the pivot
    swap_index = length - 1
    while characters[swap_index] <= characters[pivot]:
        swap_index -= 1
    
    # Step 3: Swap the pivot with the found character
    characters[pivot], characters[swap_index] = characters[swap_index], characters[pivot]
    
    # Step 4: Reverse everything after the pivot position
    # This gives us the smallest permutation for the suffix
    characters[pivot + 1:] = characters[pivot + 1:][::-1]
    
    return ''.join(characters)
print(generate_permutation("fgjlbeckihda"))
