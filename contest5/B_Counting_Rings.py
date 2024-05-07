string = input()

m = 0
c = 0

for char in string:
    if char == 'O':
        c += 1
        m = max(m, c)
    else:
        c = 0

print(m)
