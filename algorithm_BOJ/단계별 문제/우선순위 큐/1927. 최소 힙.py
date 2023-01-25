# 12번째 줄에서 보이는 것처럼 바로 print(heapq.heappop(hq)) 하는 것보다
# 리스트에 append해서 한꺼번에 출력하는 것이 시간초과 나지 않는다.

import heapq
n = int(input())
hq = []
res = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if hq:
            res.append(heapq.heappop(hq))
        else:
            res.append(0)
    else:
        heapq.heappush(hq, num)
for num in res:
    print(num)