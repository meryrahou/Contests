t = int(input()) 

for _ in range(t):
    n, k = map(int, input().split())  
    produce = list(map(int, input().split())) 

    total_points = 0  

    for i in range(n):
        # points for full pick
        full_pick_points = produce[i] - k  
        if full_pick_points < 0:
            # points if produce < k
            full_pick_points = - (k - produce[i])  

        # points for half pick
        half_pick_points = produce[i] // 2
        
        if half_pick_points > full_pick_points:
            total_points += half_pick_points
            # Update future trees
            for j in range(i + 1, n):
                # Halve the fruit for future trees
                produce[j] //= 2  
        else:
            total_points += full_pick_points  

    print(total_points)  
