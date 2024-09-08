def min_operations(a, b):
    operations = 0
    while b > a:
        if b % 2 == 0:  
            b //= 2
        else:  
            b += 1
        operations += 1
    operations += a - b
    return operations

a, b = map(int, input().split())
print(min_operations(a, b))
