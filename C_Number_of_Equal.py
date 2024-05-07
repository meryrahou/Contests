n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0
ptr_a = ptr_b = 0

while ptr_a < n and ptr_b < m:
    # Move pointers while elements are smaller (avoid infinite loop)
    while ptr_a < n - 1 and a[ptr_a] == a[ptr_a + 1]:
        ptr_a += 1
    while ptr_b < m - 1 and b[ptr_b] == b[ptr_b + 1]:
        ptr_b += 1

    if a[ptr_a] == b[ptr_b]:
        # Count all matches in the array with FEWER duplicates (modified logic)
        duplicates_a = 0
        while ptr_a < n and a[ptr_a] == a[ptr_a - 1]:
            duplicates_a += 1
            ptr_a += 1
        count += duplicates_a + 1  # Count all elements with same value in a (including duplicates)

        # Move ptr_b to the next non-matching element in b
        while ptr_b < m and b[ptr_b] == a[ptr_a - 1]:
            ptr_b += 1
    elif a[ptr_a] < b[ptr_b]:
        ptr_a += 1
    else:
        ptr_b += 1

print(count)
