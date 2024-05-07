max_diff , problems = map(int, input().split())
difficulties = list(map(int, input().split()))


list_probs = [0] * max_diff

return_char = ''


# def can_round(list_probs):
#     if 0 not in list_probs:
#         for i in range(len(list_probs)):
#             list_probs[i] -= 1
#         return True
#     return False

# for problem in difficulties:
#     list_probs[problem - 1] += 1
#     if can_round(list_probs):
#         return_char += '1'
#     else:
#         return_char += '0'


# fixing it in order not to exceed time limit
for problem in difficulties:
    list_probs[problem - 1] += 1
    if 0 not in list_probs:
        for i in range(len(list_probs)):
            list_probs[i] -= 1
        return_char += '1'
    else:
        return_char += '0'

print(return_char)


