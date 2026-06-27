# bubble sort algorithm

def bubble_sort(arr):
    size = len(arr)
    for passes in range(0,size):
        for j in range(0, size -1 - passes):
            if (arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arr1 = [5,46,68,45,98,23,67]
print(bubble_sort(arr1))
