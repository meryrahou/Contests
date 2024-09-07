t = int(input())
 
for _ in range(t):
    n = int(input())
 
    matriz = [[0 for _ in range(n)] for _ in range(n)]
 
    l, r = 1, n*n
 
    flag = 1
    for i in range(n):
        for j in range(n):
            if flag:
                matriz[i][j] = l
                l += 1
            else:
                matriz[i][j] = r
                r -= 1
            flag ^= 1
 
        if i % 2 == 1:
            matriz[i].reverse()
 
    for i in range(n):
        for j in range(n):
            print(matriz[i][j], end=" " if j != n-1 else "\n")