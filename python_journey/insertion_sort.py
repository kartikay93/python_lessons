# insertion sort

def insertion_sort(arr):
    n = len(arr)

    for current in range(1,n):
        currentcard = arr[current]
        correctPosition = current - 1

        while correctPosition >= 0:
            if(arr[correctPosition] < currentcard):
                break
            else:
                arr[correctPosition + 1] = arr[correctPosition]
                correctPosition-=1
            arr[correctPosition + 1] = currentcard
    return arr

arr1 = [5,46,68,45,98,23,67]
print(insertion_sort(arr1))
