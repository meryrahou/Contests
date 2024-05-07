n, q = map(int, input().split())
words = input().split()

for _ in range(q):
    pref, suff = input().split()
    largest_word_index = -1

    for i, word in enumerate(words):
        if word.startswith(pref) and word.endswith(suff):
            largest_word_index = i

    print(largest_word_index)
