arr = [1,2,3,4,6]

def bin_search(arr, target):
    low = 0
    high = len(arr) - 1
    for i in range(len(arr)):
        mid = (low + high) // 2
        if (target == arr[mid]):
            return mid
        elif (target > arr[mid]):
            low = mid + 1
        elif (target < arr[mid]):
            high = mid - 1
    return -1

target = 6

index = bin_search(arr, target)

if (index != -1):
    print (f"Element {target} found at index {index}")
else:
    print (f"Element {target} not found in the array")




