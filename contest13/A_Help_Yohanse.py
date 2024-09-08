n = int(input())  

if n == 1:
    print(1)
else:
    arr = list(range(1, n + 1))
    
    for i in range(n, 1, -1):
        arr[i - 1], arr[i - 2] = arr[i - 2], arr[i - 1]
    
    print(" ".join(map(str, arr)))
