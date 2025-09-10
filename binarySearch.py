def linear_search(number_list, number_to_find):
    for index, element in enumerate(number_list):
        if element == number_to_find:
            return index
    return -1

def binary_search(number_list, number_to_find):
    left_index = 0
    right_index = len(number_list) - 1
    mid_index = (left_index + right_index) // 2
    mid_index = 0
    
    while left_index <= right_index:
        mid_index = (left_index + right_index) //2
        mid_value = number_list[mid_index]
        if mid_value == number_to_find:
            return mid_index
        elif mid_value < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
        
    return -1

def binary_search_recursive(number_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1
    
    mid_index = (left_index + right_index) // 2
    mid_value = number_list[mid_index]
    
    if mid_value == number_to_find:
        return mid_index
    
    elif mid_value > number_to_find:
        right_index = mid_index - 1
    else:
        left_index = mid_index + 1
        
    return binary_search_recursive(number_list, number_to_find, left_index, right_index)

def find_all_indices(number_list, number_to_find):
    index = binary_search(number_list, number_to_find)
    indices = [index]
    
    i = index - 1
    while i >= 0 and number_list[i] == number_to_find:
        indices.append(i)
        i -= 1
    
    i = index + 1
    while i < len(number_list) and number_list[i] == number_to_find:
        indices.append(i)
        i += 1
    
    return sorted(indices)


if __name__ == "__main__":
    number_list = [1,3,5,7,9,11,13,15,17,19,21]
    number_to_find = 21
    
    linear_search_index = linear_search(number_list, number_to_find)
    print(f"Index of {number_to_find} using linear search: {linear_search_index}")
    
    binary_search_index = binary_search(number_list, number_to_find)
    print(f"Index of {number_to_find} using binary search: {binary_search_index}")
    
    binary_search_recursive_index = binary_search_recursive(number_list, number_to_find, 0, len(number_list)-1)
    print(f"Index of {number_to_find} using binary search recursive: {binary_search_recursive_index}")
    
    find_all_indices_list = find_all_indices([1,3,5,7,9,11,13,15,17,19,21,21,21], 21)
    print(f"All indices of {number_to_find} using binary search: {find_all_indices_list}")