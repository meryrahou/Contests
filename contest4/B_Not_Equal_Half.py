l = int(input())
array = list(map(int, input().split()))

array.sort()

if sum(array[:l]) == sum(array[l:]):
    print(-1)
else:
    print(*array)
