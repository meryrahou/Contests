t = int(input())

for _ in range(t):
    nbnails = int(input())
    ropescut = 0
    for _ in range(nbnails):
        nail, rope = map(int, input().split())

        if nail > rope:
            ropescut += 1

    print(ropescut)