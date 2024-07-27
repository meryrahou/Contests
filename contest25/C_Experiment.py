n = int(input())
needs = []
for _ in range(n):
	s, t, b = map(int, input().split())
	needs.append((s, t, b))


events = []
for s, t, b in needs:
	events.append((s, b))  
	events.append((t + 1, -b))  

events.sort()

current_rooms = 0
max_rooms = 0

for time, change in events:
	current_rooms += change
	max_rooms = max(max_rooms, current_rooms)

print(max_rooms)