from collections import deque
def bfs():
    q = deque([n])
    while q:
        v = q.popleft()
        if v == k:
            return array[v]
        for i in (v-1, v + 1, 2 * v):
            if 0 <= i < 100001 and not array[i]:
                array[i] = array[v] + 1
                q.append(i)

n, k = map(int, input().split())
array = [0] * 100001

print(bfs())