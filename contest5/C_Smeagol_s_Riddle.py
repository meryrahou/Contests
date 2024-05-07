n = int(input())

for _ in range(n):
    change = 0
    word = input()
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - 1 - i]:
            change += 1
    print(change)