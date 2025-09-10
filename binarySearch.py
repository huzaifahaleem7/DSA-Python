def linear_search(number_list, number_to_find):
    for index, element in enumerate(number_list):
        if element == number_to_find:
            return index
    return -1

def binary_search(number_list, number_to_find):
    left_index = 0
    right_index = len(number_list) - 1
    mid_index = (left_index + right_index) // 2
    mid_value = number_list[mid_index]
    
    while left_index <= right_index:
        if mid_value == number_to_find:
            return mid_index


if __name__ == "__main__":
    number_list = [1,3,5,7,9,11,13,15,17,19,21]
    number_to_find = 1
    
    linear_search_index = linear_search(number_list, number_to_find)
    print(f"Index of {number_to_find} using linear search: {linear_search_index}")