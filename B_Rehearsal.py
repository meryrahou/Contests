case = int(input())
talents = []
m = 0
for _ in range(case):
    x, y = map(int, input().split())
    m += x
    for _ in range(x):
        talents.append(y)

print(m, talents)