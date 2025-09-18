def merge_sort(arr, key="name"):
    if len(arr) <= 1:
        return 
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    
    merge_sort(left, key)
    merge_sort(right, key)
    
    merge_two_sorted_list(left, right, arr, key)


def merge_two_sorted_list(a, b, arr, key="name"):
    i = j = k = 0
    
    while i < len(a) and j < len(b):
        if a[i][key] < b[j][key]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j] 
            j += 1
        k += 1
        
    while i < len(a):
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1


if __name__ == "__main__":
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab',     'age': 12, 'time_hours': 3},
        { 'name': 'vignesh',   'age': 21, 'time_hours': 2.5},
        { 'name': 'chinmay',   'age': 24, 'time_hours': 1.5},
    ]
    
    # Sort by name (default)
    merge_sort(elements, key="name")
    print("Sort by name:", elements)

    # Sort by age
    merge_sort(elements, key="age")
    print("Sort by age:", elements)

    # Sort by time_hours
    merge_sort(elements, key="time_hours")
    print("Sort by time_hours:", elements)
