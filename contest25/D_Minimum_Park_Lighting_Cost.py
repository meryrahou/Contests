n, m = map(int, input().split())

parks = [ tuple(map(int, input().split())) for _ in range(n) ]
lights = [ tuple(map(int, input().split())) for _ in range(m) ]

minCost = float('inf')
parkLighting = [0] * 101

for s,t,c in parks:
    parkLighting[s-1] += c
    parkLighting[t] -= c

for i in range(1,101):
    parkLighting[i] += parkLighting[i-1]

cost = 0

def backTracking(ind):
    global minCost, cost

    if ind == len(lights):
        for parkLight in parkLighting:
            if parkLight > 0:
                return
        minCost = min(minCost, cost)
        return
    
    x,y,z,w = lights[ind]

    cost += w
    for i in range(x-1,y):
        parkLighting[i] -= z
    backTracking(ind+1)

    cost -= w
    for i in range(x-1,y):
        parkLighting[i] += z
    backTracking(ind+1)

backTracking(0)
print(minCost)  