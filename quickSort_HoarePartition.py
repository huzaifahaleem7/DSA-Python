def swapp(start, end, elements):
    temp = elements[start]
    elements[start] = elements[end]
    elements[end] = temp

def partiton(elements, start, end):
    pivot_index = start
    pivot_element = elements[pivot_index]
    start_index = start + 1
    end_index = end
    
    while start_index < end_index:
        while start_index < len(elements) and elements[start_index] <= pivot_element:
            start_index += 1
        while elements[end_index] > pivot_element:
            end_index -= 1
            
        if start_index < end_index:
            swapp(start_index, end_index, elements)  
    swapp(pivot_index, end_index, elements)
    
    return end_index  
        
        
def quick_sort(elements, start, end):
    if start < end:
        pi = partiton(elements, start, end)
        quick_sort(elements, start, pi - 1)
        quick_sort(elements, pi + 1, end)

if __name__ == "__main__":
    elements = [11,9,29,7,2,15,28]
    quick_sort(elements, 0 , len(elements)-1)
    print(elements)