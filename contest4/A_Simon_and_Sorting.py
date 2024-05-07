test_case = int(input())

for _ in range(test_case):
    word = input()
    # a b c # YES
    # a c b # YES
    # b a c # YES
    # b c a # NO
    # c a b # NO
    # c b a # Yes
    if word == 'cab' or word == 'bca':
        print('NO')
    else:
        print('YES')
