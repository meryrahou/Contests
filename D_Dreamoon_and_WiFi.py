s1 = input()
s2 = input()

n = len(s1)
pos = neg = recognised = unrecognised = 0

for i in range(n):
    if s1[i] == '+':
        pos += 1
    elif s1[i] == '-':
        neg += 1
    if s2[i] == '+':
        recognised += 1
    elif s2[i] == '-':
        recognised += 1
    elif s2[i] == '?':
        unrecognised += 1

correct_outcomes = abs(pos - neg) + recognised
total_outcomes = 2 ** unrecognised

probability = correct_outcomes / total_outcomes
print("{:.12f}".format(probability))
