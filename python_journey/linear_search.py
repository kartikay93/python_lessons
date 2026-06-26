import array

print("Array example ------------------")
arr = array.array('i',[1,2,3,4,5])
print(arr)

print("Linear search ------------------")
arr = [30,45,67,37,91]
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i]==target:
            print(f"The {target} is at index: {i}")
            return i
    return -1

index = linear_search(arr, 37)
