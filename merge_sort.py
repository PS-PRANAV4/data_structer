def merge_sort(array):
    if len(array) > 1:
        half = len(array)//2

        L = array[:half]
        R = array[half:]
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        while i < len(R) and j < len(L):
            if L[j] >= R[i]:
                array[k] = R[i]
                i+=1
            else:
                array[k] = L[j]
                j+=1
            k += 1
        while i < len(R):
            array[k] = R[i]
            k+=1
            i+=1
        while j < len(L):
            array[k] = L[j]
            k+=1
            j+=1
    return array
array = [10,5,2,11,7,15,23,56]

array = merge_sort(array)

print(array)