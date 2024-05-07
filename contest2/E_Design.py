n , q = map(int, input().split())
words = list(map(str, input().split()))
queries = []
for _ in range(q):
    queries.append(list(map(str, input().split())))

def is_valid(word, query):
    pref , suff = query[0] , query[1]
    word_pref = ''
    word_suff = ''
    for t in range(len(pref)):
        word_pref += word[t]
    for t in range(len(suff)):
        word_suff += word[-len(suff)+t]
    if word_pref == pref and word_suff == suff:
        return True
    return False

for query in queries:
    largest_word = ''
    largese_word_index = -1 
    for word in words:
        if is_valid(word, query):
            if len(word) > len(largest_word):
                largest_word = word
                largese_word_index = words.index(word)

    if largese_word_index == -1 :
        print(-1)
    else:
        print(largese_word_index)