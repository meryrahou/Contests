nb_test = int(input())

for _ in range(nb_test):
    nb_values = int(input())
    values = list(map(int, input().split()))

    values.sort()

    max_occurrence = 1
    current_occurrence = 1

    for i in range(1, nb_values):
        if values[i] == values[i - 1]:
            current_occurrence += 1
            max_occurrence = max(max_occurrence, current_occurrence)
        else:
            current_occurrence = 1

    operations_needed = nb_values - max_occurrence

    nums_left = operations_needed

    while nums_left > 0:
        operations_needed -= nums_left
        max_occurrence *= 2
        nums_left -= 1

    print(max_occurrence)