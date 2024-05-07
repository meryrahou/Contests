n = int(input())
nunmbers = list(map(int, input().split()))

neg = []
pos = []
zero = []

for num in nunmbers:
    if num < 0:
        neg.append(num)
    elif num > 0:
        pos.append(num)
    else:
        zero.append(num)

if len(pos) == 0:
    pos.append(neg.pop())
    pos.append(neg.pop())

if len(neg) % 2 == 0:
    zero.append(neg.pop())

print(len(neg), *neg)
print(len(pos), *pos)
print(len(zero), *zero)