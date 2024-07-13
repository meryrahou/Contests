testcases = int(input())

for i in range(testcases):
    n = int(input())
    listt = list(map(int, input().split()))

    m = 10 ** 9

    for l in range(n-1):
        m = min(max(listt[l], listt[l+1]) - 1, m)
    
    print(m)