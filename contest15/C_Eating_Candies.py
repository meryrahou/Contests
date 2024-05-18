t = int(input())

for _ in range(t):
    nb_candies = int(input())
    candies = list(map(int, input().split()))

    p1, p2 = 0, nb_candies - 1
    alice, bob = 0, 0
    nb = 0
    if nb_candies == 1:
        print(0)
    else:
        while p1 <= p2:
            if alice <= bob:
                alice += candies[p1]
                p1 += 1
            elif alice > bob:
                bob += candies[p2]
                p2 -= 1
            if alice == bob:
                nb = p1 + nb_candies - p2 - 1

        print(nb)
