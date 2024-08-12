from sortedcontainers import SortedList

# Number of test cases
t = int(input())

for _ in range(t):
    # Number of sights
    n = int(input())
    
    # Beauties of sights
    beauties = list(map(int, input().split()))
    
    max_beauty_sum = 0
    sorted_list = SortedList()
    
    # Pre-fill with the first three beauties
    if n >= 3:
        sorted_list.add(beauties[0])
        sorted_list.add(beauties[1])
        sorted_list.add(beauties[2])
        max_beauty_sum = sum(sorted_list[-3:]) - 2

    # Slide the window and calculate the sums
    for r in range(3, n):
        sorted_list.add(beauties[r])
        current_max_sum = sum(sorted_list[-3:])
        max_beauty_sum = max(max_beauty_sum, current_max_sum - r)
    
    print(max_beauty_sum)
