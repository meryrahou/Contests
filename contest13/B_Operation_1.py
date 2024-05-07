a, m = map(int, input().split())

if a < m:
    print(-1)
elif a == m:
    print(m)
else:
    aa = a // 2
    if aa % 2 != 0:
        aa += 1
        while aa % m != 0:
            aa += 1
    print(aa)   