# Read input board
board = [input() for _ in range(3)]

# Initialize counts
individual_heads = 0
team_heads = 0

# Check rows and columns
for i in range(3):
    row = board[i]
    col = ''.join(board[j][i] for j in range(3))
    if row.count(row[0]) == 3:
        individual_heads += 1
    elif len(set(row)) == 2:
        team_heads += 1
    if col.count(col[0]) == 3:
        individual_heads += 1
    elif len(set(col)) == 2:
        team_heads += 1

# Check diagonals
diag1 = ''.join(board[i][i] for i in range(3))
diag2 = ''.join(board[i][2 - i] for i in range(3))
if diag1.count(diag1[0]) == 3:
    individual_heads += 1
elif len(set(diag1)) == 2:
    team_heads += 1
if diag2.count(diag2[0]) == 3:
    individual_heads += 1
elif len(set(diag2)) == 2:
    team_heads += 1

# Print counts
print(individual_heads)
print(team_heads)
