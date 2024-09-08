from collections import defaultdict
 
n, k = map(int, input().split())
arr = list(map(int, input().split()))

freq = defaultdict(int)
distinct_count = 0
left = 0
good_segments = 0   

for right in range(n):
    freq[arr[right]] += 1
    if freq[arr[right]] == 1:
        distinct_count += 1

    while freq[arr[right]] >= k and left <= right:
        good_segments += n-right
        freq[arr[left]] -= 1

        if freq[arr[left]] == 0:
            distinct_count -= 1

        left += 1
print(good_segments)
