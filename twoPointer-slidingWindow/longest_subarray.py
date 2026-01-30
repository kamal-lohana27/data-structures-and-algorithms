arr = [2,5,1,7,10]

max_len = 0
k = 14
for i in range(len(arr)):
    sum = 0
    for j in range(i, len(arr)):
        sum = sum + arr[j]
        if sum <= k:
            max_len = max(max_len, j - i + 1)
        elif sum > k:
            break    

print(max_len)
 