import heapq
n = int(input())
hq = []

for i in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(hq, (-1) * num)
    else:
        if len(hq) == 0:
            print(0)
        else:
            print((-1)*heapq.heappop(hq))