# heapq는 최소 힙만 지원하기 때문에 이 문제처럼 최대 힙을 출력하려면
# 10번째 줄과 16번째 줄처럼 -1을 곱해주면 된다.

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