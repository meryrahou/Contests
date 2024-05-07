test_cases = int(input())

for _ in range(test_cases):
    n, ops = map(int, input().split())
    elements = sorted(map(int, input().split()))

    for _ in range(ops):
        if sum(elements[2:]) > sum(elements[:-1]):
            elements = elements[2:]  
        else:
            elements = elements[:-1]  

    print(sum(elements))

