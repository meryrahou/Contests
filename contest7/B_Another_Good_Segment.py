from collections import defaultdict

n , s = map(int , input().split())
a = list(map(int , input().split()))


left , right = 0 , 0
seg = defaultdict(int)

good_seg = 0
for right in range(n):
    seg[a[right]] += 1
    while left < n and len(seg) > s:
        seg[a[left]] -= 1
        if seg[a[left]] == 0:
            del seg[a[left]]
        left += 1
    good_seg += ( right - left + 1)

print(good_seg)



