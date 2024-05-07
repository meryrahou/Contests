test_cases = int(input())

def beauty_matrix(n, matrix):
    beauty = 0
    nb_beauty = 0
    for i in range(n):
        for j in range(n-1):
            beauty = max(beauty, abs(matrix[i][j] - matrix[i][j+1]))
            beauty = max(beauty, abs(matrix[j][i] - matrix[j+1][i]))
            nb_beauty += 1
    return nb_beauty


for _ in range(test_cases):
    n = int(input())
    nums = [num for num in range(1, n * n +1)]
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    k = 0
    for i in range(n):
        for j in range(n):
            matrix[i][j] = nums[k]
            k += 1
    

    for number in range(n):
        print(*matrix[number])