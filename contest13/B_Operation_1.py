a, m = map(int, input().split())

def min_operations(a, m):
    # Start by trying the maximum number of `2` operations
    for twos in range(a // 2, -1, -1):  
        ones = a - 2 * twos  
        total_ops = twos + ones  
        if total_ops % m == 0:   
            print(total_ops)
            return
    print(-1)  

min_operations(a, m)
