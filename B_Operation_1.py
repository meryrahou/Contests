a, m = map(int, input().split())


def B_operation( a , m ):
    # base case
    if a == 0:
        return 0
    elif a == 1:
        return -1
    
    remainder = a % m
    if remainder == 0:
        return 0
    elif remainder == 1:
        return 1 + B_operation( a - 1 , m )
    elif remainder == 2:
        return 1 + min(B_operation(a - 1, m), B_operation(a - 2, m))

print(B_operation(a, m))