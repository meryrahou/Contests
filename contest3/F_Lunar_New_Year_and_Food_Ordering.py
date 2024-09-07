import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))  # quantities of dishes
c = list(map(int, input().split()))  # costs of dishes

# Create a heap of available dishes (cost, index) to always access the cheapest one
available = [(c[i], i) for i in range(n)]
heapq.heapify(available)

for _ in range(m):
    t, d = map(int, input().split())  
    t -= 1  
    total_cost = 0
    possible = True
    
    # serve as much as possible from the t-th dish
    if a[t] >= d:
        # Serve all d dishes of type t
        total_cost += d * c[t]
        a[t] -= d
        d = 0
    else:
        # Serve as much as we can from type t
        total_cost += a[t] * c[t]
        d -= a[t]
        a[t] = 0
    
    # remaining, use the cheapest available
    while d > 0 and available:
        while available and a[available[0][1]] == 0:
            heapq.heappop(available)
        
        if not available:
            possible = False
            break
        
        cost, idx = available[0]
        if a[idx] >= d:
            # Serve all remaining d dishes
            total_cost += d * cost
            a[idx] -= d
            d = 0
        else:
            # Serve as much as we can from this type
            total_cost += a[idx] * cost
            d -= a[idx]
            a[idx] = 0
    
    if d > 0:
        print(0)
    else:
        print(total_cost)

