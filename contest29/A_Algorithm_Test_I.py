from math import factorial

m = int(input())

ballons = list(map(int, input().split()))

n = len(ballons)

unique_colors = set(ballons)
print(factorial(len(unique_colors)))
