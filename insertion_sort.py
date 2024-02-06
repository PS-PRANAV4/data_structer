array = [10,5,2,11,7,15,23,56]
length = len(array)
for i in range(0,length):
    j = i -1
    key = array[i] 
    while j >=0 and array[j] > key:
        temp = array[j]
        array[j] = array[j + 1]
        array[j + 1] = temp
        j -= 1
arra1 = [print(i) for i in array]
del arra1