from math import inf

rows, cols = map(int, input().split())

matrix = []
for _ in range(rows):
    matrix.append(list(map(int, list(input()))))
diff = [[inf for _ in range(cols)] for _ in range(rows)]

for row in range(rows):
    count = inf
    # going right twice
    for col in range(cols * 2):
        col %= cols
        if matrix[row][col] == 1: count = 0
        else: count += 1

        diff[row][col] = min(diff[row][col], count)
    
    count = inf
    # going left twice
    for col in range(cols * 2 - 1, -1, -1):
        col %= cols
        
        if matrix[row][col] == 1: count = 0
        else: count += 1

        diff[row][col] = min(diff[row][col], count)

# Compute cols
cols = min([sum([diff[row][col] for row in range(rows)]) for col in range(cols)])

if cols == inf: print(-1)
else: print(cols)
