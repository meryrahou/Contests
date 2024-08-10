import heapq

def max_army_power(test_cases):
    results = []
    for cards in test_cases:
        max_heap = []
        total_power = 0
        
        for card in cards:
            if card > 0:
                heapq.heappush(max_heap, -card)  # Use negative to simulate max-heap
            else:  # Hero card encountered
                if max_heap:
                    total_power += -heapq.heappop(max_heap)
        
        results.append(total_power)
    
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    cards = list(map(int, input().split()))
    test_cases.append(cards)

results = max_army_power(test_cases)

for result in results:
    print(result)
