n , s = map(int , input().split())
a = []
for _ in range(n):
    a.append(int(input()))

a.sort()

print(a)
print('----------')

left = 0
case1 = []
case2 = []
for right in range(n):
    diff1 = a[right] - case1[0]
    diff2 = a[right] - case2[0]
    if diff1 <= s:
        case1.append(a[right])
    elif diff2 <= s:
        case2.append(a[right])
    elif diff1 > diff2:
        case2.pop(0)
        case2.append(a[right])
    else:
        case1.pop(0)
        case1.append(a[right])
    


print('----------')
print(case1)
print(case2)
print(len(case1)+len(case2))
