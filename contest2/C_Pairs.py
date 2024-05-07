n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l3 = list(map(int, input().split()))

pair = 0
for a in l1:
    for c in l3:
        if a == l2[c-1]:
            pair += 1

print(pair)