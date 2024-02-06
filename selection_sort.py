array = [10,5,2,11,7,15,23,56]
length = len(array)
flag = False
for i in range(0,length):
    min =  array[i]
    for j in range(i+1,length):
        if min > array[j]:
            min = array[j]
            position = j
            flag = True
    if flag:
        array[position] = array[i]
        array[i] = min
        flag = False
array1 = [print(x) for x in array]
print(len(array1),length)