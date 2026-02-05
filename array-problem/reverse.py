arr = [2,4,6,8,10]

i = 0
j = len(arr) - 1

while i < j:
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp
    i += 1
    j -= 1

for i in arr:
    print(i, end=" ")