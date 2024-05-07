from collections import defaultdict

n = int(input())

dict = defaultdict(int)
for _ in range(n):
    file_name = input()
    if file_name in dict:
        dict[file_name] += 1
        print(file_name + str(dict[file_name]))
    else:
        dict[file_name] = 0
        print("OK")