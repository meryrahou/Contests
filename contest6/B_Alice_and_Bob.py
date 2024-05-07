test_case = int(input())

for _ in range(test_case):
    n , m , k = map(int , input().split())
    a = list(input())
    b = list(input())
    ptr_a = ptr_b = cpt_a = cpt_b = 0
    a.sort()
    b.sort()
    s = []

    while ptr_a < n and ptr_b < m:
        if b[ptr_b] < a[ptr_a]:
            if cpt_b < k:
                s.append(b[ptr_b])
                ptr_b += 1
                cpt_b += 1
                cpt_a = 0
            else:
                s.append(a[ptr_a])
                ptr_a += 1
                cpt_a += 1
                cpt_b = 0
        elif a[ptr_a] <= b[ptr_b]:
            if cpt_a < k:
                s.append(a[ptr_a])
                ptr_a += 1
                cpt_a += 1
                cpt_b = 0
            else:
                s.append(b[ptr_b])
                ptr_b += 1
                cpt_b += 1
                cpt_a = 0

    print(*s ,sep='')
