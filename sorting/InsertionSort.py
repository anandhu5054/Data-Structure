def insertionSort(array):
    for i in range(1,len(array)):
        while array[i-1] > array[i] and i > 0:
            array[i-1], array[i] = array[i], array[i-1]
            i-=1


data_items = [0,0,0,0,1,0,1]
insertionSort(data_items)
print(data_items)