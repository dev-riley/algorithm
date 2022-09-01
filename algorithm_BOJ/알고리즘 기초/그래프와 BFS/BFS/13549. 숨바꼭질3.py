from collections import deque

n, k = map(int, input().split())
MAX = 100001
array = [0] * MAX

def bfs():
    q = deque([n])
    while q:
        v = q.popleft()
        if v == k:
            return array[v]
        for e in (v + 1, v - 1, v * 2):
            if 0 <= e < MAX and not array[e]:
                if e == v * 2 and v != 0:
                    array[e] = array[v]
                    q.appendleft(e)
                else:
                    array[e] = array[v] + 1
                    q.append(e)

print(bfs())