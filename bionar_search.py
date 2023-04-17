def binary(array,low,high,x):
    if high > low :
        mid = low+high//2

        if array[mid] > x :
            return binary(array,low, mid-1,x)
        elif array[mid]<x :
            return binary(array,mid+1,high,x)
        else:
            return mid
    else:
        return -1

array = [1]

result = binary(array,0,len(array),1)

if result == -1:
    print("element not present")
else:
    print("positon is", str(result))
        