damage = list(map(int, input().split()))
num = list(map(int, input().split()))

side1 = damage[0] * num[0] + damage[1] * num[1] + damage[2] * num[2]
side2 = damage[3] * num[3] + damage[4] * num[4]

if side1 > side2:
    print("WIN")
elif side1 < side2:
    print("LOSE")
else:
    print("DRAW")