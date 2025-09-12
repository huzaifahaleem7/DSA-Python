
def swapp(i, j, elements):
    temp = elements[i]
    elements[i] = elements[j]
    elements[j] = temp

def partition(elements, start, end):
    pivot_index = end
    pivot_element = elements[pivot_index]
    p_index = start
    
    for i in range(start, end):
        if elements[i] <= pivot_element:
            swapp(i, p_index, elements)
            p_index += 1
    swapp(p_index, pivot_index, elements)
    
    return p_index
        

def quick_sort(elements, start, end):

    if len(elements) == 1:
        return
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi - 1)
        quick_sort(elements, pi + 1, end)
        
        
if __name__ == "__main__":
    elements = [11,9,29,7,2,15,28]
    quick_sort(elements, 0, len(elements) - 1)
    print(elements)