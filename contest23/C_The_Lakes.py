testcases = int(input())

def inbound(row, col):
    return (0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != 0)

def dfs(grid, visited, row, col):
    stack = [(row, col)]
    s = 0

    while stack:
        row, col = stack.pop()
        if not visited[row][col]:
            s += grid[row][col]
            visited[row][col] = True

            for row_change, col_change in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row, new_col) and not visited[new_row][new_col]:
                    stack.append((new_row, new_col))

    return s

for i in range(testcases):
    n, m = map(int, input().split())
    grid = []
    for j in range(n):
        grid.append(list(map(int, input().split())))

    visited = [[False for i in range(m)] for j in range(n)]

    s = 0
    for row in range(n):
        for col in range(m):
            if grid[row][col] != 0 and not visited[row][col]:
                s = max(dfs(grid, visited, row, col), s)

    print(s)
