import heapq
n = int(input())
heap = []

for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

res = 0
while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    value = one + two
    res += value
    heapq.heappush(heap, value)

print(res)