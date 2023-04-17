#selction sort
def selectionSort(array):
    count=0
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[j], array[i] = array[i], array[j]
                count+=1
    print(count)
array = [4, 5, 12]
selectionSort(array)
print(array) 