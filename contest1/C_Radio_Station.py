n , m = map(int, input().split())

commands_dictionnary = {}
for i in range(n):
    k = input().split()
    commands_dictionnary.update({k[1]:k[0]})

for i in range(m):
    k = input().split()
    k[1] = k[1][:-1]
    if k[1] in commands_dictionnary:
        print(k[0] + ' ' + k[1] + '; #' + commands_dictionnary[k[1]])

