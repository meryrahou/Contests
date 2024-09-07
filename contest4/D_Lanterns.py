from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    d = defaultdict(list)
    for _ in range(n):
        x, y = map(int, (input().split()))
        d[x].append(y)
    res = 0
    for i in d:
        d[i].sort(reverse=True)
        res += sum(d[i][:i])
    print(res)