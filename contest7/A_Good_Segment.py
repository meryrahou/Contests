n = int(input())

a = list(input())

ptr_a = count = max_count = 0
if n == 1: 
    print(1)
else:
    while ptr_a < n-1:
        if ord(a[ptr_a])+1 == ord(a[ptr_a + 1]):
            count += 1
        else:
            count = 0
        max_count = max(max_count , count)
        ptr_a += 1
    print(max_count+1)