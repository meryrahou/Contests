n = int(input())
a = list(map(int, input().split()))

swaps = []

for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if a[j] < a[min_index]:
            min_index = j
    if min_index != i:
        swaps.append((i, min_index))
        a[i], a[min_index] = a[min_index], a[i]

print(len(swaps))
if len(swaps) > 0:
    for i, j in swaps:
        print(i, j)
