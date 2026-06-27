# binary search algorithm

def binary_search(arr, target):
    size = len(arr)
    start = 0
    end = size - 1

    while(start <= end):
        mid = (start + end)//2

        if (arr[mid]==target):
            return mid
        
        elif (arr[mid] < target):
            start = mid + 1

        elif (arr[mid] > target):
            end = mid - 1

    return -1

        
lst = [23,54,56,78,97,43,67,96]

sorted_list = sorted(lst)
print(sorted_list)
target = 50
result = binary_search(sorted_list, target)
print(result)

print(binary_search(sorted_list, 67))
