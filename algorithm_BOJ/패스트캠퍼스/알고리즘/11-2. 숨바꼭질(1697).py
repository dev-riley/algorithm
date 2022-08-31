from collections import deque
n, k = map(int, input().split())
array = [0] * 100001

def bfs():
    q = deque([n])
    while q:
        v = q.popleft()
        if v == k:
            return array[v]
        for e in (v - 1, v + 1, v * 2):
            if 0 <= e < 100001 and not array[e]:
                array[e] = array[v] + 1
                q.append(e)

print(bfs())