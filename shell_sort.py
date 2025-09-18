def shel_sort(arr):
    size = len(arr)
    gap = size // 2
    index_to_delete = []   # list banai indexes store karne ke liye
    
    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j - gap] > anchor:
                if arr[j] == arr[j - gap]:
                    index_to_delete.append(j)   # duplicate index save
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = anchor
        
        gap = gap // 2
    
    return arr, index_to_delete   # dono return karo
            

if __name__ == "__main__":
    elements = [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1]
    sorted_elements, indexes = shel_sort(elements)
    print("Sorted:", sorted_elements)
    print("Indexes to delete (duplicates):", indexes)
