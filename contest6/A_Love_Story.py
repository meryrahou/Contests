test_cases = int(input())

for _ in range(test_cases):
    s = input()
    count = sum(s[i] != 'codeforces'[i] for i in range(10))
    print(count)