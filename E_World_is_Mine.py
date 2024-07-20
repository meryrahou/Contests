t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    tastiness_values = list(map(int, input().strip().split()))

    tastiness_values.sort(reverse=True)
    max_tastiness = 0
    for i in range(n):
        max_tastiness = max(max_tastiness, min(i + 1, tastiness_values[i]))
    
    print(max_tastiness)