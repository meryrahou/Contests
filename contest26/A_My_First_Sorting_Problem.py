testcase = int(input())

for i in range(testcase):
    x, y = map(int, input().split())
    print(min(x, y), max(x, y))