def dec_by_tania(n,k):
    for i in range(k):
        if n%10 == 0:
            n = n//10
        else:
            n -= 1
    return n

n , k = map(int, input().split())
print(dec_by_tania(n,k))