array = [10,5,2,11,7,15,23,56]
length = len(array)
for i in range(0,length):
    for j in range(0,length - i - 1):
        if array[j] > array[j + 1]:
            value = array[j]
            array[j] = array[j + 1]
            array[j + 1] = value

arra1 = [print(i) for i in array]
del arra1

        