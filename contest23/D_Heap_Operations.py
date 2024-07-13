import heapq
import sys
input = sys.stdin.read

data = input().strip().split('\n')
records = int(data[0])
operations = data[1:]

heap = []
result = []

for operation in operations:
    parts = operation.split()
    if parts[0] == 'insert':
        val = int(parts[1])
        heapq.heappush(heap, val)
        result.append(f'insert {val}')
    elif parts[0] == 'removeMin':
        if heap:
            heapq.heappop(heap)
        result.append('removeMin')
    elif parts[0] == 'getMin':
        val = int(parts[1])
        while heap and heap[0] < val:
            result.append('removeMin')
            heapq.heappop(heap)
        if not heap or heap[0] > val:
            heapq.heappush(heap, val)
            result.append(f'insert {val}')
        result.append(f'getMin {val}')

print(len(result))
for r in result:
    print(r)
