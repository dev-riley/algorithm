import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
heap_abs = []
for i in range(n):
    if i != 0 and len(heap) != 0:
        heapq.heappush(heap, i)
        heap_abs.append(abs(i))
    else:
        min_ = min(heap_abs)
        print(heap_abs.index(min_))
        print(heapq.heappop(heap, heap_abs.index(min_)))