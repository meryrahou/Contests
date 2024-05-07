testcases = int(input())

for _ in range(testcases):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))

    total_difference = 0

    for element in a:
        max_diff = float('-inf')
        max_diff_index = -1

        for i in range(len(b)):
            current_diff = abs(element - b[i])
            if current_diff > max_diff:
                max_diff = current_diff
                max_diff_index = i

        total_difference += max_diff
        if max_diff_index != -1:
            b.pop(max_diff_index)

    print(total_difference)
