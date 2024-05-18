testvase = int(input())

for _ in range(testvase):
    a = list(map(int, input().split()))
    a.sort()
    if a[0] + a[1] >= 10:
        print("YES")
    elif a[1] + a[2] >= 10:
        print("YES")
    elif a[0] + a[2] >= 10:
        print("YES")
    else:
        print("NO")