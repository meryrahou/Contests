n, target = map(int, input().split())
l = list(map(int, input().split()))

found_solution = False

for i in range(n - 3):
    for j in range(i + 1, n - 2):
        for k in range(j + 1, n - 1):
            for m in range(k + 1, n):
                if l[i] + l[j] + l[k] + l[m] == target:
                    found_solution = True
                    print(i + 1, j + 1, k + 1, m + 1)
                    break
            if found_solution:
                break
        if found_solution:
            break
    if found_solution:
        break

if not found_solution:
    print("IMPOSSIBLE")
