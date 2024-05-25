t = int(input())

def check(h, arr, x):
    missing_x = 0
    for elem in arr:
        if elem < h:
            missing_x += (h - elem)

    return missing_x <= x

for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    low, high = 1, 10**10

    while low <= high:
        h = (low + high) // 2
        if check(h, arr, x):
            low = h + 1
        else:
            high = h - 1
    print(high)