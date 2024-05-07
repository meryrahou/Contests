n , m = map(int , input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

    
B = [[0 for _ in range(m)] for _ in range(n)]

def mat_equal(A , B):
    if A == B:
        return True
    return False

def add_1(B, r, c):
    B[r][c] = B[r][c+1] = B[r+1][c] = B[r+1][c+1] = 1


def where_A_has_0(A):
    listt = []
    for i in range(n-1):
        for j in range(m-1):
            if A[i][j] == 0 or A[i][j+1] == 0 or A[i+1][j] == 0 or A[i+1][j+1] == 0:
                listt.append([i , j])
    return listt


where_A_has_0 = where_A_has_0(A)



result = []
for i in range(n-1):
    for j in range(m-1):
        if [i , j] not in where_A_has_0:
            add_1(B , i , j)
            result.append([i+1 , j+1])

if mat_equal(A , B):
    print(len(result))
    for line in result:
        print(*line)
else:
    print(-1)