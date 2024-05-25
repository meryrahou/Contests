t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    a = list(map(int, input().split()))

    for i in range(k):
        # go through b matrix and findout 
        # if i color is in half of the border of b matrix

        